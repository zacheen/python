# # ----------------------
# 基本
# def func(aa):
#     return aa+1
# print(func(10))
# # 意義等同 print(10+1)

# # ----------------------
# # 預設值
# def func(aa = 1):
#     return aa+1

# print(func(10))
# print(func())

# # ----------------------
# # 預設值 放後面
# def func(bb, aa = 1):
#     return aa+1

# print(func(10,20))
# print(func(10))
# print(func())

# # ----------------------
# 預設值 放前面
# def func(aa = 1 , bb):
#     return aa+1

# print(func(10,20))
# print(func(10))
# print(func())

# # ----------------------
# # 預設值 是list
# # 預設值的給值只會初始化一次
# def func(bb = []):
#     bb += [1,2]
#     return bb

# print(func(["start"]))
# print(func())
# print(func())
# print(func())
# print(func(["start"]))
# print(func())
