# asterisk 星號用法

# -- 乘法 ----------------------
print("4*7",4*7)

# -- 次方 ----------------------
print("4**7",4**7)

# -- 解包 ----------------------
def func_3(a, b, c):
    return a + b + c

l = [1, 2, 5]
print(func_3(*l))

# # 錯誤數量會跳錯
# l = [1, 2, 5, 8]
# print(func_3(*l))

# -- 任意數量參數 ----------------------
def func_any_p(*p):
    for n in p :
        print(n, end=", ")
    print()

func_any_p(1, 3, 7, 4, 5)

# -- 任意帶名稱參數 ----------------------
def func_any_p(**p):
    for k, n in p.items() :
        print(k, n, end=", ")
    print()
func_any_p(x=1, y=3, z=7)