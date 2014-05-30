import thread
import time
"""
try:
	thread.start_new_thread(time_fun,("thread1",2,))
	thread.start_new_thread(time_fun,("thread2",3,))
	thread.start_new_thread(time_fun,("thread3",5,))

except:
	print "sorry i could not create thread" 

thread.start_new_thread(time_fun,("thread1",2,))
thread.start_new_thread(time_fun,("thread2",3,))
thread.start_new_thread(time_fun,("thread3",5,)) """

def time_fun(name,delay):
	print "ha ha "
	count=0
	while count < 5:
		time.sleep(delay)
		print name,time.ctime(time.time())
		count = count+1

try:
        thread.start_new_thread(time_fun,("thread1",1,))
        thread.start_new_thread(time_fun,("thread2",2,))
#        thread.start_new_thread(time_fun,("thread3",3,))

except:
        print "sorry i could not create thread"

#while 1 :
#    pass

time.sleep(10)
