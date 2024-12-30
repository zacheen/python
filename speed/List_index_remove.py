# 結論 
# del vs pop : del好像快一點
# 取第幾個項目的值 是 O(1)  (速度會不一樣應該是誤差)
# 不管是刪除或新增 愈後面的項目愈快 O(n)

import time

# # del vs pop ######################################################
# # 前
# # pop
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     ll.pop(0)
# end = time.time()
# print("pop 前 :",end - start) # 7.736309051513672
# # del
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     del(ll[0])
# end = time.time()
# print("del 前 :",end - start) # 8.08120846748352

# # 中
# # pop
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     ll.pop(len(ll)//2)
# end = time.time()
# print("pop 中 :",end - start) # 3.849705696105957
# # del
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     del(ll[len(ll)//2])
# end = time.time()
# print("del 中 :",end - start) # 4.04122519493103

# # 後
# # pop
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     ll.pop(len(ll)-1)
# end = time.time()
# print("pop :",end - start) # 0.000997781753540039
# # del
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     del(ll[len(ll)-1])
# end = time.time()
# print("del :",end - start) # 0.000997304916381836


# ######################################################
# ll = list(range(10000000))
# ret = ll[0]
# ret = ll[9000]

# # 不知道為什麼第一次比較慢
#     # 所以第一個 for 迴圈是為了抵銷誤差
# # 取第一個的值
# start = time.time()
# for i in range(1000000) : 
#     ret = ll[0]
# end = time.time()
# print(end - start)

# # 取第一個的值
# del_place = 0
# start = time.time()
# for i in range(100000000) : 
#     ret = ll[del_place]
# end = time.time()
# print("取第一個的值 :",end - start) # 7.620257377624512

# # 取中間的值
# del_place = 9000
# start = time.time()
# for i in range(100000000) : 
#     ret = ll[del_place]
# end = time.time()
# print("取中間的值 :",end - start)  # 7.435962915420532

# # 取後面的值
# del_place = 9999999
# start = time.time()
# for i in range(100000000) : 
#     ret = ll[del_place]
# end = time.time()
# print("取後面的值 :",end - start)  # 7.382392883300781

#-------------------------------------------------
# # str 版本測試  速度跟list差不多
# # 取第一個的值
# ll = "1"*10000000
# del_place = 0
# start = time.time()
# for i in range(100000000) : 
#     ret = ll[del_place]
# end = time.time()
# print("取第一個的值 :",end - start) # 7.620257377624512

# # 取中間的值
# del_place = 9000
# start = time.time()
# for i in range(100000000) : 
#     ret = ll[del_place]
# end = time.time()
# print("取中間的值 :",end - start)  # 7.435962915420532

# # 取後面的值
# del_place = 9999999
# start = time.time()
# for i in range(100000000) : 
#     ret = ll[del_place]
# end = time.time()
# print("取後面的值 :",end - start)  # 7.382392883300781

#--- 刪除項目 ----------------------------------------------
# # 刪除第一個的值
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     del(ll[0])
# end = time.time()
# print("刪除第一個的值 :",end - start) # 6.500624418258667

# # 刪除中間的值
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     del(ll[9000])
# end = time.time()
# print("刪除中間的值 :",end - start) # 6.4689719676971436

# # pop
# ll = list(range(10000000))
# start = time.time()
# for i in range(100000) : 
#     ll.pop()
# end = time.time()
# print("pop :",end - start)

# # del(ll[-1])
# ll = list(range(10000000))
# start = time.time()
# for i in range(100000) : 
#     del(ll[-1])
# end = time.time()
# print("del(ll[-1]) :",end - start)

# # del(ll[-2])
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     del(ll[-2])
# end = time.time()
# print("del(ll[-11000]) :",end - start)

# # del(ll[-1000000])
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     del(ll[-1000000])
# end = time.time()
# print("del(ll[-1000000]) :",end - start)

# # del(ll[9000000]) 位置等同 del(ll[-1000000]) 
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     del(ll[9000000])
# end = time.time()
# print("del(ll[9000000]) :",end - start)

# # del(ll[900000]) 
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     del(ll[900000])
# end = time.time()
# print("del(ll[900000])  :",end - start)

# # ll.pop(900000)
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     ll.pop(900000)
# end = time.time()
# print("ll.pop(900000)  :",end - start)

# #-- 增加項目 -----------------------------------------------
# # 前端
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     ll.insert(0, 0) 
# end = time.time()
# print("增加第一個的值 :",end - start) # 7.313439846038818

# # 增加中間的值
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     ll.insert(9000, 0)
# end = time.time()
# print("增加中間的值 :",end - start) # 7.240641117095947

# # 增加尾端的值 append 
# ll = list(range(10000000))
# start = time.time()
# for i in range(100000) : 
#     ll.append(0)
# end = time.time()
# print("append :",end - start) # 0.0079803466796875

# # 增加尾端的值 insert -1
# ll = list(range(10000000))
# start = time.time()
# for i in range(100000) : 
#     ll.insert(-1, 0) 
# end = time.time()
# print("insert -1 :",end - start) # 0.017952919006347656

# # insert(-1000000, 0) 位置等同  insert(900000, 0)
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     ll.insert(-1000000, 0) 
# end = time.time()
# print("insert(-1000000, 0) :",end - start) # 0.6123635768890381

# # insert(9000000, 0)
# ll = list(range(10000000))
# start = time.time()
# for i in range(1000) : 
#     ll.insert(9000000, 0)
# end = time.time()
# print("insert(9000000, 0)  :",end - start) # 0.6073763370513916
