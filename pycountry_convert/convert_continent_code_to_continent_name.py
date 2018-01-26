#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2018 TUNE, Inc. (http://www.tune.com)
#  @namespace pycountry-convert
"""
Convert continent code to continent name.
"""

CONTINENT_CODE_TO_CONTINENT_NAME = {
    'AS': 'Asia',
    'EU': 'Europe',
    'NA': 'North America',
    'SA': 'South America',
    'AF': 'Africa',
    'OC': 'Oceania',
    'AN': 'Antarctica'
}


def convert_continent_code_to_continent_name(continent_2_code):
    """Convert continent code to continent name.
    """
    if continent_2_code is None or len(continent_2_code) != 2:
        raise KeyError("Invalid Continent code: '{0}'".format(continent_2_code))

    if continent_2_code not in CONTINENT_CODE_TO_CONTINENT_NAME:
        raise KeyError("Invalid Continent code: '{0}'".format(continent_2_code))

    return CONTINENT_CODE_TO_CONTINENT_NAME[continent_2_code]
