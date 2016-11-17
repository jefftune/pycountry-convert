#!/bin/bash
#   remove_trailing_whitespaces.sh
#
#   Copyright (c) 2016 Tune, Inc
#   All rights reserved.
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#   THE SOFTWARE.
#
# license   http://opensource.org/licenses/MIT The MIT License (MIT)
# update    $Date: 2016-07-18 15:06:23 PDT$
# copyright Copyright (c) 2016, TUNE Inc. (http://www.tune.com)
#

find pycountry-convert/ -type f -name '*.py' -print0 | xargs -0 sed -i .bak -E "s/[[:space:]]*$//"
find pycountry-convert/ -type f -name '*.md' -print0 | xargs -0 sed -i .bak -E "s/[[:space:]]*$//"

find . -type f -name 'Makefile' -print0 | xargs -0 sed -i .bak -E "s/[[:space:]]*$//"
find . -type f -name 'README*' -print0 | xargs -0 sed -i .bak -E "s/[[:space:]]*$//"
find . -type f -name '*.md' -print0 | xargs -0 sed -i .bak -E "s/[[:space:]]*$//"
find . -type f -name '*.rst' -print0 | xargs -0 sed -i .bak -E "s/[[:space:]]*$//"

find . -type f -name '*.bak' -delete
