# Imaginary_number(虛數)

# # 初始化 方法1
# i = 5+2j # j 代表虛數
# print(type(i))
# print("5+2j :",i)
# # 初始化 方法2
# i = complex(5,2)
# print(type(i))
# print("5+2j :",i)

# # 單獨取出整數的部分或複數的部分
# print(i.real)
# print(i.imag)

# # 計算(跟 int 一樣的符號 但是是虛數的規則)
# i = 2j
# print("2j :",i)
# print("2j*2j :",i**2)
# print("2j*2j*2j :",i**3)
# print("2j*2j*2j*2j :",i**4)

# i = 5+2j # j 代表虛數
# print("5+2j**2 :",i**2)

# 計算複數的角度
import numpy as np
import math
i = 2 + 2j
print("複數位置用\"弧度(radians)\"表示 :", np.angle(i)) # 弧度 = (PI/180) * 角度
print("math.pi / 4          :", math.pi / 4)
print("複數位置用\"角度(degrees)\"表示 :", np.angle(i, deg=True))
print("弧度換算角度         :",  np.angle(i) / (math.pi/180) )
