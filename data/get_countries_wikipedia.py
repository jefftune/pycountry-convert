#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pycountries
"""
Extract a list of countries, grouped by continent, from Wikipedia
"""

import doctest
import csv

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import re

from pprintpp import pprint
import pycountry


def download_wiki_cntry_list():
    """Downloads the Wikipedia country list in wikitext format.
    """
    url = (
        "http://en.wikipedia.org/wiki/"
        "List_of_sovereign_states_and_dependent_"
        "territories_by_continent?action=raw"
    )
    wikitext = urllib2.urlopen(url).read().decode("utf-8")
    return wikitext.split("\n")


def open_wiki_cntry_list():
    """Open Wikipedia country list
    """
    with open(
        "sovereign_states_and_dependent_territories_by_continent.txt"
    ) as wikipedia_cntry_list:
        wikitext = wikipedia_cntry_list.read()
        return wikitext.split("\n")


def split_list_at_indices(the_list, indices):
    """
    Split a list at a given set of indices
    >>> split_list_at_indices([1,3,5,7,9], [0, 3])
    [[], [1, 3, 5], [7, 9]]
    """
    return [the_list[i:j] for i, j in zip([0] + indices, indices + [None])]


def extract_continents(wikitext_lines):
    """Given a wikitext-format line list,
        extracts the lines that belong to a continent
        for each continent.
    """
    continent_regex = re.compile(r"===([\s|\w]+)===")
    #Generate list of (lines index, continent) tuples
    continents = [
        (idx, continent_regex.match(line).group(1))
            for idx, line in enumerate(wikitext_lines)
                if continent_regex.match(line)
    ]

    continent_lines = split_list_at_indices(
        wikitext_lines,
        [continent[0] for continent in continents]
    )[1:]

    return {
        continents[i][1]: continent_lines[i] for i in range(len(continents))
    }


COUNTRY_REGEX = re.compile(r"\| '+\[?\[?([^\]]+)\]?\]?\'+")


def find_cntry(line):
    """
    >>> find_cntry("| '''[[Germany]]'''")
    'Germany'
    >>> find_cntry("| [[Berlin]]")
    """
    match = COUNTRY_REGEX.match(line)
    if match:
        country = match.group(1)
        if "De facto" in country:
            return None
        if "|" in country:
            return country.partition("|")[2]
        return country
    return None


def extract_countries(lines_by_continent):
    """Extract countries.
    """
    return {
        continent: [find_cntry(line) for line in continent_lines if find_cntry(line)]
            for continent, continent_lines in lines_by_continent.items()
    }


def get_continents_to_countries_from_wiki():
    """Get Continents and Countries from Wikipedia.
    """
    lines = open_wiki_cntry_list()
    lines_by_continent = extract_continents(lines)
    return extract_countries(lines_by_continent)


def get_codes_to_continents_from_wiki():
    """Get Country Codes to Continents from Wikipedia.
    """
    data = {}
    for continent, countries in get_continents_to_countries_from_wiki().items():
        for country_name in countries:
            try:
                country_code = pycountry.countries.get(name=country_name).alpha2
                data[country_code] = continent
                continue
            except KeyError:
                pass

            try:
                country_code = get_country_name_to_2_code_from_wiki(country_name)
                data[country_code] = continent
                continue
            except KeyError:
                pass

    return data


def get_codes_to_countries_from_wiki():
    """Get Country Codes to Countries from Wikipedia.
    """
    data = {}
    for continent, countries in get_continents_to_countries_from_wiki().items():
        for country_name in countries:
            try:
                country_code = pycountry.countries.get(name=country_name).alpha2
                data[country_code] = country_name
                continue
            except KeyError:
                pass

            try:
                country_code = get_country_name_to_2_code_from_wiki(country_name)
                data[country_code] = country_name
                continue
            except KeyError:
                pass

    return data

def get_countries_to_codes_from_wiki():
    """Get Countries to Country Codes from Wikipedia.
    """
    data = {}
    for continent, countries in get_continents_to_countries_from_wiki().items():
        for country_name in countries:
            try:
                country_code = pycountry.countries.get(name=country_name).alpha2
                data[country_name] = country_code
                continue
            except KeyError:
                pass

            try:
                country_code = get_country_name_to_2_code_from_wiki(country_name)
                data[country_name] = country_code
                continue
            except KeyError:
                pass

    return data


def get_3_codes_to_2_codes_from_wiki():
    """Get Countries to Country Codes from Wikipedia.
    """
    data = {}
    for continent, countries in get_continents_to_countries_from_wiki().items():
        for country_name in countries:
            try:
                country_2_code = pycountry.countries.get(name=country_name).alpha2
                country_3_code = pycountry.countries.get(name=country_name).alpha3
                data[country_3_code] = country_2_code
                continue
            except KeyError:
                pass

            try:
                country_3_code = get_country_name_to_3_code_from_wiki(country_name)
                country_2_code = get_country_name_to_2_code_from_wiki(country_name)
                data[country_3_code] = country_2_code
                continue
            except KeyError:
                pass

    return data



def convert_country_name_to_continent(country_name):
    """Convert country name to continent.
    """
    dic = {}

    with open("Continents_to_CountryNames.csv") as continents_file_csv:
        continents_file_csv_content = csv.DictReader(continents_file_csv, delimiter=',')
        for line in continents_file_csv_content:
            dic[line['Country']] = line['Continent']

    if country_name not in dic:
        raise KeyError()

    return dic[country_name]


def convert_country_name_to_code(country_name):
    """Convert country name to country code.
    """
    dic = {}

    with open("CountryCodes_to_CountryNames.csv") as countries_file_csv:
        countries_file_csv_content = \
            csv.DictReader(countries_file_csv, delimiter=',')
        for line in countries_file_csv_content:
            dic[line['Country']] = line['Iso2c']

    if country_name not in dic:
        raise KeyError()

    return dic[country_name]


def get_country_codes_to_continents():
    """Get listing of country codes to continents.
    """
    dic_cntry_continent = {}
    dic_cntry_iso2c = {}
    dic_iso2c_continent = {}

    with open("Continents_to_CountryNames.csv") as continents_file_csv:
        continents_file_csv_content = \
            csv.DictReader(continents_file_csv, delimiter=',')
        for line in continents_file_csv_content:
            dic_cntry_continent[line['Country']] = line['Continent']

    with open("CountryCodes_to_CountryNames.csv") as countries_file_csv:
        countries_file_csv_content = csv.DictReader(countries_file_csv, delimiter=',')
        for line in countries_file_csv_content:
            dic_cntry_iso2c[line['Country']] = line['Iso2c']

    for country_name, continent in dic_cntry_continent.items():
        if country_name in dic_cntry_iso2c:
            country_code = dic_cntry_iso2c[country_name]
            dic_iso2c_continent[country_code] = continent

    return dic_iso2c_continent


def get_country_name_to_2_code_from_wiki(country_name):
    """Get listing of Country names and code from Wikipedia.
    """
    dic = {}

    with open("wikipedia-iso-country-codes.csv") as wikipedia_iso_csv:
        wikipedia_iso_csv_content = csv.DictReader(wikipedia_iso_csv, delimiter=',')
        for line in wikipedia_iso_csv_content:
            dic[line['English short name lower case']] = line['Alpha-2 code']

    if country_name not in dic:
        raise KeyError()

    return dic[country_name]


def get_country_name_to_3_code_from_wiki(country_name):
    """Get listing of Country names and code from Wikipedia.
    """
    dic = {}

    with open("wikipedia-iso-country-codes.csv") as wikipedia_iso_csv:
        wikipedia_iso_csv_content = csv.DictReader(wikipedia_iso_csv, delimiter=',')
        for line in wikipedia_iso_csv_content:
            dic[line['English short name lower case']] = line['Alpha-3 code']

    if country_name not in dic:
        raise KeyError()

    return dic[country_name]



if __name__ == "__main__":
    #Unit-selftest
    doctest.testmod()
    #Print country list
    #pprint(get_continents_to_countries_from_wiki())
    pprint(get_codes_to_countries_from_wiki())
