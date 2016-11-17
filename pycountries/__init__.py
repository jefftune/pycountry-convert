#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pycountries

__title__ = 'pycountries'
__version__ = '0.1.2'
__build__ = 0x000101
__version_info__ = tuple(__version__.split('.'))

__author__ = 'jefft@tune.com'
__license__ = 'The MIT License (MIT)'
__copyright__ = 'Copyright 2016 TUNE, Inc.'

__python_required_version__ = (3, 0)

from .country_2_code_to_continent import (
    convert_country_2_code_to_continent
)

from .country_2_code_to_country_name import (
    convert_country_2_code_to_country_name
)

from .country_name_to_country_2_code import (
    convert_country_name_to_country_2_code
)

from .country_3_code_to_country_2_code import (
    convert_country_3_code_to_country_2_code
)

from .constants import (
    __python_required_version__,
    __MODULE_VERSION_INFO__,
    __MODULE_SIG__,
    __PYTHON_VERSION__
)
