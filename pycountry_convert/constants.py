#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace pycountry-convert

import sys
import pkg_resources

__title__ = 'pycountry-convert'
__version__ = pkg_resources.get_distribution(__title__).version
__MODULE_VERSION_INFO__ = tuple(__version__.split('.'))
__MODULE_SIG__ = "%s/%s" % (
    __title__,
    __version__
)

__python_required_version__ = (3, 0)

__PYTHON_VERSION__ = 'Python/%d.%d.%d' % (
    sys.version_info[0],
    sys.version_info[1],
    sys.version_info[2]
)
