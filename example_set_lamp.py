
import urllib
import urllib2

# Switch to input(...) if python3!
system_id = raw_input("Enter system id e.g. 'testsystem':")
color = raw_input("Enter lamp color on format #RRGGBB e.g. #ff00ff:")

data = urllib.urlencode({'color': color})
req = urllib2.Request('https://api.cilamp.se/v1/' + system_id, data)
urllib2.urlopen(req).read()
