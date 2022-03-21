# << bin 運算元 >>  (其實就是 int 的 operator)
# &	AND
# |	OR
# ^	XOR
# ~	取2補數
# << 	左移
# >> 	右移

# # 其實就是用數字儲存
# b = 0b0110
# print(type(b))

# # # << 轉型 >>
# # # <int 轉 str> <為了好看印出來>
# # 0b數值 == bin() == 2進位制
# print("bin :",bin(17))
# # 0o數值 == oct() == 8進位制
# print("oct :",oct(17))
# # 0x數值 == hex() == 16進位制
# print("hex :",hex(17))

# # # <str 轉 int> <從bin字串轉回來>
# # 0b數值 == bin() == 2進位制
# print("bin :",int("0b10001",2))
# print("bin :",int("10001",2))
# # 0o數值 == oct() == 8進位制
# print("oct :",int("0o21",8))
# # 0x數值 == hex() == 16進位制
# print("hex :",int("0x11", 16))

# # # <int 轉 int> <不同進制之間互相轉換>
# # 0b數值 == bin() == 2進位制
# print("bin :",int(0b10001))
# # 0o數值 == oct() == 8進位制
# print("oct :",int(0o21))
# # 0x數值 == hex() == 16進位制
# print("hex :",int(0x11))

# # << 運算元 展示 運算結果 >>
# # shift 移位
# print("shift :",bin(0b1010 << 2))  # 往前移兩位  == *4
# print("shift :",bin(0b1010 >> 1))  # 往前移兩位  == *4