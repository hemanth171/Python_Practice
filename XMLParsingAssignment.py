import urllib
import xml.etree.ElementTree as ET

serviceUrl = 'http://python-data.dr-chuck.net/comments_323311.xml'

address = raw_input('Enter location: ')
if len(address) < 1: address = serviceUrl
print 'Retrieving', address

uh = urllib.urlopen(address)
data = uh.read()
print 'Retrieved', len(data), 'characters'

tree = ET.fromstring(data)
counts = tree.findall('.//count')
print 'Count:', len(counts)

total = 0
for count in counts:
    comment_count = int(count.text)
    total = total + comment_count
print total