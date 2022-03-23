# given ans Runtime: 1288 ms, faster than 96.07% of Python3 online
# 原理是 sort 各個線段的第二個位置 
# 每次要剪 都是剪 第二個位置 
# 如果目前這個線段的開頭位置 <= arrowX 代表此線段會被剪到
class Solution(object):
    def findMinArrowShots(self, points):
        arrowX = -sys.maxsize+1
        # print(arrowX)
        ans = 0
        # print(sorted(points, key=lambda x: x[1]))
        for point in sorted(points, key=lambda x: x[1]):
          if point[0] > arrowX :
            ans += 1
            arrowX = point[1]

        return ans

s = Solution()
print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))

