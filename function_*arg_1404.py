def function(a,*b):
	print a
	for i in b:
		print 'inside *b',i 
	return 

function(10)
function(100,200,300)
