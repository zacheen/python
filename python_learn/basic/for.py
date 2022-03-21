# break
# continue

# #------------------------------------
# # Range 間隔 (初始值,結束值,間隔)
# for x in range(2,8,3):
#     print(x)

# #------------------------------------
# # foreach 
# for x in [1,3,6,7]:
#     print(x)

# #------------------------------------
# # 如果同時要取 index 跟 value 使用 enumerate (list or str)
# 注意 !! 不要同時對 enumerate 的 list 做變動 enumerate 是對當下的list 判斷還有沒有值
# s = "abcd"
# s = ["a","b","c"]
# s = [1,2,3]
# for idx, val in enumerate(s):
#     print(idx, val)

# #------------------------------------
# # 如果同時要取 index 跟 value (map)
# # map 不能直接用 enumerate !! 坑 
# m = {1:"a",2:"b"}
# for key, val in m.items():
#     print(key, val)

# print(list(range(5,-1)))


