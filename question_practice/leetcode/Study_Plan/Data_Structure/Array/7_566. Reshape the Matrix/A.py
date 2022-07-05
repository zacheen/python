# my Runtime: 104 ms, faster than 66.97% of Python3
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r*c :
            return mat
        
        one_d = []
        for m in mat :
            one_d += m
            
        ans = []
        for start in range(0,r*c,c) :
            ans.append(one_d[start:start+c])
        return ans

# given ans
# 更慢...
# 但可以學習的是 處理index的方法
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if nums == [] or r * c != len(nums) * len(nums[0]):
            return nums

        ans = [[0 for j in range(c)] for i in range(r)]
        k = 0

        for row in nums:
            for num in row:
                ans[k // c][k % c] = num
                k += 1

        return ans

s = Solution()
print(s.matrixReshape())



