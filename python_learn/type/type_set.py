# set 其實就是 dict 但後面沒有對應的值
# #------------------------------------
# # <初始化> set
# 方法1 從list轉型
ll = [3,6,5,4,201,202,203]
s = set(ll)
# 方法2 使用指定項目
# s = {3,4,5,6}
print("init :",s)
# # <增加項目>
s.add(8) # 如果增加已經存在的項目不會做任何事
print("add :",s)
# # <刪除某個值 (不存在會跳錯) >
s.remove(4)
print("remove :",s)
# # <刪除某個值 (不存在不會跳錯) >
s.discard(100)
print("discard:",s)
# # <隨機取出某個值 (set為空會跳錯) >
print("before pop:",s)
print("pop out :",s.pop())
print("before pop:",s)
# # <判斷有沒有此項目>
print("in s :", 3 in s)
# # <sorted> set 也可以 sort 變成 list
print("sort_set :", sorted(s, key=lambda x:-x))

# #------------------------------------
# << set operator >>
# <and or>
s1 = {1,2,3,4}
s2 = {3,4,6,7}
print("s1 | s2 :", s1 | s2)
print("s1 & s2 :", s1 & s2)
# <大於等於 '>='>
# 包含另一個全部的項目
s1 = {1,2,3,4}
s2 = {3,4,6,7}
print("s1 >= s2 :", s1 >= s2) # False
s1 = {1,3,4}
s2 = {3,4}
print("s1 >= s2 :", s1 >= s2) # True
s1 = {3,4}
s2 = {3,4}
print("s1 >= s2 :", s1 >= s2) # True
# <大於 '>'>
# 等同大於等於'>=' 但是得要多一個項目
print("s1 > s2 :", s1 > s2) # False

