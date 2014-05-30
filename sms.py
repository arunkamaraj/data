import MySQLdb
import csv
import logging
import glob
import urllib2
import re
import datetime
from datetime import date,timedelta
#conn = MySQLdb.connect('localhost','root','123','arun')
#cur=conn.cursor()
today=datetime.datetime.now().strftime('%Y-%m-%d')
t=date.today() - timedelta(1)
#yesterday=t.strftime('%Y-%m-%d')
yesterday='2013-07-17'
filedate='20130717'
log_filename ='/home/arun.k/smslog/test.log'
logging.basicConfig(filename=log_filename,level=logging.DEBUG)
#config=[]
class mine:

    def read(self,i):
#       c=glob.glob('/home/arun.k/sms/*removed.csv')
#        d=[]
#        for i in range(len(c)):
#        d.append(c[i].split('/')[-1])
#       for i in range(len(c)):
        self.val=i
#       with open('self.val','r') as f:
#       self.c=f.read()
        filein=csv.reader(open(self.val),delimiter='\n')
        filein.next()
        self.d=filein
        logging.debug('%s' %self.d)
    def connt(self):
        self.conn = MySQLdb.connect('wenchuan','arun.k','EAsterly?7','ukl_arunk')
        self.cur=self.conn.cursor()
    def createdb(self):
#        self.cur.execute('drop table sms')
        self.cur.execute("SELECT CASE (SELECT COUNT( * ) FROM information_schema.tables     WHERE table_schema = 'ukl_arunk'     AND table_name = 'sms' ) WHEN 0 THEN 0 ELSE 1 END AS table_exists;")
        self.te=self.cur.fetchall()
        print self.te[0][0]
        if self.te[0][0]==0:
                self.cur.execute('CREATE TABLE `sms` (`id` int(11) NOT NULL AUTO_INCREMENT,`CustID` int(15) NOT NULL,`PhoneNo` VARCHAR(32) NOT NULL,`custemail` VARCHAR(50) ,`name`VARCHAR (50) ,`Amount` int(10),PRIMARY KEY (`id`));')
        else:
                pass

    def insertdb(self):
        #self.count=self.d.count('')
        #logging.debug('empty str count %d' %self.count )
        self.n=[]
        self.o=[]
        self.p=[]
        self.q=[]
        self.r=[]
        #for i in range(self.count):
        #    self.d.remove('')
        #logging.debug('after removing enmpty str')
        #logging.debug('%s' %self.d)
        for j in self.d:
                s=str(j[0]).split(',')
        #for s in self.z:
        #for s in self.d:
        #    if not s.count(''):
                logging.debug('%s' %s)
                self.n.append(s[0])
                self.o.append(s[1])
                self.p.append(s[2])
                self.q.append(s[3])
                self.r.append(s[4])
            #else:
            #    s.remove('')
            #    self.n.append(s[0])
            #                    self.r.append(s[1])
        logging.debug('after removing all strings')
        logging.debug('%s' %self.n)
        logging.debug('%s' %self.o)
        logging.debug('%s' %self.p)
        logging.debug('%s' %self.q)
        logging.debug('%s' %self.r)
        self.tot=len(self.n)
        for k in range(self.tot):
            CustID=self.n[k]
            PhoneNo=self.o[k]
            custemail=self.p[k]
            name=self.q[k]
            Amount=self.r[k]
            self.cur.execute("insert into sms (CustID,PhoneNo,custemail,name,Amount) values (%s,%s,%s,%s,%s)",(CustID,PhoneNo,custemail,name,Amount))
            #self.conn.commit()
            #self.cur.execute('insert into my_family (name,relation) values (%s,%s)', ('arun','me'))
            logging.debug('sucessfully insered!!!!')

    def testing(self):
        self.config=[]
#       self.j
        self.s=[]
        le=[]
        self.x=[]
        self.z=[]
        test1="select count(distinct custid) from uklsoft.DNCCustID  join ukl_arunk.sms using (CustID)  where Updateddatetime < '"+yesterday+"';"
        test2 ="select count(distinct PhoneSMS) from uklsoft.DNCPhoneSMS join ukl_arunk.sms on PhoneNo=PhoneSMS where Updateddatetime < '"+yesterday+"';"
        self.cur.execute(test1)
        self.res=[]
        self.rest1=self.cur.fetchall()
        self.res.append(self.rest1[0][0])
        self.cur.execute(test2)
        self.rest2=self.cur.fetchall()
        self.res.append(self.rest2[0][0])
        print self.res
        if self.res[0]!=0:
                print "issue in adding DNCCustID"
                self.config.append(0)
        else:
                print "eveything corroect in "
                self.config.append(1)
        if self.res[1]!=0:
                print "issue in adding DNCPhoneSMS"
                self.config.append(0)
        else:
                self.config.append(1)

        self.s = glob.glob('/home/arun.k/sms/*.csv')
        for i in self.s:
                if filedate not in i and  "removed" not in i :
                        self.res.append(i)
                        print self.res
        for j in self.res[2:]:
                filein1=csv.reader(open(j),delimiter='\n')
                self.l=[]
                self.l=filein1
#               print self.l
                print "inside the j for loop"
                for x in self.l:
                        z=str(x[0]).split(',')
                        le.append(z[0])
                        print le
                        print "inside the x for loop"
                        if len(le) > 160:
                                print "meg length is more the 160 char in file "+ j
                                self.config.append(0)
                        else:
                                self.config.append(1)
        print self.config
        print le
	pattern=(r'http:\/\/bit.ly\/\w*')
        self.d=[]
        for i in le:
                self.d.append(re.search(pattern,i).group())
		
	for j in len(self.d):
        	file_exists(d[j])
		
	
    def file_exists(location):

    	request = urllib2.Request(location)
        request.get_method = lambda : 'HEAD'
        try:
        	response = urllib2.urlopen(request)
                #return True
		self.config.append('TRUE')
        except urllib2.HTTPError:
                #return False
		self.config.append('FALSE')


    def test_sms(s)
	for o in le:
		print o
		host='localhost'
		port='5554'
		tn = telnetlib.Telnet(host,port)
		t='sms send +5123'+o+'\n'
		tn.write(t)
	
	



"""
import urllib2
import re 
def file_exists(location):
	
	print location
	request = urllib2.Request(location)
        request.get_method = lambda : 'HEAD'
        try:
                response = urllib2.urlopen(request)
                print 'True'
		
        except urllib2.HTTPError:
                print 'False'
		

if __name__=="__main__":

	c=['Apply for the cash you need at Lending Stream. Login (http://bit.ly/177ku7R) and use your prefilled application to get started. Representative 4071.5% APR.','Paying on time has its privileges. Get a decision in minutes. Apply Today. Log in to Lending Stream (http://bit.ly/142G2Kg). Representative 4071.5% APR.']
	pattern=(r'http:\/\/bit.ly\/\w*')
	d=[]
	for i in c:
		d.append(re.search(pattern,i).group())
	print d
#	for i in d:
#		print str(i)
#		file_exists(i)
	file_exists(d[0])
	file_exists(d[1])"""




if __name__=='__main__':
    d=[]
    w=glob.glob('/home/arun.k/sms/*removed.csv')
    c=mine()
    q=mine()
    
    for i in w:
        c=mine()
        c.read(i)
        c.connt()
        c.createdb()
#        c.insertdb()
    	c.testing()
	c.test_sms()
