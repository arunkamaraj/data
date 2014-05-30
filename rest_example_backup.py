import util
import img_parser
import json
import urllib
#applicationKey='2ugtcs5mf3s39cgdc2c6b8pp'
# Set the request URL
class album:

	applicationKey='2ugtcs5mf3s39cgdc2c6b8pp' # This is class variable called by class name album.applicationKey scop of his variable is entire class 

	def __init__(self,urldata): # __init__ method invokes while creating object , __xxxx__ initcates built-in method and __xxx is strongly private 
		self.url=urldata
		
	def getting_request(self):
		print "Requested API url \n",self.url
		self.resp = util.request(self.url, album.applicationKey) # Calling util modeule with "."
#		print self.resp
	def interpret_json_response(self):
		self.data = json.loads(self.resp.decode('utf8')) # Interpret the JSON response 
#		print self.data
#		self.albums=self.data['response'] # Extracting Response
		for i in self.data['response']['results']:
			self.weburl = i['webUrl']
			self.webTitle=i['webTitle']
			print self.webTitle
			print self.weburl
			img_parser.imgpaser(self.weburl,self.webTitle)
#		self.albums=self.data['results'] # Extracting Response
#		print self.albums
#		self.weburl =self.albums['content']['webUrl'] #Extracing Web url
#		self.weburl =self.albums['webUrl'] #Extracing Web url

		print "This weburl" ,self.weburl
	

 					
"""url ='http://content.guardianapis.com/world/2014/may/19/narendra-modi-india-election-victory-america-china-pakistan-world'
#nourl='http://explorer.content.guardianapis.com/#/search?page-size=50&format=json'
#nourl='http://explorer.content.guardianapis.com/#/search?page-size=50'
#url='http://api.bbcnews.appengine.co.uk/stories/technology'

# Send the GET request
resp = util.request(url, applicationKey)

#print resp
# Interpret the JSON response 
data = json.loads(resp.decode('utf8'))

#print data
# Get the collection of albums from the result set
#albums = data['ResultSet']
albums=data['response']
weburl =albums['content']['webUrl']
print weburl
webcontent  = util.request(weburl, applicationKey)
#print webcontent
img_parser.imgpaser(weburl)

#obj=album('http://content.guardianapis.com/world/2014/may/19/narendra-modi-india-election-victory-america-china-pakistan-world')
obj=album("http://content.guardianapis.com/world")
obj.getting_request()
obj.interpret_json_response()

