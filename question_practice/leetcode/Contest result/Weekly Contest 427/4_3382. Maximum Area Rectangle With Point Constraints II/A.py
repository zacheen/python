# 3382. Maximum Area Rectangle With Point Constraints II
# https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/description/

from typing import List
import functools

# # my Time Limit Exceeded
# # worst case is none of the previous link is deleted
# from itertools import pairwise
# class Solution:
#     def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
#         points = [(x,y) for x,y in zip(xCoord, yCoord)]
#         points.sort()
#         links = []
#         ans = -1
#         for new_indx, ((x1,x2),(y1,y2)) in enumerate(pairwise(points)) :
#             del_list = []
#             for old_indx, (l1,(l1s, l1e)) in enumerate(links) :
#                 if l1s<=y2 and y2<=l1e :
#                     del_list.append(old_indx)
#                     if l1s==y2 :
#                         next_indx = new_indx+2
#                         # print("maybe",points[next_indx])
#                         if next_indx<len(points) and y1 == points[next_indx][0] and l1e == points[next_indx][1] :
#                             # print("new r:",l1e,l1s,y1,l1)
#                             ans = max( ans, (l1e-l1s)*(y1-l1) )
#             while del_list :
#                 del(links[del_list.pop()])
#             if x1 == y1 :
#                 links.append((x1,(x2,y2)))
#         return ans

# given ans 1833ms Beats80.95%
# reduce the time of updating nodes
from math import inf
from itertools import pairwise
class Solution:
    def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
        points = list(zip(xCoord, yCoord))

        # sort by x, then y
        points.sort()
        yAxis = sorted(set(yCoord)) # 全部的 Y 點，從小到大
        yPos = {y: i for i,y in enumerate(yAxis)} # 不會變，用來查詢Y的indx順序
        yMax = {y: -inf for y in yAxis} # 紀錄 Y 對到的 X 最大是多少
        maxTree = SegTree(len(yAxis))
        res = -1

        for (prevX, prevY), (x,y) in pairwise(points): # 按 X 的順序一次取兩點
            # 如果兩點的 X 相同 > 可以成為邊
            # !! yMax[prevY] == yMax[y] > 新的這兩點跟前面的兩點距離相同 > 是長方形
            if prevX == x and yMax[prevY] == yMax[y] \
                and yMax[y] > maxTree.query(yPos[prevY], yPos[y]):
                # and no other points in the rectangle
                res = max(res, (y-prevY) * (x - yMax[y]))

            # update the info of (prevX, prevY)
            yMax[prevY] = prevX
            maxTree.update(yPos[prevY], prevX)
        return res

class SegTree:
    def __init__(self, n: int):
        self.n = 1<<n.bit_length()
        self.tree = [-inf] * (self.n<<1)

    def update(self, idx: int, val: int):
        idx += self.n
        while idx:
            self.tree[idx] = val
            idx >>= 1

    def query(self, l: int, r: int) -> int:
        res = -inf
        l += self.n
        r += self.n
        while r-l > 1:
            if not l&1:
                res = max(res, self.tree[l+1])
            if r&1:
                res = max(res, self.tree[r-1])
            l >>= 1
            r >>= 1
        return res
    
# # my using template 3116ms Beats37.35%
# from math import inf
# from itertools import pairwise
# class Solution:
#     def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
#         points = list(zip(xCoord, yCoord))

#         # sort by x, then y
#         points.sort()
#         yAxis = sorted(set(yCoord))
#         yPos = {y: i for i,y in enumerate(yAxis)}
#         yMax = {y: -inf for y in yAxis}
#         maxTree = SegTree_Max(len(yAxis))
#         res = -1

#         for (prevX, prevY), (x,y) in pairwise(points):
#             if prevX == x and yMax[prevY] == yMax[y] \
#                 and yMax[y] > maxTree.query(yPos[prevY], yPos[y]):
#                 res = max(res, (y-prevY) * (x - yMax[y]))

#             # update the info of (prevX, prevY)
#             yMax[prevY] = prevX
#             maxTree.update(yPos[prevY], prevX)
#         return res

# class SegTree_Max:
#     def __init__(self, nums):
#         self.n = nums
#         self.tree = [-inf] * 2 * self.n

#     def update(self, index, val):
#         index += self.n
#         self.tree[index] = val
#         while index > 1:
#             # update node
#             self.tree[index>>1] = max(self.tree[index], self.tree[index^1])
#             index >>= 1

#     def query(self, left, right):
#         left += self.n+1
#         right += self.n-1
#         res = -inf
#         while left <= right:
#             if left & 1 :
#                 # combine result
#                 res = max(res, self.tree[left])
#                 left += 1
#             if not (right & 1) :
#                 # combine result
#                 res = max(res, self.tree[right])
#                 right -= 1
#             left >>= 1
#             right>>= 1
#         return res

s = Solution()
# print(s.maxRectangleArea(xCoord = [1,1,3,3], yCoord = [1,3,1,3]))
# print(s.maxRectangleArea(xCoord = [1,1,3,3], yCoord = [1,4,1,4]))
# print(s.maxRectangleArea(xCoord = [1,1,5,5,3], yCoord = [2,6,2,6,4]))
print(s.maxRectangleArea(xCoord = [0,1,1,5,5,3,7,7], yCoord = [3,2,6,2,6,4,2,6]))
# print(s.maxRectangleArea(xCoord = [1,1,3,3,1,3], yCoord = [1,3,1,3,2,2]))



