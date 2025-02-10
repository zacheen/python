# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

# my practice again : 18ms Beats44.59%
import heapq
class Solution:
    def trap(self, height):
        ans = 0
        l = 0
        r = len(height) - 1
        heap = [(height[0], True), (height[-1], False)] # (height, is_left)
        heapq.heapify(heap)
        while l < r :
            heap_h, is_left = heapq.heappop(heap)
            if is_left :
                l += 1
                nei_h = height[l]
            else :
                r -= 1
                nei_h = height[r]
            
            if heap_h > nei_h :
                ans += max(heap_h-nei_h, 0)
                heapq.heappush(heap, (heap_h, is_left))
            else :
                heapq.heappush(heap, (nei_h, is_left))
        return ans

# # My 經過一個晚上思考
# # Runtime: 101 ms, faster than 82.76% of Python3
# # l r 先找各自初始下降的地方
# # 矮的那一邊 縮回來找高點 找到更高的點 就算一個區間
# class Solution:
#     def trap(self, height):
#         def cal_total(l, r):
#             print("in cal_total",l, r)
#             h = min(height[l], height[r])
#             total = 0
#             for i in range(l, r+1):
#                 total += max(h - height[i], 0)
#             return total
        
#         l = 0
#         r = len(height)-1
#         # l r 先找各自初始下降的地方
#         while l < len(height)-1 and height[l+1] > height[l] :
#             l += 1
#         while r > 1 and height[r-1] > height[r] :
#             r -= 1
#         print(l,r)

#         total = 0
        
#         while l < r :
#             if height[l] < height[r] :
#                 # 左邊比較矮
#                 # 找比左邊高的點
#                 temp_l = l+1
#                 while height[temp_l] < height[l] :
#                     temp_l += 1
#                 total += cal_total(l, temp_l)
#                 l = temp_l

#             else :
#                 temp_r = r-1
#                 while height[temp_r] < height[r] :
#                     temp_r -= 1
#                 total += cal_total(temp_r, r)
#                 r = temp_r
#         return total

# given ans 
# 每個柱子都找自己右邊和左邊的次低點 取比較低的點
# 應該算特殊解法
# ori
#         #
#     #   #   #
#   # #   # # #
#   # # # # # #
#   # # # # # #

# left (從左邊填滿)
#         # # #
#     # # # # #
#   # # # # # #
#   # # # # # #
#   # # # # # #

# right (從右邊填滿)
#   # # # #
#   # # # # # #
#   # # # # # #
#   # # # # # #
#   # # # # # #

# 取 小值 (就是各個位置的水位 在減掉原本的高度即可)
#         #
#     # # # # #
#   # # # # # #
#   # # # # # #
#   # # # # # #
# given ans : but slower
class Solution:
    def trap(self, height):
        n = len(height)
        l = [0] * n  # l[i] := max(height[0..i])
        r = [0] * n  # r[i] := max(height[i..n))

        for i, h in enumerate(height):
            l[i] = h if i == 0 else max(h, l[i - 1])

        for i, h in reversed(list(enumerate(height))):
            r[i] = h if i == n - 1 else max(h, r[i + 1])

        return sum(min(l[i], r[i]) - h for i, h in enumerate(height))

# https://walkccc.me/LeetCode/problems/0042/  Approach 2
# 更進一步的想法 其實只要先找到 Max 
# 再各自做左邊跟右邊就好了


s = Solution()
# print(s.trap([1,0,3]))
# print(s.trap([0,2,1,0,1,2,1]))
# print(s.trap([0,2,1,0,1,3,1,2,1,2]))
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) #
# print(s.trap([4,2,0,3,2,5])) #
# print(s.trap([4,2,3])) #
# print(s.trap([3,2,4]))