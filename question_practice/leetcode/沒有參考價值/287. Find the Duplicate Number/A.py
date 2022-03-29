# My Runtime: 784 ms, faster than 63.78% of Python3
# class Solution:
#     def findDuplicate(self, nums):
#         seen_set = set()
#         for each_num in nums :
#             if each_num not in seen_set :
#                 seen_set.add(each_num)
#             else :
#                 return each_num

# My 如果範圍是有限制的應該是 list 比較快
# Runtime: 580 ms, faster than 99.89% of Python3
class Solution:
    def findDuplicate(self, nums):
        seen_set = [False]*(len(nums)+2)
        for each_num in nums :
            if seen_set[each_num] :
                return each_num
            else :
                seen_set[each_num] = True

s = Solution()
print(s.findDuplicate(nums = [1,3,4,2,2]))

