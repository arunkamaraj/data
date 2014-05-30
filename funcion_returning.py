from sys import argv
def add(*args):
	a,b=args
	print "adding",int(a)+int(b)
def sub(*args):
	a,b=args
	print "subtracting",int(a)-int(b)
def mul(*args):
	a,b=args
	print "multiplication",int(a)*int(b)
def div(*args):
 	a,b=args
	print "division", int(a)/int(b)
f,c,d=argv

add(c,d)
sub(c,d)
mul(c,d)
div(c,d)
