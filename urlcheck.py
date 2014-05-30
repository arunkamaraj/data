import urllib2
import re 
def file_exists(location):
	
	print location
	request = urllib2.Request(location)
        request.get_method = lambda : 'HEAD'
        try:
                response = urllib2.urlopen(request)
                print 'True'
		
        except urllib2.HTTPError:
                print 'False'
		

if __name__=="__main__":

	c=['Apply for the cash you need at Lending Stream. Login (http://bit.ly/177ku7R) and use your prefilled application to get started. Representative 4071.5% APR.','Paying on time has its privileges. Get a decision in minutes. Apply Today. Log in to Lending Stream (http://bit.ly/142G2Kg). Representative 4071.5% APR.']
	pattern=(r'http:\/\/bit.ly\/\w*')
	d=[]
	for i in c:
		d.append(re.search(pattern,i).group())
	print d
#	for i in d:
#		print str(i)
#		file_exists(i)
	file_exists(d[0])
	file_exists(d[1])



