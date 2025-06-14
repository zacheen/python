# 763. Partition Labels
# https://leetcode.com/problems/partition-labels
    # 其實跟 # 3169. Count Days Without Meetings 很像

from typing import List
from math import inf

# my 3ms Beats91.15% (better)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_i = {c:i for i,c in enumerate(s)}
        
        ans = []
        l = 0
        while l < len(s) :
            now_i = l
            r = last_i[s[now_i]]
            while now_i < r :
                new_r = max(last_i[c] for c in s[now_i+1:r+1])
                now_i = r
                if new_r > r :
                    r = new_r
            ans.append(r-l+1)
            l = r+1
        return ans
    
# my 2nd attempt (concept same) : 3ms Beats90.98%
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 某個字母最右邊的位置
        # ri_pos = {}
        # for i,c in enumerate(s):
        #     ri_pos[c] = i
        ri_pos = {c:i for i,c in enumerate(s)}

        most_r = 0
        ans = []
        while most_r < len(s) :
            last_r = most_r
            now_i = most_r
            most_r = ri_pos[s[now_i]]
            while now_i != most_r :
                now_i += 1
                most_r = max(ri_pos[s[now_i]], most_r)
            most_r += 1
            ans.append(most_r-last_r)
        return ans

s = Solution()
print("ans :",s.partitionLabels("ababcbacadefegdehijhklij")) # [9, 7, 8]
print("ans :",s.partitionLabels("eccbbbbdec")) # [10]



