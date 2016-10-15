import urllib

data = urllib.urlopen('http://www.dr-chuck.com/page1.htm')
for line in data:
    print line