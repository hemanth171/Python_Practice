import urllib
import json

serviceUrl = 'http://python-data.dr-chuck.net/geojson?'

address = raw_input("Enter location:")
url = serviceUrl + urllib.urlencode({'sensor':'false', 'address': address})
print "Retrieving", url

uh = urllib.urlopen(url)
data = uh.read()
print "Retrieved", len(data), "characters"

info = json.loads(data)
place = info["results"][0]["place_id"]
print "Place id", str(place)