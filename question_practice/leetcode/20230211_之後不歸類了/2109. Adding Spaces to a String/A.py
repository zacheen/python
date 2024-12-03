# 

from typing import List
import functools

# my ver1 47ms Beats83.97%
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        last_indx = 0
        ans = ""
        for indx in spaces :
            ans += s[last_indx:indx] + " "
            last_indx = indx
        return ans + s[last_indx:]
    
# my ver2 35ms Beats94.46%
# I'm impress that generating another list is faster
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        last_indx = 0
        split_list = []
        for indx in spaces :
            split_list.append(s[last_indx:indx])
            last_indx = indx
        split_list.append(s[last_indx:])
        return " ".join(split_list)

# given ans

s = Solution()
print("ans :",s.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))
print("ans :",s.addSpaces(s = "icodeinpython", spaces = [1,5,7,9]))
print("ans :",s.addSpaces(s = "spacing", spaces = [0,1,2,3,4,5,6]))



