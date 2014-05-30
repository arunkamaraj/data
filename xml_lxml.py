#mport xml.etree.ElementTree as etree
from lxml import etree
tree=etree.parse('broken.xml')
root=tree.getroot()
for i in root:
        print '************Movie**************'
        print "title :",i.attrib['title']
        for j in i:
                print j.tag,':',j.text

