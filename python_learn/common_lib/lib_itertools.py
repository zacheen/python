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
# # 1. repeat 是自己跟自己組合
# print(list(product([1,2,3],repeat = 2)))
# print(list(product([1,1,2],repeat = 2)))
# # 2. list 之間的組合
# print(list(product([1,2,3],[3,4])))
# # 如果傳入兩層 list 就會是裡面的各個 list 組合
# A = [[1,2,3],[3,4]]
# print(list(product(*A)))
# A = [[1,2,3],[3,4],[7,8]]
# print(list(product(*A)))

# # -----------------------------------------------
from itertools import permutations
# # combinations 從list中挑n個出來(會重複)
#     # [1,2,3] 挑過 (1,2) 還會有 (2,1)
# # 跟 product 不同的是 "不會挑到同樣的項目"
# # 沒有選擇要挑 n 個出來 : 預設為 len(n)
# print("perm : ",list(permutations([1,2,3],2)))
# print("perm : ",list(permutations([1,2,3])))
# print("perm : ",list(permutations([1,1,2])))
# print("perm : ",list(set(permutations([1,1,2]))))

# # -----------------------------------------------
from itertools import combinations
# # combinations 從list中挑n個出來(不會重複)
#     # [1,2,3] 挑過 (1,2) 就不會有 (2,1)
# # 一定要選擇要挑 n 個出來
# print("comb : ",list(combinations([1,2,3],2)))
# print("comb : ",list(combinations([1,1,2],2)))
# print("comb : ",list(set(combinations([1,1,2],2))))

# # -----------------------------------------------
from itertools import pairwise  # 前一個與後一個 同時取出
# s = "abcdefghijklmnop"
# indx_list = [3,4,6,9,10,12]
# # 不規則split很好用
# indx_list = [0]+indx_list+[len(s)]
# print([s[f:b] for f,b in pairwise(indx_list)])

# # -----------------------------------------------
from itertools import accumulate  # 到此 index 的總和
# num_list = [1,3,6,2,100]
# print(list(accumulate(num_list)))
