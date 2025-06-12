from functools import lru_cache, reduce

# <lru_cache> ##########################################################
    # 會儲存之前的執行結果，重複呼叫的時候就會直接取得之前的結果
    # def lru_cache(maxsize=128, typed=False):
    # maxsize 最多cache 的個數，如果傳入 None 代表沒有限制
        # 預設 128 代表只會存 128 個結果，如果超過就會把最舊的結果刪除
    # 因此最常用的用法 : "@lru_cache(None)"
@lru_cache(None)
def test_lru_cache(n) :
    ret = n*n
    print(n,"的平方是 :", ret)
    return ret

# print("test_lru_cache : ", test_lru_cache(3))
# print("test_lru_cache : ", test_lru_cache(3)) # 第二次沒有印 function 裡面的輸出

@lru_cache(2)
def test_lru_cache_maxsize(n) : 
    ret = n*n
    print(n,"的平方是 :", ret)
    return ret

# print("test_lru_cache_maxsize : ", test_lru_cache_maxsize(3))
# print("test_lru_cache_maxsize : ", test_lru_cache_maxsize(3)) # 第二次沒有印 function 裡面的輸出
# print("test_lru_cache_maxsize : ", test_lru_cache_maxsize(4)) 
# print("test_lru_cache_maxsize : ", test_lru_cache_maxsize(5)) 
# print("test_lru_cache_maxsize : ", test_lru_cache_maxsize(3)) # 第二次"有"印 function 裡面的輸出

# <reduce> ############################################
# reduce 會逐個做, 從頭做到尾
# reduce(function, iterable[, initializer])
    # function 一定是帶兩個參數的

l = [3,7,6,4,9,1]
print("sum :",reduce(lambda n1,n2 : n1+n2, l))
print("max :",reduce(lambda n1,n2 : max(n1,n2), l))

# 使用 operator 會比較快 (可以看 speed 測試)
import operator
print("sum :",reduce(operator.add, l))
print("max :",reduce(max, l))

# 注意!! < list 相加不要用 reduce, 慢很多 >
# all_num = reduce(operator.add, grid)
