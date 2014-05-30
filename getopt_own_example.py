import sys,getopt

get=getopt.getopt(sys.argv[1:],"i:o:")

# bcz it always in the format of ([[lnjvd],[jefhsd]])
print get[-2]

for i,j in get[-2]:
	print i,j
