import urllib2
import re
from os.path import basename
import os
from urlparse import urlsplit
from os.path import expanduser
home = expanduser("~")

def imgpaser(urldata,title):
	default_dir= home + title
	os.makedirs(default_dir)
#	url = "http://www.theguardian.com/world/2014/may/19/narendra-modi-india-election-victory-america-china-pakistan-world"
	url=urldata
	urlContent = urllib2.urlopen(url).read()
	#print urlContent
	# HTML image tag: <img src="url" alt="some_text"/>
	imgUrls = re.findall(r'src="(.*?)"', urlContent)
	#imgUrls = re.findall('a .*?href="(.*?)"', urlContent)

	# download all images
	for imgUrl in imgUrls:
	#    print imgUrl
	    if imgUrl.endswith('.jpg') or imgUrl.endswith('.png') or imgUrl.endswith('.gif'): 
		print imgUrl
		try :
			print "downloading!!!"
	        	imgData = urllib2.urlopen(imgUrl).read()
#			print imgData
	        	f = basename(urlsplit(imgUrl)[2])
#			print f
			fileName = os.path.join(default_dir, f)
#			print fileName
	        	output = open(fileName,'w')
	        	output.write(imgData)
	        	output.close()
		except:
			pass 
#			fileName = basename(urlsplit(imgUrl)[2])
#	                print fileName
#	                output = open(fileName,'w')
#	                output.write(imgUrl)
#	                output.close()
	    else:
		        pass
