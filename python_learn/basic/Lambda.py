# 如果是要找 [... for ...] 的用法，去看 short_code.py

# Lambda (其實Lambda就是一個function)
# 語法 : 
# 基本用法
    # lambda parameter_list: expression
    # parameter_list 是會帶入的變數
    # expression 是 使用parameter_list做一些事情 做完會return

# ------------------------------------------
# # < function 與 lambda 之間的轉換>
# def normal_func(parameter_list) :
#     return parameter_list*parameter_list

# lambda_func = lambda parameter_list : parameter_list*parameter_list

# print(normal_func(5))
# print(lambda_func(5))

# ------------------------------------------
# # < 是不是從頭跟從尾念過來都一樣 >
# isPalindrome = lambda s : s == s[::-1] 
# print(isPalindrome("aba"))
# print(isPalindrome("abab"))

# ------------------------------------------
# # < filter 搭配 lambda 用法 >  這是因為 filter 本來就要帶一個function
# # filter(lambda parameter: expression, iterable)
# # filter 會移除判斷為 False 的項目
# ll = [1,5,3,8,2,4,6]
# res = filter(lambda x: x > 4, ll)
# print(list(res))

# ------------------------------------------
# # < map 搭配 lambda 用法 > 通常不會使用
# # 更好的寫法 : [expression for parameter in iterable]
# # map(lambda parameter: expression, iterable)
# ll = [1,5,3,8,2,4,6]
# res = map(lambda x: x**2, ll)
# print(list(res))
# # 但是通常不會使用 map
# print( [x**2 for x in ll] )
