# set 其實就是 dict 但後面沒有對應的值
# #------------------------------------
# # <初始化> set
# 方法1 從list轉型
ll = [3,4,5,6]
s = set(ll)
# 方法2 使用指定項目
# s = {3,4,5,6}
print("init :",s)
# # <增加項目>
s.add(8) # 如果增加已經存在的項目不會做任何事
print("add :",s)
# # <刪除某個值>
s.remove(4)
print("remove :",s)
# # <不確定有沒有此值的刪除>
remove_item = 100
if remove_item in s:
    s.remove(remove_item)
# # try except 比較慢
# try :
#     s.remove(remove_item)
# except KeyError :
#     print("didnt have this value")
print("remove didnt sure :",s)
# # <判斷有沒有此項目>
print("in s : ", 3 in s)

# #------------------------------------
# << set 操作 >>
# # 聯集
# s1 = {1,2,3,4}
# s2 = {3,4,6,7}
# print("s1 | s2 :", s1 | s2)

