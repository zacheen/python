import numpy as np
import math
# # ------------------------------------
# # 初始化 方法1 全部都是0
# array = np.zeros( shape = (3, 5) , dtype=int ) 
#     # shape = (column, row)
#     # dtype : float int
# print(array)
# # 初始化 方法2 類似range
# array = np.arange(12, dtype=int)
#     # np.arange(start = 3,stop = 10, step = 2, dtype=int)
# print("original :",array)
# # 初始化 方法3 list 轉型
# array = np.array([[1,3,2],[8,5,7]])
# print(array)
# # 初始化 方法4 隨機
# array = np.random.rand(3,4) # 隨機產生 0~1 之間的數字 大小為 3*4
array = np.random.randint(1,11,(3,4)) # 隨機產生 1~10(不包含11) 之間的數字 大小為 3*4
array = array.astype("float16") # 有時候會需要 float 才能計算
# numpy.random.randint(low, high=None, size=None, dtype='l')
# # 初始化 方法5 讀取 byte 檔
# array = np.fromfile(XX, dtype=np.float32, count=-1, offset=0)
print(array)

# # 初始值
# array.fill(100)
# print(array)

# < 可察看的屬性 >
# 查看形狀
# print(array.shape)
# # 查看有幾個維度
# print(array.ndim)
# # 查看是什麼型態
# print(array.dtype)
# # 不要省略中間項目 or 印出完整資料
# 取消印出長度限制
np.set_printoptions(threshold=np.inf)

# # # << 自己的數值格式 >> 
# # 基本上 np.XX 的數值都只有 float 可以用
# val_float = np.zeros( 1, dtype=float ) 
# # np.nan 空值
# val_float[0] = np.nan
# print("nan :",val_float)
# val_float[0] = None
# print("None :",val_float)
# # 無限大
# val_float[0] = np.inf
# print("np.inf :",val_float)
# # 無限小
# val_float[0] = -np.inf
# print("-np.inf :",val_float)
# val_float[0] = np.NINF
# print("-np.inf :",val_float)

# # 複製 copy clone
# print("copy np :",array.copy())

# # 轉換型態、改變型態 (轉型) 
# # 但是 大轉小會出問題 EX int32 轉 int16
# new_array = array.astype("float16")
# print("float16 :",new_array)

# # 找出最大值
# # 方法 1
# print("max 1 :",np.max(array))
# # 方法 2
# print("max 2 :",array.max())
# # 如果是要對個別 dimention 取最大值，就要帶入參數
# print(array.max(1))
# # 找出最小值
# print("max :",np.min(array))
# # 找最大值的位置 比較快的方法
# print("max pos :", np.unravel_index(np.argmax(array),array.shape))
# # 找出某個項目的位置
# print("where :",np.where(array==8))
# where 的其他應用 : 更改指定數值成另一個數值
# pass_arr = np.array([np.inf, -np.inf, math.inf, -math.inf])
# print( np.where( pass_arr == np.inf, np.nan, pass_arr) )
# # 排序 
# print("sort :\n",np.sort(array))
# # 總和
# print("sum  :",np.sum(array))
# # 每個項目增加某個數字
# print("add  :",array + 5)
# # 平均 
# print("mean :",np.mean(array))
# # 平均 (nan 的值會去掉 )
# array[0] = np.nan
# print("mean :",np.nanmean(array))
# # 計算各個項目各有幾個
# unique_item, counts = np.unique(array, return_counts=True)
# print(dict(zip(unique_item, counts)))
# # 計算符合條件的項目有幾個
# condition_count = np.sum(array > 5)
# print(condition_count)

# # < 組合兩個 array >
# array2 = array*2
# # < 水平組合 >
# # 方法1 : (較通用)
# array_concat = np.concatenate((array,array2), axis = 1)
# print("horizon 1 :\n",array_concat)
# # 方法2 :
# # array_concat = np.hstack((array,array2))
# # print("horizon 2 :\n",array_concat)
# # < 垂直組合 >
# # 方法1 : (較通用)
# array_concat = np.concatenate((array,array2), axis = 0)
# print("vertical 1 :\n",array_concat)
# # 方法2 :
# # array_concat = np.vstack((array,array2))
# # print("vertical 2 :\n",array_concat)

# << 對每個項目做運算 >>

# # boolean 運算
# # logical_and logical_or logical_xor ...
# mid_value = np.logical_and(array > 2, array < 7)
# print(mid_value)

# # + - * / 都可以直接做
# # 這樣是把其他的值都改成0
# print(mid_value * array)

# # 取對數 log
# # log 預設的底數是 e 
# print("log :\n",np.log(array))
# ret = np.log(np.array([0,1,math.e,10,math.e**2]))
# print("log 特殊數字 :",ret)


#  << 維度相關 >> ####################################################
# # < 變成一維 > 
# print("flatten :",array.flatten())

# # < 把 shape 中 各個維度(dim)的 channel 長度為 1 的刪除 >
# array = np.array([[5,3,2,1,4,8,6,7,9]])
# print(array.shape)
# array_squ = array.squeeze()
# print(array_squ.shape)

# # < 重新調整 dimension 大小 : reshape >
# print("reshape :\n",array.reshape(2,6))
# # 如果用 -1 ，np 會自動計算 -1 的值可以是多少
# print("reshape :\n",array.reshape(2,-1))
# # 注意 reshape 會公用記憶體 !!
# test_reshape_1 = array.copy()
# test_reshape_2 = test_reshape_1.reshape(2,6)
# print("before : \n", 
# "test_reshape_1 :\n", test_reshape_1, "\n",
# "test_reshape_2 :\n", test_reshape_2)
# test_reshape_1[0,0] = 100 # test_reshape_1 跟 test_reshape_2 都會修改
# print("before : \n", 
# "test_reshape_1 :\n", test_reshape_1, "\n",
# "test_reshape_2 :\n", test_reshape_2)

# # < 重新調整 dimension 大小 : resize >
# # 其實跟 reshape 很像，只是如果大小不符會補重複的資料或刪除資料
# print("resize(2,6) :\n",np.resize(array,(2,6)))
# print("resize(2,5) :\n",np.resize(array,(2,5)))
# print("resize(2,7) :\n",np.resize(array,(2,7)))

# # << 轉型 >> ####################################################
# # < 轉 int >
# # 有時候 np 印出來是單個數值，但其實 type 是 np 的 type
# ten = np.array(10)
# print(ten)
# print(type(ten))
# ten = int(ten)
# print(ten)
# print(type(ten))

# # < 轉 list >
# print(array.tolist())

# # << 一維專用 (=List) >> < 通常用 List 還是會比較快 > ####################################################
# # 合併
# one_dim = np.array([1,2,3], dtype=int)
# one_dim = np.append(one_dim+10, [1,2])
# print("append :",one_dim)

# # << 較不常用到 >> ####################################################
# # < 百分位數 percentile >
#     # 求數列中 第 X%分位 的數值
# # 不管前面的 list 丟進去有沒有按照順序 都沒差
# # 101 個點 , 共有 100 個區間 
# print(np.percentile(range(101),90))
# print(np.percentile(range(100,201),90))   # 不管前面的 list 丟進去有沒有按照順序 都沒差 1
# print(np.percentile(range(200,99,-1),90)) # 不管前面的 list 丟進去有沒有按照順序 都沒差 1
# print("([1,2,3,4],25) :",np.percentile([1,2,3,4],25))
# print("([1,2,2,4],50) :",np.percentile([1,2,2,4],50))
# print("([1,2,2,4],40) :",np.percentile([1,2,2,4],40))
# print("([4,2,2,4],50) :",np.percentile([4,2,2,4],50))  # 不管前面的 list 丟進去有沒有按照順序 都沒差 2
# print("([2,2,4,4],50) :",np.percentile([2,2,4,4],50))  # 不管前面的 list 丟進去有沒有按照順序 都沒差 2
# print("([2,4],50) :",np.percentile([2,4],50))

# # < 是否為純量 scalar >
# # isscalar
# # 不具方向性的物理量
# print("isscalar(1) :",np.isscalar(1))  # True
# print("isscalar([1,3,4,5]) :",np.isscalar([1,3,4,5])) # False
# print("isscalar([1]) :",np.isscalar([1])) # False
# print("isscalar(1.5) :",np.isscalar(1.5)) # True
# print("isscalar(-1) :",np.isscalar(-1)) # True

# # < 限制資料的大小 > 
# # clip
# # 如果大/小於規定的數字 則會變成規定的數字
# # boundary 的 值都會保留
# ll = np.array([5,3,2,1,4,8,6,7,9])
# print("bef clip :",ll)              # [5 3 2 1 4 8 6 7 9]
# print("aft clip :",np.clip(ll,3,7)) # [5 3 3 3 4 7 6 7 7]

# # < 初始化一個大小、型態一樣大小 全部數字都為零的空間 > 
# # zeros_like
# print(np.zeros_like(array))

# # < 擴張 array 的維度 > 
#     # EX: (3, 4) -> (1, 3, 4) 或 (3, 1, 4) ... 反正就是插入一個 1 進來
# # expand_dims
# print(array.shape)
# expand_dim_array = np.expand_dims(array, axis = 0)
# print(expand_dim_array.shape)
# print(expand_dim_array)

# # # << 注意事項 >> ####################################################
# # # numpy 的 type 一定要是數字
# # import math
# # array.fill(math.inf)
# # print(array)

# # # 裡面不能存 List
# # array = np.zeros( shape = (1, 1) , dtype=list ) # 結果跟dtype=int一樣
# # print(array)
