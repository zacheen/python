# my 
from collections import Counter
from typing import List
class Solution:
    def findMatrix(self, nums):
        cou = Counter(nums)
        ans = []
        while len(cou.keys()) != 0 :
            arr = []
            remove_item = []
            for k, num in cou.items() :
                arr.append(k)
                if num == 1 :
                    remove_item.append(k)
                else :
                    cou[k] -= 1
            ans.append(arr)
            for k in remove_item :
                del(cou[k])
        return ans

# given ans 
# 因為 1 <= nums[i] <= nums.length 
    # 所以其實我可以不用 Counter，可以用 list[num] 來計數

s = Solution()
print(s.findMatrix([1,3,4,1,2,3,1]))
print(s.findMatrix([1,2,3,4]))



