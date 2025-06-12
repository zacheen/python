# map dict

# #------------------------------------
# # # 初始化 list
# mm = {0 : "0000"}
# print('init :',mm)
# # # 賦值 (value 可以是不同型別)
# mm[1] = 123
# print('set  :',mm)
# # setdefault
# mm.setdefault(1, "setdefault_value") # 已經有值不會更新
# print('set  :',mm)
# mm.setdefault(5, "setdefault_value")
# print('set  :',mm)
# # # 刪除
# del(mm[1])
# print(mm)
# # # 取值 (不一定有此值)
# print(mm.get(0,"default"))
# print(mm.get(1000,"default"))

# #------------------------------------
# # list 不能當 hash 值 !! 會跳錯
# m = {}
# m[[1]] = 1

# #------------------------------------
# # 直接 for map 會是 for 全部的 key 值
# for i in mm :
#     print(i)

# #------------------------------------
# # 如果同時要取 index 跟 value (map)
# # map 不能直接用 enumerate !! 坑 
# for key, val in mm.items():
#     print(key, val)

# #------------------------------------
# # # 單獨取出 key 值
# print(mm.keys())
# # # 確認有沒有此 key 值
# print("check key :", 1 in mm) # 跟下面的功能相同
# print("check key :", 1 in mm.keys())
# print("check key :", 2 in mm.keys())

# #------------------------------------
# # # 單獨取出 value 值
# print(mm.values())
# # # 確認有沒有此 value 值
# print("check value :", 123 in mm.values())
# print("check value :", 124 in mm.values())

# 特殊用法 ###########################################
# # # <or> ------------------------------------
# # # 把後面的加入前面的，但如果key值相同會覆寫
# comb1 = {"a":3, "b":10, "c":9, 1:"z"}
# comb2 = {"a":5, "b":6,  "d":2}
# print(comb1 | comb2)

# # <與上面作用相同 包括順序>
# for k2,i2 in comb2.items() :
#     comb1[k2] = i2
# print(comb1)

# #------------------------------------
# # 創建一個 尋找有沒有此值的 set
# ll = ["1","2"]
# m = {i:True for i in ll}
# print(m)

