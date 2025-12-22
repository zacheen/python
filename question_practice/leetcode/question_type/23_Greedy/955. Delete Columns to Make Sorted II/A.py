# 955. Delete Columns to Make Sorted II
# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

from typing import List
from math import inf

# my : 0ms
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        comp_range = len(strs)-1
        in_order = [False]*comp_range
        in_order_cnt = 0
        ans = 0
        for col in range(len(strs[0])) :
            new_in_order = in_order.copy()
            new_in_order_cnt = in_order_cnt
            have_to_del = False
            for front_i, in_order_flag in enumerate(in_order) :
                if in_order_flag == False :
                    front_c = strs[front_i][col]
                    later_c = strs[front_i+1][col]
                    if front_c > later_c :
                        # print(col, front_i)
                        have_to_del = True
                        break
                    elif front_c < later_c :
                        new_in_order[front_i] = True
                        new_in_order_cnt += 1
            if have_to_del :
                ans += 1
            else :
                in_order = new_in_order
                in_order_cnt = new_in_order_cnt
                if in_order_cnt == comp_range :
                    return ans
        return ans

s = Solution()
print("ans :",s.minDeletionSize(["ca","bb","ac"])) # 1
print("ans :",s.minDeletionSize(["xc","yb","za"])) # 0
print("ans :",s.minDeletionSize(["zyx","wvu","tsr"])) # 3



