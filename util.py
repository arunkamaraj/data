import time
import datetime
import urllib2

#def request(url, applicationID, applicationKey):
def request(url, applicationKey):
	
	# Set the request authentication headers
	timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d %H:%M:%S')
	headers = {'DecibelAppKey': '2ugtcs5mf3s39cgdc2c6b8pp',
                   'DecibelTimestamp': timestamp}

	# Send the GET request
	req = urllib2.Request(url, None, headers)

	# Read the response
	return urllib2.urlopen(req).read()
	
