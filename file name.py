import os
path = input('輸入文件路徑：')+'\\'  # 獲取該目錄下所有文件，存入列表中
f = os.listdir(path)
n = 0
for i in f:  # 設置舊文件名（就是路徑+文件名）
    oldname = path+f[n]  # 設置新文件名
    newname = path+str(n+1)+'.jpg'
    os.rename(oldname, newname)
    print(oldname, '已經改名為：', newname)
    n += 1
