#file searching
from fnmatch import filter
import os

file_name='*.jpg'
for root,dirs,files in os.walk('/'):
	for filename in filter(files, file_name):
		print(os.path.join(root, filename))