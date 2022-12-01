import os

file_path = r"D:\test_file.txt"

# 寫檔
fw = open(file_path, "w") # 刪除之前的紀錄 重新寫
fw = open(file_path, "a") # append
fw.write("Now the file has more content!")
fw.close()

# 讀檔
# f = open(file_path) # 預設好像就是讀檔
fr = open(file_path, "r")
print(fr.readline())
fr.close()

input("write successfully! press any key to continue")

os.remove(file_path)