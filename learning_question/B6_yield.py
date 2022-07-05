# # 創建 generator -------------------------------------
# # < 使用 () 跟 for >
# powers = (x**2 for x in range(10))
# # print(powers)  # 注意 是generator
# # print(powers[3]) # generator 不能直接取用
# for x in powers:
#     print(x)

# # < 使用 function 跟 yield >
# def yield_test(n):
#     print("start n =", n)  # 並不會重複執行
#     for i in range(n):
#         print("i =", i)
#         yield i*i  
#         # 可以想成 每次執行到yield 就會回傳結果 
#         # 下次呼叫就會再從 yield 繼續執行

#         # return # 可以嘗試把註解打開
#         # 執行到return 就代表到尾端 結束for
#     print("end")  # 注意是印完 "--------" 才印這個

# for test in yield_test(3):
#     print("i*i =", test)
#     print("--------")

# #  -------------------------------------
# # next : 可以單獨呼叫 generator
# # send : 會把值傳入 function 中，再繼續做，直到回傳 yield
# def test():
#     print("start i = 0")
#     for i in range(3):
#         throw = yield i
#         print("throw:", throw)

# p = test()
# print("next(p) :",next(p))
# print("-----------")
# print("p.__next__() :",p.__next__())
# print("-----------")
# print("p.send(7) :",p.send(7))
# print("-----------")
# # # 如果沒有下一個 會丟出 StopIteration 的 Error
# # print("next(p) :",next(p))
# # print("-----------")