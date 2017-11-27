#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2017 TUNE, Inc. (http://www.tune.com)
#  @namespace pycountry-convert

__title__ = 'pycountry-convert'
__version__ = '0.4.0'
__build__ = 0x000400
__version_info__ = tuple(__version__.split('.'))

__author__ = 'jefft@tune.com'
__license__ = 'MIT License'

__python_required_version__ = (3, 0)


from .get_country_pycountry import (
    get_countries,
    get_country_name_to_country_alpha2,
    get_country_name_to_country_alpha3
)

from .get_country_pycountry_mapping import (
    get_country_alpha2_to_country_name,
    get_country_alpha3_to_country_name,
    get_country_alpha3_to_country_alpha2,
    get_country_alpha2_to_country_alpha3
)


from .convert_countries import (
    convert_country_alpha2_to_country_name,
    convert_country_alpha3_to_country_alpha2,
    convert_country_name_to_country_alpha2,
    convert_country_name_to_country_alpha3,
)

from .convert_country_alpha2_to_continent_code import (
    convert_country_alpha2_to_continent_code
)

from .convert_continent_code_to_continent_name import (
    convert_continent_code_to_continent_name
)

from .country_name_format import (
    COUNTRY_NAME_FORMAT_DEFAULT,
    COUNTRY_NAME_FORMAT_LOWER,
    COUNTRY_NAME_FORMAT_UPPER,
    country_name_format
)

from .country_wikipedia import (
    WIKIPEDIA_COUNTRY_NAME_TO_COUNTRY_ALPHA2
)