import os
import time
import linecache
os.system('pause')
time.sleep(0.1)
a=0
for j in range(1,6546):
    files="C:/Users/User/Desktop/Bad Apple/txt/%s.txt"%(j)
    time.sleep(0.02)
    for i in range(1,36):
        if i%36==0:
            continue
        text = linecache.getline(files,i)
        text+="\n"
        print(text)
f.close()