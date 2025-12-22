# 3531. Count Covered Buildings
# https://leetcode.com/problems/count-covered-buildings

from typing import List
from math import inf
from collections import defaultdict

# my v1 : 493ms Beats76.47%
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        bucket_x = defaultdict(list)
        for x, y in buildings :
            bucket_x[x].append(y)
        mid = set()
        for key_x, list_y in bucket_x.items():
            list_y.sort()
            for mid_y in list_y[1:-1]:
                mid.add((key_x, mid_y))

        bucket_y = defaultdict(list)
        for x, y in buildings :
            bucket_y[y].append(x)
        ans_cnt = 0
        for key_y, list_x in bucket_y.items():
            list_x.sort()
            for mid_x in list_x[1:-1]:
                if (mid_x, key_y) in mid :
                    ans_cnt += 1
        return ans_cnt
    
# my v2 : this version would be faster if there is a lot of point in the same x or y
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        bucket_x = defaultdict(list)
        for x, y in buildings :
            bucket_x[x].append(y)
        mid = set()
        for key_x, list_y in bucket_x.items():
            min_y = min(list_y)
            max_y = max(list_y)
            for y in list_y:
                if y != min_y and y != max_y :
                    mid.add((key_x, y))

        bucket_y = defaultdict(list)
        for x, y in buildings :
            bucket_y[y].append(x)
        ans_cnt = 0
        for key_y, list_x in bucket_y.items():
            min_x = min(list_x)
            max_x = max(list_x)
            for x in list_x:
                if x != min_x and x != max_x :
                    if (x, key_y) in mid :
                        ans_cnt += 1
        return ans_cnt

# given ans 171 ms : same concept, different implement method
    # this method even require less memory
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        minRowIndices = [n + 1] * (n + 1)
        maxRowIndices = [0] * (n + 1)
        minColIndices = [n + 1] * (n + 1)
        maxColIndices = [0] * (n + 1)

        for building in buildings:
            row = building[0]
            col = building[1]

            if row < minRowIndices[col]:
                minRowIndices[col] = row
            if row > maxRowIndices[col]:
                maxRowIndices[col] = row

            if col < minColIndices[row]:
                minColIndices[row] = col
            if col > maxColIndices[row]:
                maxColIndices[row] = col

        count = 0
        for building in buildings:
            row = building[0]
            col = building[1]

            if (minRowIndices[col] < row and
                maxRowIndices[col] > row and
                minColIndices[row] < col and
                maxColIndices[row] > col):
                count += 1

        return count

s = Solution()
print("ans :",s.countCoveredBuildings(n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]])) # 0
print("ans :",s.countCoveredBuildings(n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]])) # 1



