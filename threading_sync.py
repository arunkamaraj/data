import threading,time

class MyThread(threading.Thread):
        def __init__(self,no,name,delay):
                threading.Thread.__init__(self)
                self.threadid=no
                self.name=name
                self.delay=delay

        def run(self):
                print self.name,"Thread is started"
		threadlock.acquire()
                func(self.threadid,self.name,self.delay)
                print  self.name,"is completed and lock is released"
		threadlock.release()

def func(no,name,delay):
        count=0
        while count < 5:
                time.sleep(delay)
                print name,time.ctime(time.time())
		count +=1

threadlock=threading.Lock()
threads=[]

t1=MyThread(1,"thread1",1)
t2=MyThread(2,"thread2",2)

t1.start()
t2.start()

threads.append(t1)
threads.append(t2)

#print "after invoke",threads

#print threads
for t in threads:
	t.join()
print "Exiting Main Thread"




