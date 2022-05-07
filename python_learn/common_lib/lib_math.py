import math

# #------------------------------------
# # int 最大值與最小值 maxint max int 極限值
# import math  # 這是虛擬的數字 (通常用這個)
# print("math 最大值 :",math.inf)
# print("math 最小值 :",-math.inf) #最小值
# print("9223372036854775808 > math.inf :", 9223372036854775808 > math.inf)
# print("math.inf + 1 :", math.inf + 1)  # math.inf
# print("math.inf+1 > math.inf :", math.inf+1 > math.inf) # False

# import sys   # 這是真實的數字
# print("sys  最大值 :",sys.maxsize)  # 最大值 9223372036854775807
# print("sys  最小值 :",-sys.maxsize) # 最小值 -9223372036854775807
# print("9223372036854775808 > sys.maxsize :",9223372036854775808 > sys.maxsize) # True
# print("sys.maxsize+1 > sys.maxsize :",sys.maxsize+1 > sys.maxsize) # True

# #------------------------------------
# # # 最大公因數
# print("最大公因數 :",math.gcd(105, 140)) # 35
# # # 最小公倍數
# n1, n2 = 105, 140
# print("最小公倍數 :",(n1*n2) // math.gcd(105, 140)) # 420
# # python3.9 之後才有
# # print("最小公倍數 :",math.lcm(105, 140)) #

# #------------------------------------
# < 去除小數點以下 > < 轉 int >
# # # ceil 回傳"大"於此數的最大int
# print("ceil",math.ceil(5.4))
# print("ceil",math.ceil(-5.4))
# # # floor 回傳"小"於此數的最大int
# print("floor",math.floor(5.4))
# print("floor",math.floor(-5.4))
# # # round 四捨五入成int
# print("round",round(5.4))
# print("round",round(-5.4))
# print("round",round(5.5))
# print("round",round(-5.5))