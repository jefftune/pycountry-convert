#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2018 TUNE, Inc. (http://www.tune.com)
#  @namespace pycountry-convert

COUNTRY_NAME_FORMAT_DEFAULT = 'default'
COUNTRY_NAME_FORMAT_UPPER = 'upper'
COUNTRY_NAME_FORMAT_LOWER = 'lower'

COUNTRY_NAME_FORMATS = [COUNTRY_NAME_FORMAT_DEFAULT, COUNTRY_NAME_FORMAT_UPPER, COUNTRY_NAME_FORMAT_LOWER]


def country_name_format(cn_name, cn_name_format=COUNTRY_NAME_FORMAT_DEFAULT):
    if cn_name_format == COUNTRY_NAME_FORMAT_DEFAULT:
        pass
    elif cn_name_format == COUNTRY_NAME_FORMAT_LOWER:
        cn_name = cn_name.lower()
    elif cn_name_format == COUNTRY_NAME_FORMAT_UPPER:
        cn_name = cn_name.upper()

    return cn_name