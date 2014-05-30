import MySQLdb
conn= MySQLdb.connect('localhost','root','123','arun')
cur=conn.cursor()

p=open('cpa_final1.csv','rb')
d=p.read().split('/home/')
for i in d[1:]:
	f=i.replace('\n',' ')
	z=f.split('|')
	print z
	k=z[0].split('_')[1]
	print k,z[1],z[2],z[-2],z[-1]
	cur.execute("insert into Agreement_CPA_Virtual1 values ('%s','','','%s','%s')"%(k,z[-2],z[-1]))
	conn.commit()
'''	for j in z:
        	if 'Agreement_' in j:
                	s =j.split('_')
			#print s[1]
			cur.execute("insert into Agreement_CPA_Virtual values ('%s','','','','')"%(s[1]))
			#onn.commit()
        	else:
			print z[1],z[2],z[3],z[4]
			cur.execute("insert into Agreement_CPA_Virtual values ('','%s','%s','%s','%s')"%(z[1],z[2],z[3],z[4]))
			#onn.commit()
'''
