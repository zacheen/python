import sys

i = 1
print(sys.getsizeof(i))
i = 1010101
print(sys.getsizeof(i))
i = 1073741824
print(sys.getsizeof(i))
i = 1073741823
print(sys.getsizeof(i))
# 但是沒有辦法指定使用 int32 或 int16 python 會自動轉換
