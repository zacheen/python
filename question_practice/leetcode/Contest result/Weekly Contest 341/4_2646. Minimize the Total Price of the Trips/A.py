from typing import List
import functools
from collections import defaultdict, Counter
# my 
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        path = defaultdict(list)
        for start, dest in edges :
            path[start].append(dest)
            path[dest].append(start)
        # print(path)
        
        path_mem = set()
        # @cache
        def dfs(start, dest) :
            # print(start, path_mem)
            path_mem.add(start)
            if start == dest :
                return True
            for next_p in path[start] :
                if next_p in path_mem :
                    continue
                if dfs(next_p, dest) :
                    return True
            path_mem.remove(start)
            return False
            
        # 各個點總共會踩幾次
        count_pass = Counter()
        for start, dest in trips :
            path_mem = set()
            dfs(start, dest)
            print(start, dest, path_mem)
            count_pass += Counter(path_mem)
            print(count_pass)
        
        # 最小化總和
        total_list = []
        for p, step_times in count_pass.items() :
            if step_times != 0 :
                total_list.append((step_times*price[p], p))
        print(total_list)
        
        # 現在我已經有每個點的總和了
        # 不知道要怎麼最小化總和
        # 其實只有兩種組合?因為是相間 - 不對 因為只要不相臨就好
            # 1-2-3-4 這種情況可以減半 1,4 
            # 而不是只有 2,4 或 1,3 這兩種方法
        # 從最大的開始減半? - 不對這樣有可能減半的點數很少
        # 我覺得這就是我沒學過的演算法...
            # 跟 given ans 大概念是相同的
            # 所以我的思路是正確的，只是不知道相對應的演算法

        # 目前我想到的就是 計算每一種可能
        # 時間複雜度 2**50 = 1000**5 = 10**15 應該太久了 
        
        return 0

# given ans Beats 99.67%
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        path = defaultdict(list)
        for start, dest in edges :
            path[start].append(dest)
            path[dest].append(start)
        # print(path)
        
        previous_p = [0]*n # 紀錄從 0 分支出去的支線 前一個點是哪一個點
        dis_to_zero = [0]*n
        def dfs(x, f, dis) :
            previous_p[x] = f; dis_to_zero[x] = dis
            for v in path[x]:
                if (v == f) :
                    continue
                dfs(v, x, dis + 1)
        dfs(0, 0, 0)
        print(previous_p, dis_to_zero)
            
        # 各個點總共會踩幾次
        count_pass = [0]*n
        # 雖然一樣是 O(n) 但是有很高的機率不會遍歷每個點 而是0分出去的其中兩支分支 
        for start, dest in trips :
            if (dis_to_zero[start] > dis_to_zero[dest]) :
                start, dest = dest, start
            # 先讓距離相等
            while (dis_to_zero[start] < dis_to_zero[dest]) :
                count_pass[dest]+=1
                dest = previous_p[dest]
            # 若距離相等 但點卻不同 -> 代表此兩點在 0 分出去不同的兩個分支
            while (start != dest) :
                count_pass[start]+=1
                count_pass[dest]+=1
                start = previous_p[start] 
                dest = previous_p[dest]
            count_pass[start]+=1
        print(count_pass)
        
        # # 最小化總和
        # 這裡的方法 = 未減價的價格(ori_price) - (間隔走怎麼走會最大)/2
        ori_price = [step_times*step_price for step_price, step_times in zip(price,count_pass)]
        print(ori_price)

        # 其實之前有遇過類似的題目 但是那時候是 2D 的
        # # 優化 易讀性較好################################################
        # # 
        # # dp = [[0, 0] for _ in range(n)]
        # def dfs2(now_p, previous_p):
        #     # 現在這個 p 要選或不選
        #     # [0] 代表不選 [1]代表要選
        #     dp[now_p][0] = 0
        #     dp[now_p][1] = price[now_p]*count_pass[now_p] # 選擇此點的金額
        #     for next_p in path[now_p] :
        #         if (next_p == previous_p) :
        #             continue
        #         dfs2(next_p, now_p)
        #         dp[now_p][0] += max(dp[next_p][1], dp[next_p][0]) # 如果此點不選 那最佳解就是 看上一個點選跟不選 那個比較好
        #         dp[now_p][1] += dp[next_p][0] # 如果此點要選 那分支的每一個點都不能選
        # 優化後 ################################################
        dp = [[0, each_p_cost] for each_p_cost in ori_price]
        def dfs2(now_p, previous_p):
            # 現在這個 p 要選或不選
            # [0] 代表不選 [1]代表要選
            # dp[now_p][0] = 0
            # dp[now_p][1] = price[now_p]*count_pass[now_p] # 選擇此點的金額
            for next_p in path[now_p] :
                if (next_p == previous_p) :
                    continue
                dfs2(next_p, now_p)
                dp[now_p][0] += max(dp[next_p][1], dp[next_p][0]) # 如果此點不選 那最佳解就是 看上一個點選跟不選 那個比較好
                dp[now_p][1] += dp[next_p][0] # 如果此點要選 那分支的每一個點都不能選
        ########################################################
        dfs2(0, 0) 

        return sum(ori_price) - max(dp[0][0], dp[0][1])//2
        # price[i] is an even integer. 所以可以用 //2

s = Solution()
print(s.minimumTotalPrice(n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]))
print(s.minimumTotalPrice(n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]))
# print(s.minimumTotalPrice())



