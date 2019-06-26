import json
dict_a={}
list_a=[]
dict_b={}

dict_b={"msg":"good","star":3}
list_a.append(dict_b.copy())	#add dict to list   .copy() creates a shallow copy
dict_b["msg"]="bad"	#pass by ref gives output as all dict over writes
list_a.append(dict_b)
#print(list_a)

dict_a={"product":"some","price":"12","comment":list_a}	#jaso format
#print(dict_a)
#print(dict_a["comment"][0]["msg"]) #print comment at 0th value at list at mgs
#print(len(dict_b["comment"]))
#for x in dict_a["comment"]:
#	print x

print(dict_a)
data=json.dumps(dict_a); #receive jason string
print(data)
data1=json.loads(data)
print(data1["product"])