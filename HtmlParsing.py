import urllib
from BeautifulSoup import *

data = urllib.urlopen('https://www.qvc.com').read()
soup = BeautifulSoup(data)
tags = soup('a')
for tag in tags:
    print tag