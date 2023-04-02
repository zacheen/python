# my 
from collections import Counter
from typing import List
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
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

s = Solution()
print(s.findMatrix([1,3,4,1,2,3,1]))
print(s.findMatrix([1,2,3,4]))



