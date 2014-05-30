import threading,time

class MyThread(threading.Thread):
	def __init__(self,no,name,delay):
		threading.Thread.__init__(self)
		self.threadid=no
		self.name=name
		self.delay=delay

	def run(self):
		print "Thread is started" 
		func(self.threadid,self.name,self.delay)
		print  self.name,"is completed"

def func(no,name,delay):
	count=0
	while count < 5:
		time.sleep(delay)
		count +=1
		print name,time.ctime(time.time())
	

t1=MyThread(1,"thread1",1)
t2=MyThread(2,"thread2",2)

t1.start()
t2.start()


		
