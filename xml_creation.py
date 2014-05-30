import xml.etree.cElementTree as et
root=et.Element("root")
doc=et.SubElement(root,'doc')
tree=et.ElementTree(root)
tree.write('myxml.xml')
