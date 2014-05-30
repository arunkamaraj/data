from sys import argv
import getopt


myopt=getopt.getopt(argv[1:],"i:o:")
print myopt
t =myopt[-2]
print "thi is t ",t
print "this is myopt value", myopt
#print "this is arg value ", arg

#for a,b in myopt :
for a,b in t:
	print a,b

