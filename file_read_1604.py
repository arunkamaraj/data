o=open('file_write_1604.txt','r')
str=o.read(10)
pos=o.tell()
o.seek(59,2)
pos2=o.tell()

print "content of file ",str,pos,pos2
o.close()
