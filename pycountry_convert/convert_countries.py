#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2018 TUNE, Inc. (http://www.tune.com)
#  @namespace pycountry-convert

from .country_name_format import (
    COUNTRY_NAME_FORMAT_DEFAULT,
)

from .country_mappings import (
    map_country_name_to_country_alpha2,
    map_country_name_to_country_alpha3,
    list_country_alpha2,
)

from .country_name_format import (
    country_name_format
)

def country_alpha2_to_country_name(country_2_code, cn_name_format=COUNTRY_NAME_FORMAT_DEFAULT):
    """Convert country ISO 3166-1 Alpha-2 code to country name.
    """
    if country_2_code is None or len(country_2_code) != 2:
        raise KeyError("Invalid Country Alpha-2 code: '{0}'".format(country_2_code))

    from .country_mappings import map_country_alpha2_to_country_name

    dict_country_alpha2_to_country_name = map_country_alpha2_to_country_name(cn_name_format)

    if country_2_code not in dict_country_alpha2_to_country_name:
        raise KeyError("Invalid Country Alpha-2 code: '{0}'".format(country_2_code))

    return dict_country_alpha2_to_country_name[country_2_code]


def country_alpha3_to_country_alpha2(country_3_code):
    """Convert country ISO 3166-1 Alpha-3 code to country ISO 3166-1 Alpha-2.
    """
    if country_3_code is None or len(country_3_code) != 3:
        raise KeyError("Invalid Country Alpha-3 code: '{0}'".format(country_3_code))

    from .country_mappings import map_country_alpha3_to_country_alpha2

    dict_country_alpha3_to_country_alpha2 = map_country_alpha3_to_country_alpha2()

    if country_3_code not in dict_country_alpha3_to_country_alpha2:
        raise KeyError("Invalid Country Alpha-3 code: '{0}'".format(country_3_code))

    return dict_country_alpha3_to_country_alpha2[country_3_code]


def country_name_to_country_alpha2(cn_name, cn_name_format=COUNTRY_NAME_FORMAT_DEFAULT):
    """Convert country name to country code ISO 3166-1 Alpha-2.
    """
    if cn_name is None:
        raise KeyError("Invalid Country Name: '{0}'".format(cn_name))

    cn_name = country_name_format(cn_name, cn_name_format)
    dict_country_name_to_country_alpha2 = map_country_name_to_country_alpha2(cn_name_format)

    if len(cn_name) == 3:
        return country_alpha3_to_country_alpha2(cn_name)

    if len(cn_name) == 2:
        if cn_name not in list_country_alpha2:
            raise KeyError("Invalid Country Alpha-2 code: '{0}'".format(cn_name))

        return cn_name

    if cn_name not in dict_country_name_to_country_alpha2:
        raise KeyError("Invalid Country Name: '{0}'".format(cn_name))

    return dict_country_name_to_country_alpha2[cn_name]


def country_name_to_country_alpha3(cn_name, cn_name_format=COUNTRY_NAME_FORMAT_DEFAULT):
    """Convert country name to country code.
    """
    if cn_name is None:
        raise KeyError("Invalid Country Name: '{0}'".format(cn_name))

    cn_name = country_name_format(cn_name, cn_name_format)
    dict_country_name_to_country_alpha3 = map_country_name_to_country_alpha3(cn_name_format)

    if len(cn_name) == 3:
        from .country_mappings import list_country_alpha3

        list_country_alpha3 = list_country_alpha3()
        if cn_name not in list_country_alpha3:
            raise KeyError("Invalid Country Alpha-3 code: '{0}'".format(cn_name))

        return cn_name

    if cn_name not in dict_country_name_to_country_alpha3:
        raise KeyError("Invalid Country Name: '{0}'".format(cn_name))

    return dict_country_name_to_country_alpha3[cn_name]
