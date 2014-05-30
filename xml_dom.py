from xml.dom.minidom import parse
import xml.dom.minidom

domtree=xml.dom.minidom.parse('/home/ak/workspace/to.xml')
document=domtree.documentElement
movies=document.getElementsByTagName('movie')
for i in movies:
    print "*********Movie************"
    if i.hasAttribute('title'):
	print "Title:%s" % i.getAttribute('title')


    type=i.getElementsByTagName('type')[0]
    print "type:%s" % type.childNodes[0].data
    format=i.getElementsByTagName('format')[0]
    print "format:%s" % format.childNodes[0].data

"""for movie in movies:
   print "*****Movie*****"
   if movie.hasAttribute("title"):
      print "Title: %s" % movie.getAttribute("title")

   type = movie.getElementsByTagName('type')[0]
   print "Type: %s" % type.childNodes[0].data
   format = movie.getElementsByTagName('format')[0]
   print "Format: %s" % format.childNodes[0].data
   rating = movie.getElementsByTagName('rating')[0]
   print "Rating: %s" % rating.childNodes[0].data
   description = movie.getElementsByTagName('description')[0]
   print "Description: %s" % description.childNodes[0].data"""
	
