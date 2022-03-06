# #------------------------------------
# # # 初始化 list
# mm = {0:"0000"}
# print(mm)
# # # 賦值
# mm[1] = "123"
# print(mm)
# # # 刪除
# del(mm[1])
# print(mm)
# # # 取值 (不一定有此值)
# print(mm.get(0,"default"))
# print(mm.get(1000,"default"))

# #
ll = ["1","2"]
m = {i:True for i in ll}
print(m)

# #------------------------------------
# 直接 for map 會是 for 全部的 key 值
# mm = {10:"a",20:"b",30:"c"}
# for i in mm :
#     print(i)

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

