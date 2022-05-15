# my Runtime: 446 ms, faster than 97.36% of Python3
class Solution:
    def containsDuplicate(self, nums):
        mem = set()
        for n in nums :
            if n in mem :
                return True
            mem.add(n)
        return False

        # given ans
        # return len(nums) != len(set(nums)) 

s = Solution()
print(s.())



