#!/bin/bash
#   update_version_date.sh
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

export TZ=America/Los_Angeles

changed_files=`git diff --name-only`
deleted_files=`git ls-files --deleted`
added_files=`git ls-files --others --exclude-standard`

today=`date +%F' '%T' '%Z`

echo $today
echo $changed_files
echo $added_files

printf -v sed_repl 's/Date: [0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} [A-Z]{3}/Date: %q/g' "$today"

for f in $changed_files
do
    if [ -f $f ]; then
        e="${f##*.}"
        
        if [ "$e" == "zip" -o "$e" == "egg" -o "$e" == "whl" -o "$e" == "gz" ]
        then
            continue  ### resumes iteration of an enclosing for loop ###
        fi
        
        echo $e

        printf -v sed_repl 's/Date: [0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} [A-Z]{3}/Date: %q/g' "$today"
        sed -i .bak -E "$sed_repl" $f
    fi
done

for f in $added_files
do
    if [ -f $f ]; then
        e="${f##*.}"
        
        if [ "$e" == "zip" -o "$e" == "egg" -o "$e" == "whl" -o "$e" == "gz" ]
        then
            continue  ### resumes iteration of an enclosing for loop ###
        fi
        
        echo $e

        printf -v sed_repl 's/Date: [0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2} [A-Z]{3}/Date: %q/g' "$today"
        sed -i .bak -E "$sed_repl" $f
    fi
done

find . -type f -name '*.bak' -delete

