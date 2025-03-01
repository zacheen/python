# 2359. Find Closest Node to Given Two Nodes
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/

from typing import List
from math import inf

# my opt 58ms Beats93.83%
    # slower might because I change it to array, but it can manage multiple node
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        len_n = len(edges)
        not_seen = len_n+1
        visit = [not_seen]*len_n
        now_node = [node1, node2]
        node_alive = [True, True]
        while any(node_alive) :
            meet_node = []
            for i, (node, alive) in enumerate(zip(now_node, node_alive)) :
                if alive :
                    if node != -1 and visit[node] != i :
                        if visit[node] != not_seen :
                            meet_node.append(node)
                        visit[node] = i
                        now_node[i] = edges[node]
                    else :
                        node_alive[i] = False
            if meet_node :
                return min(meet_node)
        return -1

# # given ans (mem visited) 28ms Beats98.32%
# class Solution:
#     def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
#         v1=set()
#         v2=set()
#         node1_alive = True
#         node2_alive = True
#         while node1_alive or node2_alive : 
#             if node1_alive :
#                 if node1 != -1 and node1 not in v1:
#                     if node1 in v2:
#                         if node2 in v1: # 同時進入別人走過的區域
#                             return min(node1,node2)
#                         else :
#                             return node1
#                     v1.add(node1)
#                     node1=edges[node1]
#                 else : # 走到底了 或 進入迴圈了
#                     node1_alive = False
#             if node2_alive :
#                 if node2 != -1 and node2 not in v2:
#                     if node2 in v1:
#                         return node2
#                     v2.add(node2)
#                     node2=edges[node2]
#                 else : # 走到底了 或 進入迴圈了
#                     node2_alive = False
#         return -1
    
# # given ans (visit every node)
# class Solution:
#     def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
#         n, min_dis, ans = len(edges), len(edges), -1
#         def calc_dis(x):
#             dis = [n] * n
#             d = 0
#             while x >= 0 and dis[x] == n:
#                 dis[x] = d
#                 d += 1
#                 x = edges[x]
#             return dis
#         for i, d in enumerate(map(max, zip(calc_dis(node1), calc_dis(node2)))):
#             if d < min_dis:
#                 min_dis, ans = d, i
#         return ans


# my fail : and testcase result counter my understanding
    # I thought is comparing total distance, but acutally is comparing the biggest one
# class Solution:
#     def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
#         len_n = len(edges)
#         deg = [0] * len_n
#         for n2 in edges:
#             if n2 == -1 : continue
#             deg[n2] += 1  # 統計基環樹每個節點的入度
#         end_point = [i for i, d in enumerate(deg) if d == 0]
#         mem_flag = [[False,False] for _ in range(len_n)]
#         mem_flag[node1][0] = True
#         mem_flag[node2][1] = True
#         while end_point:  # 拓樸排序，剪掉圖上所有樹枝
#             now_n = end_point.pop()
#             if all(mem_flag[now_n]) :
#                 return now_n
#             nei_n = edges[now_n]
#             if nei_n != -1 : 
#                 if mem_flag[now_n][0] : mem_flag[nei_n][0] = True
#                 if mem_flag[now_n][1] : mem_flag[nei_n][1] = True
#                 deg[nei_n] -= 1
#                 if deg[nei_n] == 0:
#                     end_point.append(nei_n)
        
#         # if contain cycles, there is only one cycle
#         target_n = []
#         cycle_len = 0
#         for i, (d, fl) in enumerate(zip(deg, mem_flag)) :
#             if d > 0 :
#                 cycle_len += 1
#                 if any(fl) :
#                     target_n.append(i)

#         # avoid at the same point
#         if len(target_n) == 1 :
#             t = target_n[0]
#             if all(mem_flag[t]) :
#                 return t
#             else :
#                 return -1
        
#         tar1 = target_n.pop()
#         now_n = tar1
#         tar2 = target_n.pop()
#         dis_cou = 0
#         while True :
#             now_n = edges[now_n]
#             dis_cou += 1
#             if now_n == tar2 :
#                 ano_cycle = cycle_len-dis_cou
#                 if ano_cycle < dis_cou :
#                     return tar1
#                 elif dis_cou < ano_cycle :
#                     return tar2
#                 else :
#                     return min(tar1, tar2)

s = Solution()
print("ans :",s.closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1)) # 2
print("ans :",s.closestMeetingNode(edges = [1,2,-1], node1 = 0, node2 = 2)) # 2
print("ans :",s.closestMeetingNode(edges = [2,2,3,0], node1 = 0, node2 = 1)) # 2
print("ans :",s.closestMeetingNode(edges = [4,3,0,5,3,-1], node1 = 4, node2 = 0)) # 4
print("ans :",s.closestMeetingNode(edges = [5,4,5,4,3,6,-1], node1 = 0, node2 = 1)) # -1 # 都走到底沒有遇見對方
print("ans :",s.closestMeetingNode(edges = [4,4,8,-1,9,8,4,4,1,1], node1 = 5, node2 = 6)) # 1
print("ans :",s.closestMeetingNode(edges = [4,4,8,-1,1,8,4,4,1,1], node1 = 5, node2 = 6)) # 1



