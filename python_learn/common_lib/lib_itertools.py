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
# #     會 zip 到最長的結果
# #     如果某一個長度不夠，會用 None 去補充
# #     或使用 fillvalue 指定數值
# for n1,n2 in itertools.zip_longest(l1, l2) :
#     print("zip_longest",n1,n2)
# for n1,n2 in itertools.zip_longest(l1, l2, fillvalue=100) :
#     print("zip_longest",n1,n2)

# # -----------------------------------------------
from itertools import product
# # # product 會回傳全部的組合
# # 1. repeat 是自己跟自己組合
# print(list(product([1,2,3],repeat = 2)))
# print(list(product([1,1,2],repeat = 2)))
# # 2. list 之間的組合
# print(list( (n1,n2) for n1 in [1,2,3] for n2 in [3,4])) # method 1
# print(list(product([1,2,3],[3,4])))                     # method 2
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

# # <全部有可能的組合> <all subset> -----------------------------------------------
# <從全部的項目中 組合所有的可能組合>
def all_subsets(arr):
    len_n = len(arr)
    all_comb = []
    for mask in range(0, 1 << len_n): # 如果要加入空的就從 0 開始
        l = []
        for i,n in enumerate(arr):
            if mask & (1 << i):
                l.append(n)
        all_comb.append(l)
    return all_comb

# # classic : 78. Subsets
# # https://leetcode.com/problems/subsets/description/
# print(all_subsets([1,2,3]))
# print(all_subsets(['a','b']))

# <從特定的項目中 組合所有的可能組合>
import operator
from functools import reduce
def certain_subsets(arr, indexs):
    all_mask = reduce(operator.or_, [1<<i for i in indexs])
    mask = all_mask
    all_comb = []
    while True:
        # print(bin(mask))
        l = []
        for i,n in enumerate(arr):
            if mask & (1 << i):
                l.append(n)
        all_comb.append(l)

        mask = (mask - 1) & all_mask
        if mask == all_mask:
            break
    return all_comb

# print(certain_subsets(["a","b","c","d","e"],[0,2]))

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
# print(list(accumulate(num_list))) # [1, 4, 10, 12, 112]

# # -----------------------------------------------
from itertools import groupby  # 把 key 值相同的項目分組
# # 預設的 key 就是值本身
# s = "1000110111001100001"
# print([(key_value, len(list(group))) for key_value, group in groupby(s)])
# # 也可以設定 key 如何計算
# l = ['c', 'bb', 'b', 'cc', 'aa', 'a']
# print([(key_value, list(group)) for key_value, group in groupby(l, key=len)])
# #      (key_value 長度, 包含什麼項目)

# # -----------------------------------------------
from itertools import cycle  # 會一直循環取出
# num_list = [1,3,6,2,100]
# count = 0
# l = []
# for n in cycle(num_list) :
#     l.append(n)
#     count += 1
#     if count >= 13 :
#         break
# print(l) # [1, 3, 6, 2, 100, 1, 3, 6, 2, 100, 1, 3, 6]

# # cycle 可搭配 zip 使用
# num_list1 = list(i for i in range(10))
# num_list2 = [1,3,6,2]
# l = []
# for info in zip(num_list1, cycle(num_list2)) :
#     l.append(info)
# print(l) # [(0, 1), (1, 3), (2, 6), (3, 2), (4, 1), (5, 3), (6, 6), (7, 2), (8, 1), (9, 3)]