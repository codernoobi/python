#screen shot
import PIL.ImageGrab		#pip install pillow
sc=PIL.ImageGrab.grab()		#take screen shot
sc.save('ss.jpg','JPEG')		#save with jpeg format
sc.show()		#show if youneed to see