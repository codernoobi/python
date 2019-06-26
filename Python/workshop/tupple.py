import time
import threading

def func(count):
	while(True):
		print("Count is",count)
		count=count+1
		time.sleep(5)
t=threading.Thread(target=func,args=(1,))	#at the end of tupple there should be , (1,)
t.start()
t=threading.Thread(target=func,args=(100,))	#same function with diff o/p
t.start()