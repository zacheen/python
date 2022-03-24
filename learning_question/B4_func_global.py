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

