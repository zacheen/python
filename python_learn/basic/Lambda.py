# Lambda
# 語法 : 
# 基本用法
    # lambda parameter_list: expression
# filter 用法
    # filter(lambda parameter: expression, iterable)

# # 基本用法 Example
# # 是不是從頭跟從尾念過來都一樣
# isPalindrome = lambda s : s == s[::-1] 
# print(isPalindrome("aba"))
# print(isPalindrome("abab"))

# filter 搭配 lambda 用法 Example
ll = [1,5,3,8,2,4,6]
res = filter(lambda x: x > 4, ll)
print(list(res))

