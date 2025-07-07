# 3594. Minimum Time to Transport All Individuals
# https://leetcode.com/problems/minimum-time-to-transport-all-individuals
    # Dijkstra + Bitmask
from typing import List
from math import inf

# given ans
class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        u = 1 << n
        # 预处理每个 time 子集的最大值
        max_time = [0] * u
        for i, t in enumerate(time):
            high_bit = 1 << i
            for mask in range(high_bit):
                max_time[high_bit | mask] = max(max_time[mask], t)

        # 预处理每个集合的大小 <= k 的非空子集
        sub_masks = [[] for _ in range(u)]
        for i in range(u):
            sub = i
            while sub:
                if sub.bit_count() <= k:
                    sub_masks[i].append(sub)
                sub = (sub - 1) & i

        dis = [[inf] * u for _ in range(m)]
        h = []

        def push(d: float, stage: int, mask: int) -> None:
            if d < dis[stage][mask]:
                dis[stage][mask] = d
                heappush(h, (d, stage, mask))

        push(0, 0, u - 1)  # 起点

        while h:
            d, stage, left = heappop(h)  # left 是剩余没有过河的人
            if left == 0:  # 所有人都过河了
                return d
            if d > dis[stage][left]:
                continue
            # 枚举 sub 这群人坐一艘船过河
            for sub in sub_masks[left]:
                cost = max_time[sub] * mul[stage]
                cur_stage = (stage + floor(cost)) % m  # 过河后的阶段
                if sub == left:  # 所有人都过河了
                    push(d + cost, cur_stage, 0)
                    continue
                # 枚举回来的人（可以是之前过河的人）
                s = (u - 1) ^ left ^ sub
                while s:
                    lb = s & -s
                    return_time = max_time[lb] * mul[cur_stage]
                    push(d + cost + return_time, (cur_stage + floor(return_time)) % m, left ^ sub ^ lb)
                    s ^= lb

        return -1

s = Solution()
print("ans :",s.minTime()) # 



