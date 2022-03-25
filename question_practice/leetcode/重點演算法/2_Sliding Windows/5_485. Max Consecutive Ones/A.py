# my Runtime: 380 ms, faster than 77.94% of Python3
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        now_len = 0
        max_len = 0
        for each_num in nums :
            if each_num :
                now_len += 1
                # max_len = max(max_len, now_len) # 如果 1 少放這裡
            else :
                max_len = max(max_len, now_len) # 如果 0 少放這裡  但最後要多做一次
                now_len = 0
        # max_len = max(max_len, now_len) <- 多做一次   
        return max_len

s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))

