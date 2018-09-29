#多线程实现

import time
import threading

exitFlag = 0

class myThread(threading.Thread):
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadTD = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print("开始线程：" + self.name)
		print_time(self.name,self.counter,5)
		print("退出线程：" + self.name)
		
def print_time(threadName,delay,counter):
		while counter:
			if exitFlag:
				threadName.exit()
			time.sleep(delay)
			print("%s: %s" % (threadName,time.ctime(time.time())))
			counter -= 1

thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程")




#线程同步


import threading
import time

class myThread(threading.Thread):
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
		
	def run(self):
		print("开启线程:"+self.name)
		
		threadLock.acquire()
		print_time(self.name,self.counter,3)
		
		threadLock.release()
		
def print_time(threadName,delay,counter):
		while counter:
			time.sleep(delay)
			print("%s :%s"%(threadName,time.ctime(time.time())))
			counter -= 1
			
threadLock = threading.Lock()
threads = []

thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)


for t in threads:
	t.join()
print("退出主线程")	



'''
import _thread

def print_time(threadName,delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print ("%s: %s" % (threadName,time.ctime(time.time())))
		#返回正在运行的线程的数量
		#print(threading.activeCount()) 
		#返回一个包含正在运行的线程list
		#print(threading.enumerate())
		#返回单前的线程变量
		#print(threading.currentThread())
try:
	_thread.start_new_thread(print_time,("Thread-1",2,))
	_thread.start_new_thread(print_time,("Thread-2",4,))
	
except:
	print("Error:无法启动线程")
	
while 1:
	pass
'''







	