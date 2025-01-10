# SegTree 比 Fenwick trees 應用範圍更廣(但也花更多空間儲存)
# self.tree[1] 存的是所有範圍的結果(可以直接取值)
import random

# # template ##############################################################
# class SegTree:
#     def __init__(self, nums):
#         self.n = len(nums)
#         # init
#         self.tree = [INITNUM] * 2 * self.n
#         for i,n in zip(range(self.n, 2 * self.n) , nums):
#             self.tree[i] = n
#         for i in range(self.n-1, 0, -1):
#             # execute def
#             self.tree[i] = 
#                 self.tree[2*i], self.tree[2*i+1]

#     def update(self, index, val):
#         index += self.n
#         self.tree[index] = val
#         while index > 1:
#             # update node
#             self.tree[index>>1] = 
#                 self.tree[index], self.tree[index^1]
#             index >>= 1

#     def query(self, left, right):
#         # include
#         left += self.n
#         right += self.n
#         # not include
#         left += self.n+1
#         right += self.n-1
#         l_res = INITNUM
#         r_res = INITNUM
#         while left <= right:
#             if left & 1 :
#                 # combine result
#                 l_res = l_res, self.tree[left]
#                 left += 1
#             if not (right & 1) :
#                 # combine result
#                 r_res = self.tree[right], r_res
#                 right -= 1
#             left >>= 1
#             right>>= 1
#         return l_res, r_res
# # template end ##############################################################

class SegTree_Sum:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * 2 * self.n
        for i,n in zip(range(self.n, 2 * self.n) , nums):
            self.tree[i] = n
        for i in range(self.n-1, 0, -1):
            # print("mem :",i,2*i,2*i+1, self.tree[2*i],self.tree[2*i+1])
            # print(self.tree)
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, index, val):
        index += self.n
        self.tree[index] = val
        while index > 1:
            # index如果是右 index^1就是對應左邊
            self.tree[index>>1] = self.tree[index] + self.tree[index^1]
            index >>= 1 # index //= 2

    def query(self, left, right):
        left += self.n
        right += self.n
        res = 0
        # binary search
        while left <= right:
            if left & 1 :
                # if left odd:
                res += self.tree[left]
                left += 1
            if not (right & 1) :
                # if right even
                res += self.tree[right]
                right -= 1
            left >>= 1  # left //= 2
            right >>= 1 # right //= 2
        return res
    
# ll = list(range(10))
# random.shuffle(ll)
# print(ll)

# # 偶數個
# ll = [0, 2, 9, 3, 4, 7, 5, 6, 1, 8]
# segTree_Sum = SegTree_Sum(ll)
# print(segTree_Sum.query(3,5), ll[3:6])
# print(segTree_Sum.query(3,6), ll[3:7])
# print(segTree_Sum.query(4,6), ll[4:7])
# print(segTree_Sum.query(2,7), ll[2:8])

# # 奇數個
# ll = [2, 9, 3, 4, 7, 5, 6, 1, 8]
# segTree_Sum = SegTree_Sum(ll)
# print(segTree_Sum.sumRange(3,5), ll[3:6])
# print(segTree_Sum.sumRange(3,6), ll[3:7])
# print(segTree_Sum.sumRange(4,6), ll[4:7])
# print(segTree_Sum.sumRange(2,7), ll[2:8])

# for _ in range(50) :
#     ### rand list ##########
#     ll = list(range(20))
#     random.shuffle(ll)
#     s = random.randint(0, len(ll)-1)
#     segTree = SegTree_Sum(ll)
#     ### rand list end ##########

#     while True :
#         e = random.randint(0, len(ll)-1)
#         if e >= s :
#             break
#     res = segTree.query(s,e)
#     ans = sum(ll[s:e+1])
#     print("check :", s, e, res, res == ans)


from math import inf
class SegTree_Max:
    def __init__(self, nums):
        self.n = len(nums)
        # init
        self.tree = [-inf] * 2 * self.n
        for i in range(self.n):
            self.tree[i + self.n] = nums[i]
        for i in range(self.n-1, 0, -1):
            # execute def
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])

    def update(self, index, val):
        index += self.n
        self.tree[index] = val
        while index > 1:
            # update node
            self.tree[index>>1] = max(self.tree[index], self.tree[index^1])
            index >>= 1

    def query(self, left, right):
        left += self.n
        right += self.n
        res = -inf
        while left <= right:
            if left & 1 :
                # combine result
                res = max(res, self.tree[left])
                left += 1
            if not (right & 1) :
                # combine result
                res = max(res, self.tree[right])
                right -= 1
            left >>= 1
            right>>= 1
        return res
    
# ll = list(range(20))
# random.shuffle(ll)
ll = [16, 15, 8, 4, 18, 0, 11, 3, 14, 12, 9, 19, 7, 1, 13, 17, 5, 2, 6, 10]
print("ll :", ll)

# segTree = SegTree_Max(ll)
# print(segTree.tree)
# print(segTree.query(3,7), ll[3:8])
# print(segTree.query(4,7), ll[4:8])
# print(segTree.query(5,7), ll[5:8])
# print(segTree.query(2,5), ll[2:6])
# print(segTree.query(4,5), ll[4:6])
# print(segTree.query(4,5), ll[4:6])
# print(segTree.query(7,12), ll[7:13])
# for _ in range(50) :
#     ### rand list ##########
#     ll = list(range(20))
#     random.shuffle(ll)
#     s = random.randint(0, len(ll)-1)
#     segTree = SegTree_Max(ll)
#     ### rand list end ##########

#     while True :
#         e = random.randint(0, len(ll)-1)
#         if e >= s :
#             break
#     res = segTree.query(s,e)
#     ans = max(ll[s:e+1])
#     print("check :", s, e, res, res == ans)


# # template 2 還沒研究 ##############################################################
# 因為普通 segment tree 也能辦到
# # template 2 end ##############################################################

# # 406. Queue Reconstruction by Height
# # https://leetcode.com/problems/queue-reconstruction-by-height/description
# from math import ceil,log2,inf
# class Solution:
#     def reconstructQueue(self, people):
#         n = len(people)
#         tree = [-inf for _ in range(2**(ceil(log2(n))+1)-1)]
#         def build_(treeIdx,le=0,ri=n-1):
#             if le == ri:
#                 tree[treeIdx] = 1
#             else:
#                 mid = le+(ri-le)//2
#                 tree[treeIdx] = build_(2*treeIdx+1,le,mid) + build_(2*treeIdx+2,mid+1,ri)
#             return tree[treeIdx]
#         def update_(idx,val,treeIdx=0,le=0,ri=n-1):
#             if le<=idx<=ri:
#                 if le==ri:
#                     tree[treeIdx] = val
#                 else: # le!=ri
#                     mid = le+(ri-le)//2
#                     update_(idx,val,2*treeIdx+1,le,mid)
#                     update_(idx,val,2*treeIdx+2,mid+1,ri)
#                     tree[treeIdx] = tree[2*treeIdx+1]+tree[2*treeIdx+2]
#         def query_(k,treeIdx=0,le=0,ri=n-1):
#             if le==ri:
#                 return le
#             mid = le+(ri-le)//2
#             if k<= tree[2*treeIdx+1]:
#                 return query_(k,2*treeIdx+1,le,mid)
#             else: # k > tree[2*treeIdx+1]
#                 return query_(k-tree[2*treeIdx+1],2*treeIdx+2,mid+1,ri)
#         res = [None for _ in range(n)]
#         build_(0)
#         for p in sorted(people,key=lambda x : (x[0],-x[1])):
#             idx = query_(p[1]+1)
#             res[idx] = p
#             update_(idx,0)
#         return res

# s = Solution()
# print("ans :",s.reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
# # [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# # print("ans :",s.reconstructQueue(people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))
# # # [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
