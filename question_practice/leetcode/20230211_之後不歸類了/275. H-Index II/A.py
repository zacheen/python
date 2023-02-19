# my 
class Solution(object):
    def hIndex(self, citations):
        citations.reverse()
        for indx, num in enumerate(citations):
            if (indx + 1) > num :
                return int(indx)
        return len(citations)

# 比賽應該用上面的方法比較快，但要先考慮 Order 不會超出時限
# given ans
# 跟上面相同的方法 但是用 Binary Search 去找那個點

s = Solution()
print(s.hIndex([0,1,3,5,6]))
print(s.hIndex([1,2,100]))



