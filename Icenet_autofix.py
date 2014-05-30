import MySQLdb
db=MySQLdb.connect('localhost','root','123','arun')
cur=db.cursor()
p=[]
query="""select name from my_family;"""

cur.execute(query)
data=cur.fetchall()
print data
for i in data:
	p.append(str(i[0]))
	print p
for j in range(len(p)):
#	query2="""'select rel from my_family where name=%s',(p[j])"""
#	print query2
	cur.execute('insert into Icenet_test where name=%s',(p[j]))
#	cur.execute(query2)
	final=cur.fetchall()
print "final output"
print final
#	if not final=='NULL' or ' ':
#		query3="""delete from my_family where  
