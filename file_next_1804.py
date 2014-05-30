o=open('next.txt','r+')
for i in range(5):
	print 'next',o.next()
#	o.seek(0)
	print 'read',o.read()
#	o.seek(0)

