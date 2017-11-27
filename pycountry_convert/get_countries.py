#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pycountry-convert


def get_country_alpha2_to_country_name():
    """Return a dict of ISO Alpha2 country codes to country names."""

    import pycountry
    return {x.alpha_2: x.name for x in pycountry.countries}


def get_country_alpha2_to_country_official_name():
    """Return a dict of ISO Alpha2 country codes to country official names."""

    import pycountry
    return {x.alpha_2: x.official_name for x in pycountry.countries}


def get_country_alpha3_to_country_name():
    """Return a dict of ISO Alpha3 country codes to country names."""

    import pycountry
    return {x.alpha_3: x.name for x in pycountry.countries}


def get_country_alpha3_to_country_official_name():
    """Return a dict of ISO Alpha3 country codes to country official names."""

    import pycountry
    return {x.alpha_3: x.official_name for x in pycountry.countries}


def get_country_alpha3_to_country_alpha2():
    """Return a dict of ISO Alpha3 country codes to country names."""

    import pycountry
    return {x.alpha_3: x.alpha_2 for x in pycountry.countries}


def get_country_alpha2_to_country_alpha3():
    """Return a dict of ISO 3166-1 Alpha 2 country codes to ISO 3166-1 Alpha 3."""

    import pycountry
    return {x.alpha_2: x.alpha_3 for x in pycountry.countries}


def get_country_alpha2():
    """Return a list of ISO 3166-1 Alpha 2 country codes."""

    import pycountry
    return [x.alpha_2 for x in pycountry.countries]


def get_country_alpha3():
    """Return a list of ISO 3166-1 Alpha 3 country codes."""

    import pycountry
    return [x.alpha_3 for x in pycountry.countries]


def get_country_name_to_country_alpha2():
    """Return a dict of Country Name to ISO 3166-1 Alpha 2."""

    return {key: value['alpha_2'] for key, value in sorted(get_countries().items())}


def get_country_name_to_country_alpha3():
    """Return a dict of Country Name to ISO 3166-1 Alpha 3."""

    return {key: value['alpha_3'] for key, value in sorted(get_countries().items())}


def get_countries():
    """Return a dict of ISO Alpha3 country codes to country names."""

    dict_countries = {}

    import pycountry

    for cn in pycountry.countries:
        dict_countries.update({cn.name: {'alpha_2': cn.alpha_2, 'alpha_3': cn.alpha_3, 'numeric': cn.numeric} })
        if hasattr(cn, 'official_name'):
            dict_countries.update({cn.official_name: {'alpha_2': cn.alpha_2, 'alpha_3': cn.alpha_3, 'numeric': cn.numeric}})

    # Unofficial Alternate Country Names
    if "Great Britain" not in dict_countries:
        dict_countries.update({"Great Britain": dict_countries["United Kingdom"]})
    if "England" not in dict_countries:
        dict_countries.update({"England": dict_countries["United Kingdom"]})
    if "North Korea" not in dict_countries:
        dict_countries.update({"North Korea": dict_countries["Korea, Democratic People's Republic of"]})
    if "South Korea" not in dict_countries:
        dict_countries.update({"South Korea": dict_countries["Korea, Republic of"]})
    if "United States of America" not in dict_countries:
        dict_countries.update({"United States of America": dict_countries["United States"]})
    return dict_countries