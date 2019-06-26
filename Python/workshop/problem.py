'''make a dictionary
give dummy values to it
convert that to JSON string
write to file
'''
import json
'''
dict_a={"msg":"good","star":3} # make a dictionary; give dummy values

data=json.dumps(dict_a)	#convert that to JSON string

myfile=open("dict.json","a")	#write to file
myfile.write(data)
myfile.close()
'''

def get_credentials():
	with open("dict.json") as file:
		data=file.read()
		resultdict=json.loads(data)
		if "lic" in resultdict:
			if(resultdict["lic"]=="1234"):
				print("authozized")
			else:
				print("go home")
		else:
			print("No lic found")

get_credentials()