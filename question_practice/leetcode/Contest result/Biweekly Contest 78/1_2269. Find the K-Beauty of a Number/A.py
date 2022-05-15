# my 
class Solution:
    def divisorSubstrings(self, num: int, k: int):
        num_str = str(num)
        ans = 0
        for i in range(len(num_str)-k+1):
            n = int(num_str[i:i+k])
            if n != 0 and (num%n == 0) :
                ans += 1
        return ans

# given ans 概念差不多

s = Solution()
print(s.())



