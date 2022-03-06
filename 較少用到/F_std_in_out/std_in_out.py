# 要接標準輸出到別的地方 sys.stdout

# import sys
# import os

# wr_f = open('./test.txt', "w", encoding='UTF-8')
# os.dup2(sys.stdout, wr_f)

# print('Plase input your name: ')


#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
 
# 打开一个文件
f=open('./test.txt', "w", encoding='UTF-8')
f2 = 1000
# f2=open('./test2.txt', "w", encoding='UTF-8')

print(type(f))
 
# 将这个文件描述符代表的文件，传递给 1 描述符指向的文件（也就是 stdout）
# os.dup2(1, f.fileno())
# os.dup2(f.fileno(), f2.fileno()) 
# os.dup2(f2.fileno(), f.fileno())
 
# print 输出到标准输出流，就是文件描述符1
# f.write('runoob2')
# f2.write('runoob3')
# sys.stdout = f

os.dup2(sys.stdout.fileno(), f2)
f2 = f

print("test1234")
f2.write("56789")

# 关闭文件
f.close()
# f2.close()