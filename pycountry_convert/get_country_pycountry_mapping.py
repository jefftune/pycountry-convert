#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pycountry-convert

import functools
from .country_name_format import (
    COUNTRY_NAME_FORMAT_DEFAULT,
    country_name_format
)


@functools.lru_cache()
def get_country_alpha2_to_country_name(format=COUNTRY_NAME_FORMAT_DEFAULT):
    """Return a dict of ISO Alpha2 country codes to country names."""

    import pycountry
    return {x.alpha_2: country_name_format(x.name, format) for x in pycountry.countries}


@functools.lru_cache()
def get_country_alpha2_to_country_official_name(format=COUNTRY_NAME_FORMAT_DEFAULT):
    """Return a dict of ISO Alpha2 country codes to country official names."""

    import pycountry
    return {x.alpha_2: country_name_format(x.official_name, format) for x in pycountry.countries}


@functools.lru_cache()
def get_country_alpha3_to_country_name(format=COUNTRY_NAME_FORMAT_DEFAULT):
    """Return a dict of ISO Alpha3 country codes to country names."""

    import pycountry
    return {x.alpha_3: country_name_format(x.name, format) for x in pycountry.countries}


@functools.lru_cache()
def get_country_alpha3_to_country_official_name(format=COUNTRY_NAME_FORMAT_DEFAULT):
    """Return a dict of ISO Alpha3 country codes to country official names."""

    import pycountry
    return {x.alpha_3: country_name_format(x.official_name, format) for x in pycountry.countries}


@functools.lru_cache()
def get_country_alpha3_to_country_alpha2():
    """Return a dict of ISO Alpha3 country codes to country names."""

    import pycountry
    return {x.alpha_3: x.alpha_2 for x in pycountry.countries}


@functools.lru_cache()
def get_country_alpha2_to_country_alpha3():
    """Return a dict of ISO 3166-1 Alpha 2 country codes to ISO 3166-1 Alpha 3."""

    import pycountry
    return {x.alpha_2: x.alpha_3 for x in pycountry.countries}


@functools.lru_cache()
def get_country_alpha2():
    """Return a list of ISO 3166-1 Alpha 2 country codes."""

    import pycountry
    return [x.alpha_2 for x in pycountry.countries]


@functools.lru_cache()
def get_country_alpha3():
    """Return a list of ISO 3166-1 Alpha 3 country codes."""

    import pycountry
    return [x.alpha_3 for x in pycountry.countries]

