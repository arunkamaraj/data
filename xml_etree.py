import xml.etree.ElementTree as etree
tree=etree.parse('to.xml')
root=tree.getroot()
for i in root:
	print '************Movie**************'
	print "title :",i.attrib['title']
	for j in i:
		print j.tag,':',j.text
