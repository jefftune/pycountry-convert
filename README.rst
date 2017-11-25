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
      - |license|
    * - tests
      - |travis| |coveralls|
    * - package
      - |version| |supported-versions| |requires|

.. |docs| image:: https://readthedocs.org/projects/pytz-convert/badge/?style=flat
    :alt: Documentation Status
    :target: https://readthedocs.org/projects/pytz-convert

.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: License Status
    :target: https://opensource.org/licenses/MIT

.. |travis| image:: https://travis-ci.org/TuneLab/pycountry-convert.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/TuneLab/pycountry-convert

.. |coveralls| image:: https://coveralls.io/repos/TuneLab/pycountry-convert/badge.svg?branch=master&service=github
    :alt: Code Coverage Status
    :target: https://coveralls.io/r/TuneLab/pycountry-convert

.. |version| image:: https://img.shields.io/pypi/v/pycountry-convert.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pycountry-convert

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pycountry-convert.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pycountry-convert

.. |requires| image:: https://requires.io/github/TuneLab/pycountry-convert/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/TuneLab/pycountry-convert/requirements/?branch=master

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

- ``convert_country_alpha2_to_continent()``: Convert `country code ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ to continent name.

- ``convert_country_alpha2_to_country_name``: Convert `country code ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ to country name.

- ``convert_country_name_to_country_alpha2()``: Convert country name to `country code ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ .

- ``convert_country_alpha3_to_country_alpha2()``: Convert `country code ISO 3166-1 alpha-3 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`_ to `country code ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ .


Requirements
------------

``pycountry-convert`` module is built upon Python 3 and has dependencies upon
several Python modules available within `Python Package Index PyPI <https://pypi.python.org/pypi>`_.

.. code-block:: bash

    make install-requirements

or


.. code-block:: bash

    python3 -m pip uninstall --yes --no-input -r requirements.txt
    python3 -m pip install --upgrade -r requirements.txt


Dependencies
^^^^^^^^^^^^

- `pycountry <https://pypi.python.org/pypi/pycountry>`_
- `wheel <https://pypi.python.org/pypi/wheel>`_
