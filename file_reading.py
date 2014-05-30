from sys import argv
script,file_name = argv

value =open(file_name)
print value.read()
value.close()

a=raw_input('give the file name here!!')

def reading(f):
	f.seek(0)
	print f.read()

def rewind(f):
	f.seek(0)
def eachline(f):
	for i in range(3):
		print "this is line",i,f.readline()
		#print  "this is second line",f.readline()

read_again=open(a)
print read_again.read()
print "this is for the test of function"
reading(read_again) 
print "this is for rewinding the file"
rewind(read_again)
print "one by one line"
eachline(read_again)



