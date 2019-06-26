file = "10.txt"
size = 10 # in mb

with open(file,'w') as wfile:

    for i in range(size*1024*1024):
        wfile.write("a")
