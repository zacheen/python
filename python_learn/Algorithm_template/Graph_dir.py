# links 是初始的連結 [(0,1),(1,2),(2,3)]
# li 是已經歸納好的 [0可以到的點, 1可以到的點 ...]
    # link() 的結果
from collections import Counter, deque, defaultdict

# <linking> # <建立某個點連出去有哪些點>
def link(relation, len_n = -1):
    # method 1
    li = defaultdict(list)
    # method 2
    if len_n == -1 :
        len_n = max(max(n1,n2) for n1,n2 in relation) + 1
    li = [[] for _ in range(len_n)]

    # build
    for n1,n2 in relation :
        li[n1].append(n2)
    return li

# <find_top> # <找到每個出發點> (此點沒有點會進來)
def find_top(links, len_n):
    seen_set = set(n2 for n1,n2 in links)
    return set([i for i in range(len_n)]) - seen_set
# print( find_top([(n1,n2) for n1,n2, in enumerate([2,2,1,2,1,0])], 6) )

# # 如果 find_top 沒有結果 : 代表一定有環 但不能找到全部有環的結果
# print(find_top([[1,2],[2,3],[3,1],[1,0]], 4)) # 如果沒有頂點 代表一定有環
# print(find_top([[1,2],[2,3],[3,1],[0,1]], 4)) # 有環但是回傳 False


# <find_end> # <找到每個結束點> (此點出不去其他點) ??
# def find_end(links, len_n):

# <三色標記法>
    # 0 : 沒有走過
    # 1 : 正在走
    # 2 : 走過了
def has_cycle(li, len_n):
    color = [0] * len_n
    def dfs(x):
        if color[x] == 2 :
            return False
        color[x] = 1
        for next_n in li[x]:
            if color[next_n] == 1 or dfs(next_n):
                return True
        color[x] = 2
        return False
    return any(dfs(n) for n in range(len_n))

# still don't know which one is faster ??
def has_cycle(li, len_n):
    color = [0] * len_n
    def dfs(x):
        color[x] = 1
        for next_n in li[x]:
            if color[next_n] == 1 or (color[next_n] == 0 and dfs(next_n)):
                return True
        color[x] = 2
        return False
    return any(dfs(n) for n,c in enumerate(color) if c == 0)
    
# print(has_cycle([(0, 1), (1, 2), (2, 0)], 3)) # 0 > 1 > 2 > 0 
# print(has_cycle([(0, 1), (1, 2), (0, 2)], 3))
# print(has_cycle([(0, 1), (1, 0), (2, 0)], 3)) # 0 > 1 > 0 

# <cut all branch - remain only cycle>
def cut_all_branch(links, len_n):
    deg = [0] * len_n
    for n1,n2 in links:
        deg[n2] += 1  # 統計基環樹每個節點的入度
    li = link(links, len_n)
    end_point = [i for i, d in enumerate(deg) if d == 0]
    while end_point:  # 拓樸排序，剪掉圖上所有樹枝
        now_n = end_point.pop()
        for nei_n in li[now_n] :
            deg[nei_n] -= 1
            if deg[nei_n] == 0:
                end_point.append(nei_n)

    # return cycle (回傳全部形成 cycle 的點)
    return [i for i, l in enumerate(deg) if l > 0]

# 從 cut_all_branch 改編而來
    # 回傳 cycle 點上如果有 branch, 這個 branch 的最長長度
def all_branch_len(links, len_n):
    deg = [0] * len_n
    for n1,n2 in links:
        deg[n2] += 1  # 統計基環樹每個節點的入度
    li = link(links, len_n)
    max_depth = [-1] * len_n
    end_point = [i for i, d in enumerate(deg) if d == 0]
    # print("end_point", end_point)
    while end_point:  # 拓樸排序，剪掉圖上所有樹枝
        now_n = end_point.pop()
        for nei_n in li[now_n] :
            if max_depth[now_n] == -1 :
                max_depth[now_n] = 1
            max_depth[nei_n] = max_depth[now_n] + 1
            deg[nei_n] -= 1
            if deg[nei_n] == 0:
                end_point.append(nei_n)

    # return len (回傳這個點上到 leaf 的距離(包含自己))
        # -1 代表沒有 branch 在此點上
    return max_depth

# print(cut_all_branch([(0, 1), (1, 2), (2, 0)], 3))
# print(cut_all_branch([(0, 1), (1, 0), (2, 1), (3, 2)], 4))
# print(cut_all_branch([(0, 1), (1, 2), (2, 0), (1, 3), (3, 0)], 4))

