# #------------------------------------
# # Range
# for x in range(2,6):
#     print(x)

# #------------------------------------
# # Range 間隔 (初始值,結束值,間隔)
# for x in range(2,8,3):
#     print(x)

# #------------------------------------
# # foreach 
# for x in [1,3,6,7]:
#     print(x)

# #------------------------------------ 
# # 雙重迴圈
# for x in range(5):
#     for y in range(x):
#         print("*",end="")
#     print("")

# #------------------------------------ 
# # break
# # 請問在第一次 break 之後 下一行會印什麼?
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print("zzzzzzzzzz")
#         print("這裡會break 下一行會印什麼?")
#         break
#         print("yyyyyyyy")
#     print("xxxxxxx")
# print("外面")

# #------------------------------------ 
# # continue
# # 請問在第一次 continue 之後 下一行會印什麼?
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print("zzzzzzzzzz")
#         print("這裡會continue 下一行會印什麼?")
#         continue
#         print("yyyyyyyy")
#     print("xxxxxxx")
# print("外面")

# #------------------------------------ 
# # 如果 break跟continue不熟 可以去練習 1_2_for_break_contin.py

# #------------------------------------ 
# # 使用長度的for迴圈 
# ll = [["A","B"],["C","D","DD"],["E","F"]]
# for x in range(len(ll)) :
#     # print("下一行要for的list : ",ll[x]) # 此行註解打開可以協助理解
#     for y in range(len(ll[x])) :
#         print(ll[x][y])

# #------------------------------------
# # 使用 foreach
# ll = [["A","B"],["C","D","DD"],["E","F"]]
# for x in ll :
#     # print("下一行要for的list : ", x) # 此行註解打開可以協助理解
#     for y in x :
#         print(y)

# #------------------------------------
# # for 裡面初始化變數
# ll = [["A","B"],["C","D","DD"],["E","F"]]
# for x in ll :
#     num = 100
#     for y in x :
#         num = num + 1
#         print(num)

# #------------------------------------
# # for 裡面初始化變數 殘留 坑
# ll = [["A","B"],["C","D","DD"],["E","F"]]
# for x in ll :
#     num = 100
#     for y in x :
#         num = num + 1
#         # # print(num)    #被註解了
# print(num)

# #------------------------------------
# # for 變數複寫 坑
# x = 100
# for x in [1,3,6,7]:
#     print(x)
# print(x)

# # ------------------------------------------------------
# # 更動正在 for each 的 list 坑
# ll = []

# for x in range(10):
#     ll.append(x)

# print(ll)

# for x in ll:
#     print(x)
#     ll.remove(x)

# # ------------------------------------------------------
# # 更動正在 for each 的 list (正確方法)
# ll = []

# for x in range(10):
#     ll.append(x)

# print(ll)

# for x in ll.copy():
#     print(x)
#     ll.remove(x)















