# my Runtime: 668 ms, faster than 98.52% of Python3 
class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) -1 
        max_area = 0
        min_hight = min(height[r],height[l])
        while l < r :
            if height[l] >= min_hight and height[r] >= min_hight :
                min_hight = min(height[r],height[l])
                max_area = max((r-l)*min_hight, max_area)
            
            if height[r] > height[l] :
                l += 1
            else :
                r -= 1

        return max_area
        
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))

