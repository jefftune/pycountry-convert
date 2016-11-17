#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pycountry-convert

import sys
from pprintpp import pprint

from pycountry_convert import (
    convert_country_2_code_to_country_name,
    convert_country_2_code_to_continent
)


def main():
    cn_continent = convert_country_2_code_to_continent('US')
    pprint(cn_continent)

    cn_continent = convert_country_2_code_to_continent('AU')
    pprint(cn_continent)
    cn_continent = convert_country_2_code_to_continent('NZ')
    pprint(cn_continent)
    cn_continent = convert_country_2_code_to_continent('JP')
    pprint(cn_continent)

    cn_name = convert_country_2_code_to_country_name('JP')
    pprint(cn_name)


if __name__ == '__main__':
    sys.exit(main())
