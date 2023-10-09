import random

# # 隨機產生 int 
# # random.randint(a, b)  a跟b都是有可能產出的數字 
# print([random.randint(1, 3) for i in range(10)])

# #------------------------------------
# # 隨機list的順序
# ll = list(range(10))
# random.shuffle(ll)
# print("shuffle :",ll)

# #------------------------------------
# # 隨機從 list 中選一個出來 : choice
# ll = list(range(10))
# print("choice :", random.choice(ll))

# #------------------------------------
# # 從 List 中挑選一個，並刪除此項
# # 方法1 : random indx (OK)
# from random import randrange
# import time
# def rand_remove1():
#     ll = list(range(100000))
#     random.shuffle(ll)
#     for _ in range(100000) :
#         rand_item = ll.pop(randrange(len(ll)))
# # # 方法2 : random indx (慢很多)
# # def rand_remove2():
# #     ll = list(range(100000))
# #     random.shuffle(ll)
# #     for _ in range(100000) :
# #         rand_item = random.choice(ll)
# #         ll.remove(rand_item)
        
# # import timeit
# # print("所花時間:",timeit.timeit(rand_remove1, number=3))
# # print("所花時間:",timeit.timeit(rand_remove2, number=3))
