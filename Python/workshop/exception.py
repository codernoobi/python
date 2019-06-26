import time
import threading
from multiprocessing import Queue 
MyQ=Queue()

def func_creator(count):
	global MyQ    #to call a global variable
	while(True):
		MyQ.put(count)
		print("Count is",count)
		count=count+1
		time.sleep(5)

def func_reader(count):
	global MyQ    #to call a global variable
	while(True):
		try:
			data=MyQ.get(timeout=2)	#timeout=2 waits 2 seconds before stopping
			print(data)
		except:
			print("Cant wait")
		finally:
			print("done")

t=threading.Thread(target=func_creator,args=(1,))	#at the end of tupple there should be , (1,)
t.start()
t=threading.Thread(target=func_reader,args=(1,))	#at the end of tupple there should be , (1,)
t.start()
