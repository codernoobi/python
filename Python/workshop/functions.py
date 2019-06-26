import time
import threading
from multiprocessing import Queue

'''def funcA(para1):	#create a function
	print("hello",para1)	#print and concat with passing
	

funcA("hi") 	#function call
'''

'''def funcA():
	count=0
	while(True):
		print("Count is",count)
		count=count+1
		time.sleep(5)	#go to tools and cancle build to stop


def funcB():
	count=100
	while(True):
		print("Count is",count)
		count=count+1
		time.sleep(3)	#go to tools and cancle build to stop

t=threading.Thread(target=funcA)	#multiple threads
t.start()
t=threading.Thread(target=funcB)
t.start()			
t.join()		#to start both simulteneously

#threads can communicate when they share memory

'''
MyQ=Queue()

def func_creator(count):
	global MyQ    #to call a global variable
	while(True):
		MyQ.put(count)
		print("Count is",count)
		count=count+1
		time.sleep(1)

def func_reader(count):
	global MyQ    #to call a global variable
	while(True):
		data=MyQ.get(True)	#non blocking call; does not stop
		print("Count is",count)
		print(data)

t=threading.Thread(target=func_creator,args=(1,))	#at the end of tupple there should be , (1,)
t.start()
t=threading.Thread(target=func_reader)	#at the end of tupple there should be , (1,)
t.start()

