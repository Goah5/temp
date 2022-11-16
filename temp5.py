# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?"

test_str = "https://steamcommunity.com/sharedfiles/filedetails/?id=1414302321"

subst = "workshop_download_item 294100 "

# You can manually specify the number of replacements by changing the 4th argument
result = re.sub(regex, subst, test_str, 1)

if result:
    print (result)

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.