import MySQLdb
import csv
import logging
#conn = MySQLdb.connect('localhost','root','123','arun')
#cur=conn.cursor()
log_filename ='/home/ak/workspace/logs/csvloader.log'
logging.basicConfig(filename=log_filename,level=logging.DEBUG)

class mine():
	
	def read(self):
		with open('/home/ak/workspace/csvtest.csv','r') as f:
			self.c=f.read()

 		self.d=self.c.split('\n')
		logging.debug('%s' %self.d)
	def conn(self):
		self.conn = MySQLdb.connect('localhost','root','123','arun')
		self.cur=self.conn.cursor()
	def createdb(self):
		self.cur.execute('drop table my_family')
		self.cur.execute('CREATE TABLE `my_family` (`id` int(11) NOT NULL AUTO_INCREMENT,`name` varchar(200) NOT NULL,`rel` varchar(200) NOT NULL,PRIMARY KEY (`id`));')
        def insertdb(self):
		self.count=self.d.count('')
		logging.debug('empty str count %d' %self.count )
		self.n=[]
		self.r=[]
		self.z=[]
		for i in range(self.count):
			self.d.remove('')
		logging.debug('after removing enmpty str')
		logging.debug('%s' %self.d)
		for j in self.d:
			self.z.append(j.split(' '))
		for s in self.z:
			if not s.count(''):
				logging.debug('%s' %s)
				self.n.append(s[0])
				self.r.append(s[1])	
			else:
				s.remove('')
				self.n.append(s[0])
                                self.r.append(s[1])
		logging.debug('after removing all strings')
		logging.debug('%s' %self.n)
		logging.debug('%s' %self.r)
		self.tot=len(self.n)
		for k in range(self.tot):
			name=self.n[k]
			rel=self.r[k]
			self.cur.execute('insert into my_family (name,rel) values (%s,%s)',(name,rel))
			self.conn.commit()
			#self.cur.execute('insert into my_family (name,relation) values (%s,%s)', ('arun','me'))
			logging.debug('sucessfully insered!!!!') 
		

if __name__=='__main__':
	d=[]
	c=mine()
	c.read()
	c.conn()
	c.createdb()
        c.insertdb()
    
