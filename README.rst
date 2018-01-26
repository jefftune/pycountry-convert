.. -*- mode: rst -*-

pycountry-convert
-----------------

Extension of Python package `pycountry <https://pypi.python.org/pypi/pycountry>`_ providing conversion functions.


Badges
------

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs| |license|
    * - info
      - |hits| |contributors|
    * - tests
      - |travis| |coveralls|
    * - package
      - |version| |supported-versions|
    * - other
      - |requires|


.. |docs| image:: https://readthedocs.org/projects/pycountry-convert/badge/?style=flat
    :alt: Documentation Status
    :target: http://pycountry-convert.readthedocs.io

.. |hits| image:: http://hits.dwyl.io/tuneinc/pycountry-convert.svg
    :alt: Hits
    :target: http://hits.dwyl.io/tuneinc/pycountry-convert

.. |contributors| image:: https://img.shields.io/github/contributors/tuneinc/pycountry-convert.svg
    :alt: Contributors
    :target: https://github.com/tuneinc/pycountry-convert/graphs/contributors

.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: License Status
    :target: https://opensource.org/licenses/MIT

.. |travis| image:: https://travis-ci.org/tuneinc/pycountry-convert.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/tuneinc/pycountry-convert

.. |coveralls| image:: https://coveralls.io/repos/tuneinc/pycountry-convert/badge.svg?branch=master&service=github
    :alt: Code Coverage Status
    :target: https://coveralls.io/r/tuneinc/pycountry-convert

.. |version| image:: https://img.shields.io/pypi/v/pycountry-convert.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pycountry-convert

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pycountry-convert.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pycountry-convert

.. |requires| image:: https://requires.io/github/tuneinc/pycountry-convert/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/tuneinc/pycountry-convert/requirements/?branch=master

.. end-badges


Install
-------

.. code-block:: bash

    pip install pycountry-convert


Architecture
------------

Using country data derived from wikipedia, this package provides conversion
functions between ISO country names, country-codes, and continent names.


Functions
---------

- ``map_countries(cn_name_format="default", cn_extras={})``: Return a dict of countries with key as country name (standard and official) with ISO 3166-1 values Alpha 2, Alpha 3, and Numeric. This mapping will include countries defined within `pycountry`, Wikipedia, and whatever extra countries provided by parameter `cn_extras`. Parameter `cn_name_format` will format the country name as request to either be using the default layout `"default"`, lowercase `"lower"`, or uppercase `"upper"`.

- ``country_alpha2_to_continent_code()``: Convert `country code ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ to continent name.

- ``country_alpha2_to_country_name(cn_name_format="default")``: Convert `country code ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ to country name.

- ``country_name_to_country_alpha2(cn_name, cn_name_format="default")``: Convert country name to `country code ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ .

- ``country_alpha3_to_country_name(cn_name_format="default")``: Convert `country code ISO 3166-1 alpha-3 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`_ to country name.

- ``country_name_to_country_alpha3(cn_name, cn_name_format="default")``: Convert country name to `country code ISO 3166-1 alpha-3 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`_ .

- ``country_alpha3_to_country_alpha2()``: Convert `country code ISO 3166-1 alpha-3 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`_ to `country code ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ .


Parameter: cn_name_format
---------------------------

- ``COUNTRY_NAME_FORMAT_DEFAULT "default"``: Country names as provide by ``pycountry``.
- ``COUNTRY_NAME_FORMAT_LOWER "lower"``: All lowercase country names.
- ``COUNTRY_NAME_FORMAT_UPPER "upper"``: All uppercase country names.


Parameter: cn_extras
---------------------------

Dictionary of `{ cn_name: cn_alpha2_code, ... }`

Dependencies
------------

``pycountry-convert`` module is built upon Python 3 and has dependencies upon
several Python modules available within `Python Package Index PyPI <https://pypi.python.org/pypi>`_.

- `pycountry <https://pypi.python.org/pypi/pycountry>`_
- `pprintpp <https://pypi.python.org/pypi/pprintpp>`_
