#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pycountry-convert


import functools
from .country_name_format import (
    COUNTRY_NAME_FORMAT_DEFAULT,
    country_name_format
)
from .country_wikipedia import (
    WIKIPEDIA_COUNTRY_NAME_TO_COUNTRY_ALPHA2
)


@functools.lru_cache()
def get_countries(cn_name_format=COUNTRY_NAME_FORMAT_DEFAULT, cn_extra={}):
    """Return a dict of ISO Alpha3 country codes to country names."""
    from pycountry import countries
    from .convert_countries import convert_country_alpha2_to_country_name

    dict_countries = {}

    for cn in countries:
        cn_name = country_name_format(cn.name, cn_name_format)

        dict_countries.update({cn_name: {'alpha_2': cn.alpha_2, 'alpha_3': cn.alpha_3, 'numeric': cn.numeric} })

        if hasattr(cn, 'official_name'):
            cn_name = country_name_format(cn.official_name, cn_name_format)
            dict_countries.update({cn_name: {'alpha_2': cn.alpha_2, 'alpha_3': cn.alpha_3, 'numeric': cn.numeric}})

    # Wikipedia Country Names
    for cn_name_wiki, cn_alpha2 in WIKIPEDIA_COUNTRY_NAME_TO_COUNTRY_ALPHA2.items():
        cn_name_wiki = country_name_format(cn_name_wiki, cn_name_format)

        if cn_name_wiki in dict_countries:
            # pprint(f"Skip: {cn_name_wiki}: {cn_alpha2}")
            continue

        try:
            cn_name = convert_country_alpha2_to_country_name(cn_alpha2, cn_name_format)
        except KeyError as err:
            # pprint(f"Miss: {cn_name_wiki}: {cn_alpha2}")
            continue

        if cn_name not in dict_countries:
            raise KeyError("Invalid Country Name: '{0}'".format(cn_name))

        # pprint(f"Add: {cn_name_wiki}: {cn_alpha2}")
        dict_countries.update({cn_name_wiki: dict_countries[cn_name]})

    # Extra Country Names
    for cn_name_extra, cn_alpha2 in cn_extra.items():
        cn_name_extra = country_name_format(cn_name_extra, cn_name_format)

        if cn_name_extra in dict_countries:
            continue

        try:
            cn_name = convert_country_alpha2_to_country_name(cn_alpha2, cn_name_format)
        except KeyError as err:
            raise

        if cn_name not in dict_countries:
            raise KeyError("Invalid Country Name: '{0}'".format(cn_name))

        dict_countries.update({cn_name_extra: dict_countries[cn_name]})

    return dict_countries


def get_country_name_to_country_alpha2(cn_name_format=COUNTRY_NAME_FORMAT_DEFAULT):
    """Return a dict of Country Name to ISO 3166-1 Alpha 2."""

    return {key: value['alpha_2'] for key, value in sorted(get_countries(cn_name_format).items())}


def get_country_name_to_country_alpha3(cn_name_format=COUNTRY_NAME_FORMAT_DEFAULT):
    """Return a dict of Country Name to ISO 3166-1 Alpha 3."""

    return {key: value['alpha_3'] for key, value in sorted(get_countries(cn_name_format).items())}