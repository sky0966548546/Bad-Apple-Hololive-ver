import os
import time
os.system('cls')
os.system("title 準備開始囉")
os.system('pause')
for a in range(1, 1295):
    c = "title 目前第%s張" % (a)
    os.system(c)
    time.sleep(0.1)
    f = open("C:/Users/User/Desktop/Bad Apple/txt demo/%s.txt" % (a), 'r')
    print(f.read())
    f.close()
