# #-------------------------
# # global
# ll = 1
# print("before :",ll)

# def change_l ():
#     global ll
#     ll = 2

# change_l()
# print("after  :",ll)

# #-------------------------
# # 沒有用 global
# ll = 1
# print(ll)

# def change_l ():
#     ll = 2

# change_l()
# print(ll)

# #-------------------------
# # 沒有用 global 但預設會抓取外面的 1
# ll = 1
# print(ll)

# def change_l ():
#     print(ll)

# change_l()
# print(ll)

# #-------------------------
# # 沒有用 global 但預設會抓取外面的 2
# ll = "123"
# print(ll)

# def change_l ():
#     aa = ll + "456"
#     print(aa)

# change_l()
# print(ll)

# #-------------------------
# # 又想要 global(取值) 又想要 local(給值) 
# ll = "123"
# print(ll)

# def change_l ():
#     ll = ll + "456"
#     print(ll)

# change_l()
# print(ll)
# # 所以記得要宣告 global 不要用預設會抓取外面的方法取值

# < function 裡面又宣告 function >
# 不管怎樣 inner_def 一定改不到 outer_def 的值
# 錯誤
# # def outer_def():
# #     ll = 0
# #     def inner_def():
# #         print("inner1 :",ll)
# #         ll += 1
# #         print("inner2 :",ll)
# #     inner_def()
# #     print("outer :",ll)
# # outer_def()

# # 只能看到而已
# # def outer_def():
# #     ll = 0
# #     def inner_def():
# #         print("inner1 :",ll)
# #         # ll += 1
# #         # print("inner2 :",ll)
# #     inner_def()
# #     print("outer :",ll)
# # outer_def()

# # << 如果要修改外面的值 >> 
# # 方法1 用 return 修改 outer_def 的值
# def outer_def():
#     ll = 0
#     def inner_def():
#         print("inner1 :",ll)
#         ret = ll + 1
#         print("inner2 :",ret)
#         return ret
#     ll = inner_def()
#     print("outer :",ll)
# outer_def()

# python 有 & 用法嗎 ? nonlocal 類似這種用法
# 方法2 nonlocal
# def outer_def():
#     ll = 0
#     def inner_def():
#         nonlocal ll
#         print("inner1 :",ll) # 0
#         ll = ll + 1
#         print("inner2 :",ll) # 1 有修改到
#     inner_def()
#     print("outer :",ll) # 1 外面也有修改到
# outer_def()


