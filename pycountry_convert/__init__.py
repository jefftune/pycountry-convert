#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @copyright 2018 TUNE, Inc. (http://www.tune.com)
#  @namespace pycountry-convert

__title__ = 'pycountry-convert'
__version__ = '0.7.2'
__version_info__ = tuple(__version__.split('.'))

__author__ = 'jefft@tune.com'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2018 TUNE, Inc.'


from .country_mappings import (
    map_countries,
    map_country_name_to_country_alpha2,
    map_country_name_to_country_alpha3,
    map_country_alpha2_to_country_name,
    map_country_alpha3_to_country_name,
    map_country_alpha3_to_country_alpha2,
    map_country_alpha2_to_country_alpha3
)
from .convert_countries import (
    country_alpha2_to_country_name,
    country_alpha3_to_country_alpha2,
    country_name_to_country_alpha2,
    country_name_to_country_alpha3,
)
from .convert_country_alpha2_to_continent_code import (
    country_alpha2_to_continent_code
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