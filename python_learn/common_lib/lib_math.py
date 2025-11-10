from math import inf, gcd, lcm, ceil, floor, sqrt, log
from math import perm, comb
from math import isqrt

# #------------------------------------
# # int 最大值與最小值 maxint max int 極限值
# import math  # 這是虛擬的數字 (通常用這個)
# print("math 最大值 :",inf)
# print("math 最小值 :",-inf) #最小值
# print("9223372036854775808 > inf :", 9223372036854775808 > inf)
# print("inf + 1 :", inf + 1)  # inf
# print("inf+1 > inf :", inf+1 > inf) # False

# import sys   # 這是真實的數字
# print("sys  最大值 :",sys.maxsize)  # 最大值 9223372036854775807
# print("sys  最小值 :",-sys.maxsize) # 最小值 -9223372036854775807
# print("9223372036854775808 > sys.maxsize :",9223372036854775808 > sys.maxsize) # True
# print("sys.maxsize+1 > sys.maxsize :",sys.maxsize+1 > sys.maxsize) # True

# #------------------------------------
# # # 最大公因數 greatest common division / greatest common factor O(log(min(a,b)))
# print("最大公因數 :",gcd(105, 140)) # 35
# # # 最小公倍數 Least Common Multiple
# n1, n2 = 105, 140
# print("最小公倍數 :",(n1*n2) // gcd(105, 140)) # 420
# # python3.9 之後才有
# # print("最小公倍數 :",lcm(105, 140))

# #------------------------------------
# < 去除小數點以下 > < 轉 int >
# # # ceil 回傳"大"於此數的最大int
# print("ceil",ceil(5.4))
# print("ceil",ceil(-5.4))
# # # floor 回傳"小"於此數的最大int
# print("floor",floor(5.4))
# print("floor",floor(-5.4))
# # # round 四捨五入成int
# print("round",round(5.4))
# print("round",round(-5.4))
# print("round",round(5.5))
# print("round",round(-5.5))

# # #------------------------------------
# # < sqrt > 平方根,開根號
# print("sqrt(4)",sqrt(4))
# print("sqrt(16)",sqrt(16))
# print("sqrt(17)",sqrt(17))

# # #------------------------------------
# # < log > log
# print("log(10,10)",log(10,10))
# print("log(100,10)",log(100,10))
# print("log(1000,10)",log(1000,10)) # 不是整數3
# print("log(8,2)",log(8,2))

# # #------------------------------------
# # 排列組合 Permutation and Combination
# # < perm > 排列 : P N 取 K
# print("perm(6,3)",perm(6,3))
# # < comb > 組合 : C N 取 K
# print("comb(6,3)",comb(6,3))

# # #------------------------------------
# # 階乘 factorial
mem_fact = [1,1]
def fact(n) :
    while len(mem_fact) <= n :
        mem_fact.append( mem_fact[-1]*(len(mem_fact)) )
    return mem_fact[n]
# print("fact(5)",fact(5))
# print("fact(6)",fact(6))

# # #------------------------------------
# # pow (actually not in math lib, is bulit in function)
print("pow(2,3)",pow(2,3))
print("pow(2,3,5)",pow(2,3, mod = 5)) # 8 % 5 = 3

# # # 特殊(很少用到) #####################################################
# # #------------------------------------
# # < isqrt > 平方根,開根號 + floor
# print("isqrt(4)",isqrt(4))
# print("isqrt(16)",isqrt(15))
# print("isqrt(16)",isqrt(16))
# print("isqrt(17)",isqrt(17))

# 有關數學自己實作 ##################################################
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # other even numbers are not prime
    
    sqrt_n = int(sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):  # check odd numbers only
        if n % i == 0:
            return False
    return True

# print(is_prime(5))
# print(is_prime(10))
# print(is_prime(97))
