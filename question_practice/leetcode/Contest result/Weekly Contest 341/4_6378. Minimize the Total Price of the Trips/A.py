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
        
        return 0

# given ans

s = Solution()
print(s.minimumTotalPrice(n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]))
print(s.minimumTotalPrice(n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]))
# print(s.minimumTotalPrice())



