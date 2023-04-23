# # ----------------------
# 基本
# def funcName(aa):
#     return aa+1
# print(func(10))
# # 意義等同 print(10+1)

# # ----------------------
# # 預設值
# def funcName(bb, aa = 1):
#     return aa+1

# print(func(10,20))
# print(func(10))
# print(func())

# # #-------------------------
# # global 代表要用外面(main 宣告)的變數
# string_var = "original"
# def change_l ():
#     global string_var
#     string_var = "can change"
# change_l()
# print("global string_var :",string_var)

# # #-------------------------
# # nonlocal 只能用在 function裡面的function，告訴裡面function 要用外面function的變數
# def function_outside():
#     string_var = "original"
#     def function_inside():
#         nonlocal string_var
#         string_var = "can change"
#     function_inside()
#     print("nonlocal string_var :",string_var)
# function_outside()

# # #-------------------------
# # nonlocal VS nonlocal
# string_var = "original_global"
# def function_outside():
#     string_var = "original_in_function"
#     def function_inside():
#         global string_var  # <------------
#         print("nonlocal VS nonlocal global string_var :",string_var)
#     function_inside()
# function_outside()

# string_var = "original_global"
# def function_outside():
#     string_var = "original_in_function"
#     def function_inside():
#         nonlocal string_var  # <------------
#         print("nonlocal VS nonlocal nonlocal string_var :",string_var)
#     function_inside()
# function_outside()

# # Type hints (這個其實沒有硬性的規定 "所以不會跳錯!!")
# def appoint_return_type(num : int) -> int :
#     print("input num :", num)
#     return 'a'
# print(appoint_return_type(1.5))

