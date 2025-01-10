# 406. Queue Reconstruction by Height
# https://leetcode.com/problems/queue-reconstruction-by-height/description

from typing import List
import functools

# my 2656ms Beats5.01%
class SegTree:
    def __init__(self, nums):
        self.n = len(nums)
        # init
        self.tree = [0] * 2 * self.n

    def update(self, index):
        index += self.n
        self.tree[index] += 1
        while index > 1:
            # update node
            self.tree[index>>1] = self.tree[index] + self.tree[index^1]
            index >>= 1

    def query(self, left):
        # 0 ~ right-1
        left += self.n
        right = self.n*2-1
        res = 0
        while left <= right:
            if left & 1 :
                # combine result
                res += self.tree[left]
                left += 1
            if not (right & 1) :
                # combine result
                res += self.tree[right]
                right -= 1
            left >>= 1
            right>>= 1
        return res

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # people.sort(key = lambda x : (x[1], x[0]))
        people.sort()
        # print("sort :",people)
        discrete_h = list(set(h[0] for h in people))
        discrete_h.sort()
        # print("dis :",discrete_h)
        segT = SegTree(discrete_h)
        dis_indx = {h: i for i,h in enumerate(discrete_h)}

        ans = []
        stack = []  
        for p in people :
            if segT.query(dis_indx[p[0]]) == p[1] :
                ans.append(p)
                segT.update(dis_indx[p[0]])

                while stack :
                    no_ans = True
                    for s_i, s in enumerate(stack) :
                        if segT.query(dis_indx[s[0]]) == s[1] :
                            ans.append(s)
                            del(stack[s_i])
                            segT.update(dis_indx[s[0]])
                            no_ans = False
                            break
                    if no_ans :
                        break
            else :
                stack.append(p)
        return ans

# given ans (segment tree) 48ms Beats21.84%
from math import ceil,log2,inf
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        tree = [-inf for _ in range(2**(ceil(log2(n))+1)-1)]
        def build_(treeIdx,le=0,ri=n-1):
            if le == ri:
                tree[treeIdx] = 1
            else:
                mid = le+(ri-le)//2
                tree[treeIdx] = build_(2*treeIdx+1,le,mid) + build_(2*treeIdx+2,mid+1,ri)
            return tree[treeIdx]
        def update_(idx,val,treeIdx=0,le=0,ri=n-1):
            if le<=idx<=ri:
                if le==ri:
                    tree[treeIdx] = val
                else: # le!=ri
                    mid = le+(ri-le)//2
                    update_(idx,val,2*treeIdx+1,le,mid)
                    update_(idx,val,2*treeIdx+2,mid+1,ri)
                    tree[treeIdx] = tree[2*treeIdx+1]+tree[2*treeIdx+2]
        def query_(k,treeIdx=0,le=0,ri=n-1):
            if le==ri:
                return le
            mid = le+(ri-le)//2
            if k<= tree[2*treeIdx+1]:
                return query_(k,2*treeIdx+1,le,mid)
            else: # k > tree[2*treeIdx+1]
                return query_(k-tree[2*treeIdx+1],2*treeIdx+2,mid+1,ri)
        res = [None for _ in range(n)]
        build_(0)
        for p in sorted(people,key=lambda x : (x[0],-x[1])):
            idx = query_(p[1]+1)
            res[idx] = p
            update_(idx,0)
        return res

# # given ans (best solution)
# class Solution:
#     def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
#         ans = []
#         people.sort(key=lambda x: (-x[0], x[1]))
#         for p in people:
#             ans.insert(p[1], p)
#             # print(ans)
#         return ans

s = Solution()
print("ans :",s.reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
# [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# print("ans :",s.reconstructQueue(people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))
# # [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
# # print("ans :",s.reconstructQueue())



