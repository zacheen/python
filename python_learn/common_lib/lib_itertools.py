import itertools
# https://docs.python.org/3/library/itertools.html

# # -----------------------------------------------
# l1 = [1,2,3]
# l2 = [1,2,3,4,5]
# # < zip > (內建的 不過與下面的相關) 
#     # zip 如果某一個已經到了盡頭，for 就會停止
# for n1,n2 in zip(l1, l2) :
#     print("zip",n1,n2)

# # < zip_longest > 
#     # 會 zip 到最長的結果
#     # 如果某一個長度不夠，會用 None 去補充
# for n1,n2 in itertools.zip_longest(l1, l2) :
#     print("zip_longest",n1,n2)

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
