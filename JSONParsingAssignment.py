import urllib
import json

serviceUrl = 'http://python-data.dr-chuck.net/comments_323315.json'

address = raw_input("Enter location:")
if len(address) < 1 : address = serviceUrl
print "Retrieving", address

uh = urllib.urlopen(serviceUrl)
data = uh.read()
print "Retrieved", len(data), "characters"

info = json.loads(data)
comments = info["comments"]
print "Count", len(comments)

total = 0
for comment in comments:
    total = total + int(comment["count"])
print "Sum", total
