# 有時候此類型的題目可以用 Union 去解

# links 是初始的連結 [(0,1),(1,2),(2,3)]
# li 是已經歸納好的 [0可以到的點, 1可以到的點 ...]
    # link() 的結果
from collections import Counter, deque, defaultdict
from UF_copy import UF_for_cycle

# <linking> # <建立某個點連出去有哪些點>
def link(relation, len_n = -1):
    # method 1 (slow)
    li = defaultdict(list)
    # method 2
    if len_n == -1 :
        len_n = max(max(n1,n2) for n1,n2 in relation) + 1
    li = [[] for _ in range(len_n)]

    # build
    for n1,n2 in relation :
        li[n1].append(n2)
        li[n2].append(n1)
    return li

def has_cycle(links, len_n): # ?? 有問題
    li = link(links, len_n)
    seen = set()
    cir = set()
    def dfs(n, prev) :
        if n in seen :
            cir.add(n)
            return 1
        seen.add(n)
        for next_n in li[n] :
            if next_n != prev :
                ret = dfs(next_n, n)
                if ret == 1 :
                    if n in cir : # 遇到重複的位置 其他點就不要加入了
                        return 2
                    cir.add(n)
                    return 1
                elif ret == 2 :
                    return 2
        return 3
    for i in range(len_n) : 
        if i not in seen :
            dfs(i,-1)
    # 回傳所有形成環的點
    return cir
    
# print(has_cycle([(0, 1), (1, 2), (2, 0)], 3)) # 0 > 1 > 2 > 0 
# print(has_cycle([(0, 1), (1, 2), (0, 2)], 3)) # 0 > 1 > 2 > 0 
# print(has_cycle([(0, 1), (1, 2), (0, 2), (0, 3)], 4)) # 0 > 1 > 2 > 0 
# print(has_cycle([(0, 1), (2, 0)], 3)) # 0 > 1 > 0 
# print(has_cycle([(0, 1), (1, 2), (2, 0), (1, 3), (3, 0)], 4))

def check_no_cycle(edges, len_n) :
    uf = UF_for_cycle(len_n)
    for n1,n2 in edges :
        if not uf.union(n1, n2) :
            return False
    # if uf.count != 1 : # 如果要判斷是不是全部點連起來的 tree
    #     return False
    return True

# edges[i] = n1, n2, w
def Kruskal(edges, len_n) : # finding Minimum Spanning Tree
    edges.sort(key = lambda x : x[2])
    uf = UF_for_cycle(len_n)
    for n1,n2, w in edges :
        if uf.union(n1, n2) :
            if uf.count == 1 :
                return w
    return -1

# this two version speed almost the same
def cut_all_branch(links, len_n): # 驗證 tree
    deg = [0] * len_n
    li = [[] for _ in range(len_n)]
    for n1,n2 in links :
        li[n1].append(n2)
        li[n2].append(n1)
        deg[n1] += 1
        deg[n2] += 1

    end_point = [i for i, d in enumerate(deg) if d <= 1]
    # print("end_point", end_point)
    seen = set()
    while end_point:  # 拓樸排序，剪掉圖上所有樹枝
        now_n = end_point.pop()
        seen.add(now_n)
        for nei_n in li[now_n] :
            if nei_n not in seen :
                deg[nei_n] -= 1
                if deg[nei_n] == 1:
                    end_point.append(nei_n)

def cut_all_branch_set_li(links, len_n): # 驗證 tree
    li = [set() for _ in range(len_n)]
    for n1,n2 in links :
        li[n1].add(n2)
        li[n2].add(n1)
    
    end_point = [i for i, nei in enumerate(li) if len(nei) <= 1]
    while end_point :
        now_n = end_point.pop()
        for nei_n in li[now_n] :
            li[nei_n].remove(now_n)
            if len(li[nei_n]) == 1:
                end_point.append(nei_n)

def circle_path(links, len_n) : # 目前驗證一題
    li = link(links, len_n)
    path = {}
    path_no_circle = []
    path_in_circle = set()
    def dfs(now_n, prev_n) :
        if now_n in path :# form a circle
            return path[now_n]
        path[now_n] = len(path)
        min_ret = len(path)
        for next_n in li[now_n] :
            if next_n != prev_n :
                ret = dfs(next_n, now_n)
                if ret <= path[now_n] :
                    path_in_circle.add((min(now_n, next_n), max(now_n, next_n)))
                if ret > path[now_n] :
                    path_no_circle.append((now_n, next_n))
                min_ret = min(min_ret, ret)
        path[now_n] = min_ret
        return min_ret
    dfs(0,-1)
    return path_no_circle, path_in_circle

# print(circle_path([[0,1],[1,2],[2,0],[1,3]], 4))
# print(circle_path([[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]], 6))

# # 1192. Critical Connections in a Network
# https://leetcode.com/problems/critical-connections-in-a-network/description/
