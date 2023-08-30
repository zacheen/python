# 開檔 : 
    # fw = open(FILE_NAME, "w")
    # with open(FILE_NAME, "w") as fw 
# 關檔 : close
# 移動讀寫頭 : seek (移動單位是字元)
# 讀寫頭位置 : tell

import os

file_path_txt = r"D:\test_file.txt"
file_path_bin = r"D:\test_file.bin"

# for byte
import struct
# i : int16
# f : float
# h : int8
# Xs : X 個字的字串
# https://docs.python.org/3/library/struct.html 這裡有更詳細的表

# # 讀寫"字串" ###################################################

# # < 自己控制的 open >
# # 寫檔
# fw = open(file_path_txt, "w") # 刪除之前的紀錄 重新寫
# fw = open(file_path_txt, "a") # append
# fw.write("Now the file has more content!")
# fw.close()

# # 強制規定，寫檔編碼方法
    # # 跟 "# coding:utf-8" 是不一樣的
# fw = open(file_path_txt, "w", encoding='UTF-8')

# # 讀檔
# # fr = open(file_path_txt) # 預設就是讀檔
# fr = open(file_path_txt, "r")
# print(fr.readline())
# fr.close()

# input("write successfully! press any key to continue")
# os.remove(file_path_txt)

# # < 使用 with 結束自動釋放資源 >
# # with 結束會自動 close
# # 寫檔
# with open(file_path_txt, "w") as fw : # 刪除之前的紀錄 重新寫
# # with open(file_path_txt, "a") as fw : # append
#     fw.write("Now the file has more content!")

# # 讀檔
# with open(file_path_txt) as fr : # 預設就是讀檔
# # with open(file_path_txt, "r") as fr :
#     print("whole line : ",fr.readline())

# # 讀取特定位置 seek
# # seek 的單位是字元 (要注意 window 換行有兩個字元)
# with open(file_path_txt) as fr : # 預設就是讀檔
# # with open(file_path_txt, "r") as fr :
#     print("tell 1 : ", fr.tell())
#     fr.seek(5)
#     print("tell 2 : ", fr.tell())
#     print("after seek : ",fr.readline())
#     print("tell 3 : ", fr.tell())

# input("write successfully! press any key to continue")
# os.remove(file_path_txt)

# # 讀寫"字串" end ###################################################

# 讀寫"byte" ###################################################
# 這裡主要講解使用 struct 去拆解 byte 
# numpy(np) 其實也有辦法做到 請看 np.fromfile

# # < string >
# # str 轉 byte
# to_write = b"hello"
# # byte 轉 struct (str 可以不用做這步驟，但是如果要跟其他型態組合就會需要)
# # to_write = struct.pack('5s', to_write)
# print(type(to_write))
# print(to_write)

# # 寫檔
# with open(file_path_bin, "wb") as fw : 
#     fw.write(to_write)

# # 讀檔
# with open(file_path_bin, "rb") as fr :
#     data = fr.read()

# print(type(data))
# print(data)

# input("write successfully! press any key to continue")
# os.remove(file_path_bin)

# # < int >
# # int 轉 byte
# num = 123
# print(type(num))

# to_write = struct.pack('i', num)
# print(type(to_write))
# print(to_write)

# # 寫檔
# with open(file_path_bin, "wb") as fw : 
#     fw.write(to_write)

# # 讀檔
# with open(file_path_bin, "rb") as fr :
#     data = fr.read()

# print(type(data))
# print(data)

# (read_num, ) = struct.unpack('i', data)
# print(type(read_num))
# print(read_num)

# input("write successfully! press any key to continue")
# os.remove(file_path_bin)

# # < long long >
# # 轉 byte
# num = 123437284973894
# print(type(num))

# to_write = struct.pack('q', num)
# print(type(to_write))
# print(to_write)

# # 寫檔
# with open(file_path_bin, "wb") as fw : 
#     fw.write(to_write)

# # 讀檔
# with open(file_path_bin, "rb") as fr :
#     data = fr.read()

# print(type(data))
# print(data)

# (read_num, ) = struct.unpack('q', data)
# print(type(read_num))
# print(read_num)

# input("write successfully! press any key to continue")
# os.remove(file_path_bin)

# 讀寫"byte" end ###################################################

# Error
# UnicodeEncodeError: 'cp950' codec can't encode character 
    # 使用 encoding='UTF-8' 去寫檔通常就不會出錯了
