def changeme(val):
	val.append([10,20])
	print "data inside the function as refernce ",val
	val=['this is new reference']
	print val
	return

data=[1,2,3,4]
print "data before passing",data
changeme(data)
print "data after passing",data




