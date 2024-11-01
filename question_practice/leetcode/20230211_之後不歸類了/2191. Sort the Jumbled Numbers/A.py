# 2191. Sort the Jumbled Numbers
# https://leetcode.com/problems/sort-the-jumbled-numbers

from typing import List
import functools

# my Runtime 913ms Beats 84.24%
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        bind_list = []
        for ori_num in nums :
            map_num = 0
            for each_num in str(ori_num) :
                map_num = map_num*10 + mapping[int(each_num)]
            # print("map_num: ", map_num)
            bind_list.append([map_num, ori_num])
        # print(bind_list)
        bind_list.sort(key = lambda x : x[0])
        # print(bind_list)
        return [o for m, o in bind_list]

# given ans (slower)
# similar logic but using function
class Solution:
  def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
    def getMapped(num: int) -> int:
      mapped = []
      for c in str(num):
        mapped.append(str(mapping[ord(c) - ord('0')]))
      return int(''.join(mapped))
    A = [(getMapped(num), i, num) for i, num in enumerate(nums)]
    return [num for _, i, num in sorted(A)]

s = Solution()
print(s.sortJumbled(mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]))
print(s.sortJumbled(mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,38,338]))
print(s.sortJumbled(mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123]))



