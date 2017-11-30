#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pycountry-convert

import sys
from pprintpp import pprint

from pycountry_convert import (
    map_countries,
    country_alpha2_to_country_name,
    country_name_to_country_alpha2,
    country_alpha3_to_country_alpha2,

    country_alpha2_to_continent_code,

    COUNTRY_NAME_FORMAT_UPPER
)

def main():
    cn_name_format = COUNTRY_NAME_FORMAT_UPPER
    for key, value in sorted(map_countries(cn_name_format).items()):
        pprint({key: value})

    try:
        cn_continent = country_alpha2_to_continent_code('AA')
        pprint(cn_continent)
    except KeyError as kerr:
        print("Key error: {0}".format(kerr))
    except:
        print("Unexpected error:", sys.exc_info()[0])

    try:
        cn_continent = country_alpha2_to_continent_code(None)
        pprint(cn_continent)
    except KeyError as kerr:
        print("Key error: {0}".format(kerr))
    except:
        print("Unexpected error:", sys.exc_info()[0])

    cn_continent = country_alpha2_to_continent_code('US')
    pprint(cn_continent)

    cn_continent = country_alpha2_to_continent_code('AU')
    pprint(cn_continent)
    cn_continent = country_alpha2_to_continent_code('NZ')
    pprint(cn_continent)
    cn_continent = country_alpha2_to_continent_code('JP')
    pprint(cn_continent)

    cn_name = country_alpha2_to_country_name('JP', cn_name_format)
    pprint(cn_name)

    cn_a2_code = country_name_to_country_alpha2('USA', cn_name_format)
    pprint(cn_a2_code)
    cn_a2_code = country_name_to_country_alpha2('United States', cn_name_format)
    pprint(cn_a2_code)
    cn_a2_code = country_name_to_country_alpha2('South Korea', cn_name_format)
    pprint(cn_a2_code)
    cn_name = country_alpha2_to_country_name(cn_a2_code, cn_name_format)
    pprint(cn_name)

    cn_name = country_alpha2_to_country_name('RU', cn_name_format)
    pprint(cn_name)
    cn_a2_code = country_name_to_country_alpha2(cn_name, cn_name_format)
    pprint(cn_a2_code)
    cn_a2_code = country_alpha3_to_country_alpha2('RUS')
    pprint(cn_a2_code)

    cn_name = country_alpha2_to_country_name('GB', cn_name_format)
    pprint(cn_name)
    cn_name = country_alpha2_to_country_name('US', cn_name_format)
    pprint(cn_name)


if __name__ == '__main__':
    sys.exit(main())
