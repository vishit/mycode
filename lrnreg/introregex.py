#!/usr/bin/python3

import urllib.request
import re
print ('where should we search' )
url = input()
print('so wanna search here ..... ', url)
print ('what are we searching for?')
searchFor = input()
searchMe = urllib.request.urlopen(url).read().decode('utf-8')
if re.search(searchFor, searchMe):
    print ('found a Match')
else:
    print('No match')
