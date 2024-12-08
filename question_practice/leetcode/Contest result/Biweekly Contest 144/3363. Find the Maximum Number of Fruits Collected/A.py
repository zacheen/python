# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

from typing import List
import functools

# my ver1 using filling 0
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        # 左上角的人只能走對角線 才能在N步內到達右下角
        top_left_sum = sum(fruits[i][i] for i in range(len(fruits)))

        # 右上跟左下的人都無法跨越對角線 > i,j 不相等
        # 右上
        # 先把第一排歸0
        for i in range(len(fruits)-1) :
            fruits[0][i] = 0
            fruits[i][0] = 0
        for i1 in range(1, len(fruits)) : # 從上到下
            # 每個點從上面3格選最大的 
            for i2 in range(len(fruits)-1, -1 ,-1) : # 從上面已經走過的
                if i1 == i2 : # 不能過中線
                    break
                
                if i2 <= len(fruits)-2-i1 :
                    fruits[i1][i2] = 0

                max_top3 = 0
                prev_i1 = i1-1
                for prev_i2 in range(i2-1, i2+2) :
                    if prev_i2 < len(fruits) :
                        max_top3 = max(max_top3, fruits[prev_i1][prev_i2])
                fruits[i1][i2] += max_top3
        # print("top", fruits[len(fruits)-2][len(fruits)-1])
        # 左下
        for i2 in range(1, len(fruits)) : # 從左到右
            for i1 in range(len(fruits)-1, -1 ,-1) : # 從上面已經走過的
                if i1 == i2 : # 不能過中線
                    break
                if i1 <= len(fruits)-2-i2 :
                    fruits[i1][i2] = 0
                max_top3 = 0
                prev_i2 = i2-1
                for prev_i1 in range(i1-1, i1+2) :
                    if prev_i1 < len(fruits) :
                        # print(prev_i1, prev_i2, i1, i2, fruits[prev_i1][prev_i2])
                        max_top3 = max(max_top3, fruits[prev_i1][prev_i2])
                fruits[i1][i2] += max_top3
        # print("left", fruits[len(fruits)-1][len(fruits)-2])
        print(fruits)

        return top_left_sum + fruits[len(fruits)-2][len(fruits)-1] + fruits[len(fruits)-1][len(fruits)-2]

# my ver2 using indx to avoid cal
# 971ms Beats77.39%
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        # 左上角的人只能走對角線 才能在N步內到達右下角
        top_left_sum = sum(fruits[i][i] for i in range(len(fruits)))

        # 右上跟左下的人都無法跨越對角線 > i,j 不相等
        limitation = len(fruits)-2
        # 右上
        for i1 in range(1, len(fruits)) : # 從上到下
            # 每個點從上面3格選最大的 
            for i2 in range(len(fruits)-1, len(fruits)-2-i1 ,-1) : # 從上面已經走過的
                if i1 == i2 : # 不能過中線
                    break
                max_top3 = 0
                prev_i1 = i1-1
                for prev_i2 in range(i2-1, i2+2) :
                    if (prev_i1+prev_i2) > limitation and prev_i2 < len(fruits):
                        max_top3 = max(max_top3, fruits[prev_i1][prev_i2])
                fruits[i1][i2] += max_top3
        # print("top", fruits[len(fruits)-2][len(fruits)-1])
        # 左下
        for i2 in range(1, len(fruits)) : # 從左到右
            for i1 in range(len(fruits)-1, len(fruits)-2-i2 ,-1) : # 從上面已經走過的
                if i1 == i2 : # 不能過中線
                    break
                max_top3 = 0
                prev_i2 = i2-1
                for prev_i1 in range(i1-1, i1+2) :
                    if (prev_i1+prev_i2) > limitation and prev_i1 < len(fruits):
                        max_top3 = max(max_top3, fruits[prev_i1][prev_i2])
                fruits[i1][i2] += max_top3
        # print("left", fruits[len(fruits)-1][len(fruits)-2])
        # print(fruits)
        return top_left_sum + fruits[len(fruits)-2][len(fruits)-1] + fruits[len(fruits)-1][len(fruits)-2]


# given ans
# similar concept but different method

s = Solution()
# print("ans :",s.maxCollectedFruits([[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]])) #100
# print("ans :",s.maxCollectedFruits([[1,1],[1,1]])) #4 
# print("ans :",s.maxCollectedFruits([[16,3,11,14,14],[3,0,10,13,14],[7,18,8,7,18],[7,8,5,7,5],[0,14,8,1,0]])) #105
print("ans :",s.maxCollectedFruits([[8,5,0,17,15],[6,0,15,6,0],[7,19,16,8,18],[11,3,2,12,13],[17,15,15,4,6]])) #145




