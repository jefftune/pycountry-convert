#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pycountry-convert


def convert_country_alpha2_to_country_name(country_2_code):
    """Convert country ISO 3166-1 Alpha-2 code to country name.
    """
    if country_2_code is None or len(country_2_code) != 2:
        raise KeyError("Invalid Country Alpha-2 code: '{0}'".format(country_2_code))

    from .get_countries import get_country_alpha2_to_country_name

    dict_country_alpha2_to_country_name = get_country_alpha2_to_country_name()

    if country_2_code not in dict_country_alpha2_to_country_name:
        raise KeyError("Invalid Country Alpha-2 code: '{0}'".format(country_2_code))

    return dict_country_alpha2_to_country_name[country_2_code]


def convert_country_alpha3_to_country_alpha2(country_3_code):
    """Convert country ISO 3166-1 Alpha-3 code to country ISO 3166-1 Alpha-2.
    """
    if country_3_code is None or len(country_3_code) != 3:
        raise KeyError("Invalid Country Alpha-3 code: '{0}'".format(country_3_code))

    from .get_countries import get_country_alpha3_to_country_alpha2

    dict_country_alpha3_to_country_alpha2 = get_country_alpha3_to_country_alpha2()

    if country_3_code not in dict_country_alpha3_to_country_alpha2:
        raise KeyError("Invalid Country Alpha-3 code: '{0}'".format(country_3_code))

    return dict_country_alpha3_to_country_alpha2[country_3_code]


def convert_country_name_to_country_alpha2(country_name):
    """Convert country name to country code.
    """
    if country_name is None:
        raise KeyError("Invalid Country Name: '{0}'".format(country_name))

    from .get_countries import get_country_name_to_country_alpha2, get_country_alpha2
    dict_country_name_to_country_alpha2 = get_country_name_to_country_alpha2()

    if len(country_name) == 3:
        return convert_country_alpha3_to_country_alpha2(country_name)

    if len(country_name) == 2:
        list_country_alpha2 = get_country_alpha2()
        if country_name not in list_country_alpha2:
            raise KeyError("Invalid Country Alpha-2 code: '{0}'".format(country_name))

        return country_name

    if country_name not in dict_country_name_to_country_alpha2:
        raise KeyError("Invalid Country Name: '{0}'".format(country_name))

    return dict_country_name_to_country_alpha2[country_name]


def convert_country_name_to_country_alpha3(country_name):
    """Convert country name to country code.
    """
    if country_name is None:
        raise KeyError("Invalid Country Name: '{0}'".format(country_name))

    from .get_countries import get_country_name_to_country_alpha3
    dict_country_name_to_country_alpha3 = get_country_name_to_country_alpha3()

    if len(country_name) == 3:
        from .get_countries import get_country_alpha3

        list_country_alpha3 = get_country_alpha3()
        if country_name not in list_country_alpha3:
            raise KeyError("Invalid Country Alpha-3 code: '{0}'".format(country_name))

        return country_name

    if country_name not in dict_country_name_to_country_alpha3:
        raise KeyError("Invalid Country Name: '{0}'".format(country_name))

    return dict_country_name_to_country_alpha3[country_name]
