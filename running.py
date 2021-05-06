import os
import time
import linecache
os.system('pause')
time.sleep(0.1)
a=0
files="C:/Users/User/Desktop/Bad Apple/badapple.txt"
for i in range(1,104699):
    if i%60==0 or i%60==59 or i%60==58:
        time.sleep(0.02)
        continue
    text = linecache.getline(files,i)
    print(text)
    a+=1
f.close()