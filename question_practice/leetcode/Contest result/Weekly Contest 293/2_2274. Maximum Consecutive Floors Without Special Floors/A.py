# my 
class Solution:
    def maxConsecutive(self, bottom, top, special):
        special.sort()
        
        # given ans 把尾端的top - bottom + 1在這裡當初使值順便處理掉
        max_floor = 0
        
        for s in special :
            max_floor = max(max_floor, s-bottom)
            bottom = s + 1
            
        return max(max_floor , top - bottom + 1)

# given ans
class Solution:
    def maxConsecutive(self, bottom, top, special):
        special.sort()
        
        # 把頭尾當初使值順便處理掉
        max_floor = max(special[0] - bottom, top - special[-1])
        last = special[0]
        for s in special[1:] :
            max_floor = max(max_floor, s-last-1)
            last = s
        return max_floor

s = Solution()
print(s.maxConsecutive())



