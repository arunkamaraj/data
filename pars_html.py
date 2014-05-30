import urllib2
import HTMLParser
response = urllib2.urlopen('http://www.theguardian.com/world/2014/may/19/narendra-modi-india-election-victory-america-china-pakistan-world')
html = response.read() 

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
    		# Only parse the 'anchor' tag.
    		if tag == "a":
       			# Check the list of defined attributes.
       			for name, value in attrs:
           			# If href is defined, print it.
           			if name == "href":
               				if value[len(value)-3:len(value)]=="jpg":
                   				#print value
                   				self.output=value #return the path+file name of the image

parser = MyHTMLParser()
parser.feed(html)
parse.handle_starttag('anchor','href')
imgurl='http://apod.nasa.gov/apod/'+parser.output
