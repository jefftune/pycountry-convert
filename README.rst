.. -*- mode: rst -*-

========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |license|
    * - tests
      - |travis| |coveralls|
    * - package
      - |version| |supported-versions| |requires|

.. |docs| image:: https://readthedocs.org/projects/pycountry-convert/badge/?style=flat
    :alt: Documentation Status
    :target: https://readthedocs.org/projects/pycountry-convert

.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: License Status
    :target: https://opensource.org/licenses/MIT

.. |travis| image:: https://travis-ci.org/TuneLab/pycountry-convert.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/TuneLab/pycountry-convert

.. |coveralls| image:: https://coveralls.io/repos/github/TuneLab/pycountry-convert/badge.svg?branch=master
    :alt: Code Coverage Status
    :target: https://coveralls.io/github/TuneLab/pycountry-convert?branch=master

.. |requires| image:: https://requires.io/github/TuneLab/pycountry-convert/requirements.svg?branch=master
     :target: https://requires.io/github/TuneLab/pycountry-convert/requirements/?branch=master
     :alt: Requirements Status

.. |version| image:: https://img.shields.io/pypi/v/pycountry-convert.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pycountry-convert

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pycountry-convert.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pycountry-convert

.. end-badges

pycountry-convert
========================

``pycountry-convert`` is a Python module for TUNE Multiverse Libraries.


Installation
============


Usage
=====

Using country data derived from wikipedia, this package provides conversion
functions between ISO country names, country-codes, and continent names.

Available functions:

Convert `country code ISO 3166-1 alpha-2`_ to continent name:
    ``convert_country_alpha2_to_continent()``
Convert `country code ISO 3166-1 alpha-2`_ to country name:
    ``convert_country_alpha2_to_country_name()``
Convert country name to `country code ISO 3166-1 alpha-2`_:
    ``convert_country_name_to_country_alpha2()``
Convert `country code ISO 3166-1 alpha-3`_ to `country code ISO 3166-1
alpha-2`_:
    ``convert_country_alpha3_to_country_alpha2()``

.. _country code ISO 3166-1 alpha-2: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
.. _country code ISO 3166-1 alpha-3: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3

License: MIT


Reporting Issues
================
