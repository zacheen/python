# 2127. Maximum Employees to Be Invited to a Meeting
# https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/description

from typing import List
import functools

from collections import deque
# given ans (shrink leaf) : 129ms Beats97.10%
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        deg = [0] * n
        for f in favorite:
            deg[f] += 1  # 統計基環樹每個節點的入度

        max_depth = [1] * n
        end_point = deque(i for i, d in enumerate(deg) if d == 0)
        # print("end_point", end_point)
        while end_point:  # 拓樸排序，剪掉圖上所有樹枝
            x = end_point.popleft()
            y = favorite[x]  # x 只有一條出邊
            max_depth[y] = max_depth[x] + 1
            deg[y] -= 1
            if deg[y] == 0:
                end_point.append(y)

        max_ring_size = sum_chain_size = 0
        for i, d in enumerate(deg):
            if d == 0: continue

            # 遍歷基環上的點
            deg[i] = 0  # 將基環上的點的入度標記為 0，避免重複訪問
            ring_size = 1  # 基環長度
            x = favorite[i]
            while x != i:
                deg[x] = 0  # 將基環上的點的入度標記為 0，避免重複訪問
                ring_size += 1
                x = favorite[x]

            if ring_size == 2:  # 基環長度为 2
                sum_chain_size += max_depth[i] + max_depth[favorite[i]]  # 累積兩條最長鏈的長度
            else:
                max_ring_size = max(max_ring_size, ring_size)  # 取所有基環長度的最大值
        return max(max_ring_size, sum_chain_size)

s = Solution()
# print("ans :",s.maximumInvitations([2,2,1,2])) # 3 , [2,1,0]
# print("ans :",s.maximumInvitations([1,2,0])) # 3
# print("ans :",s.maximumInvitations([3,0,1,4,1])) # 4 , [0,3,4,1]
print("ans :",s.maximumInvitations([2,2,1,2,1,0])) # 5



