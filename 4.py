__author__ = 'han'

import requests
import re

url_base = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
# num = '12345'
# num = str(16044/2)
num = '63579'

while 1:
    url = url_base + num
    r = requests.get(url)
    print r.content
    m = re.search("(\d+)", r.content)
    if len(m.groups()) == 1:
        num = m.groups()[0]
    else:
        break


#peak.html
