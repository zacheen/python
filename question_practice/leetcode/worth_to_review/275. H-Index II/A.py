# 275. H-Index II
# https://leetcode.com/problems/h-index-ii/description/

# my practice again : 0ms Beats100.00%
class Solution(object):
    def hIndex(self, citations):
        citations.reverse()
        left, right = 0, len(citations) # right 通常會超出界線(因為執行的時候不會執行到這個數字) # 但是最後 l 有可能會超出範圍
        while left < right:
            mid = (left + right) // 2
            if citations[mid] >= mid+1 : # 條件 (如果 == target 的情況 要是 False)
                # 沒通過 或 數字應該要往大的方向跑(目標沒有在 left 跟 mid 之間)
                left = mid + 1
            else:
                # 通過(包含 == target 的情況)
                right = mid 

        # 如果要回傳插入的位置
        return left

# 比賽應該用上面的方法比較快，但要先考慮 Order 不會超出時限
# given ans
# 跟上面相同的方法 但是用 Binary Search 去找那個點

s = Solution()
print(s.hIndex([0,1,3,5,6]))
print(s.hIndex([1,2,100]))



