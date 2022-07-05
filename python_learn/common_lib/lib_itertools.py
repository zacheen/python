import itertools


# # -----------------------------------------------
from itertools import product
# # # product 會回傳全部的組合
# # 1. repeat 自己跟自己組合
# print(list(product([1,2,3],repeat = 2)))
# # 2. list 之間的組合
# print(list(product([1,2,3],[3,4])))
# # 如果傳入兩層 list 就會是裡面的各個 list 組合
# A = [[1,2,3],[3,4]]
# print(list(product(*A)))
# A = [[1,2,3],[3,4],[7,8]]
# print(list(product(*A)))

# # -----------------------------------------------
from itertools import permutations
# permutations 從list中挑兩個出來
# 跟 product 不同的是 "不會挑到同樣的項目"
# print(list(permutations([1,2,3],2)))
# print(list(permutations([1,1,2])))
# print(list(set(permutations([1,1,2]))))
