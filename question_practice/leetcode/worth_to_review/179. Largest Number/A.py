# 179. Largest Number
# https://leetcode.com/problems/largest-number/description/

class CompClass(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        nums = [str(n) for n in nums]
        nums.sort(key=CompClass)
        largest_num = ''.join(nums)
        if largest_num[0] == '0' :
            return '0'
        else :
            return largest_num

s = Solution()
# print(s.largestNumber([3,34]))
# print(s.largestNumber([3,30,34,5,9]))
print(s.largestNumber([999, 991, 9, 99]))
