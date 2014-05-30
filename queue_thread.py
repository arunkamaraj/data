import threading,time,Queue

exit_flag=0

class MyThread(threading.Thread):
	def __init__(self,tid,delay,name,q):
		threading.Thread.__init__(self)
		self.tid=tid
		self.delay=delay
		self.name=name
		self.q=q
	def run(self):
		print "Thread started" + self.name
		func(self.name,self.delay,self.q)
		print "Thread End" + self.name
def func(name,delay,q):
	while  not exit_flag:
		threadlock.acquire()
		if not q.empty():
			data=q.get()
#			print name,time.ctime(time.time()),data
			threadlock.release()
			print name,time.ctime(time.time()),data
		else:
			threadlock.release()
#			print "empty queue"

		time.sleep(1)

threadlock=threading.Lock()
workingq=Queue.Queue(10)
thread=['t1','t2','t3','t4']
ele=['one','two','three','four','five']
tid=1
for i in thread:
	tr=MyThread(tid,tid,i,workingq)
	tr.start()
	tid +=tid

threadlock.acquire()
for i in ele:
	workingq.put(i)

threadlock.release()

while not workingq.empty():
	pass


exit_flag=1
	
		
time.sleep(2)

print "finished"
