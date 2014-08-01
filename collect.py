import urllib2
from settings import *

ONEPERCENT_API_HEADERS = {'Authorization':'Token {0}'.format(ONEPERCENT_API_TOKEN)}

# Latest donations
donations_source_url = "{0}{1}".format(ONEPERCENT_SERVER, '/api/fund/latest-donations/')
request = urllib2.Request(donations_source_url, headers=ONEPERCENT_API_HEADERS)

response = urllib2.urlopen(request)
donation_json = response.read()

donations_url = "{0}{1}".format(STREAM_SERVER, '/donations/')
request = urllib2.Request(donations_url, donation_json, {'Content-Type': 'application/json'})
urllib2.urlopen(request)

# donations_stream_url = "{0}{1}".format(STREAM_SERVER, '/donations/')
# urllib2.Request()


