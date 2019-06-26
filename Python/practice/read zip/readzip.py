#reading zip file
from zipfile import Zip_file#import

Zip_file=ZipFile('student.zip','r')		#read

print(Zip_file.namelist())		#list of files in zip file

for i in Zip_file.namelist():		#printing content and name of each file
	print('File Name:' ,i)
	print('File Data:', Zip_file.read(i))