# map dict

# #------------------------------------
# # 初始化 list
mm = {0 : "0000"}
print('init :',mm)
# # 賦值 (value 可以是不同型別)
mm[1] = 123
print('set  :',mm)
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
# # 單獨取出 key 值
print(mm.keys())

# #------------------------------------
# # 單獨取出 value 值
print(mm.values())

# #------------------------------------
# # 使用 map 轉型
# nums = [1,3,5]
# # nums = ["1","3","5"]
# mm = map((str), nums)
# for each in mm:
#     print(each)
# # 不能直接取值 
# # print(mm[1])

# # map((str), nums) 功能等同下面三行
# def change(x):
#     return str(x)
# ll = [change(x) for x in nums]
# print("list comprehensive : ",ll)
# #------------------------------------

# 特殊用法 ###########################################
# #------------------------------------
# # 創建一個 尋找有沒有此值的 set
# ll = ["1","2"]
# m = {i:True for i in ll}
# print(m)