class Solution:
    def searchMatrix(self, matrix, target):
        for_cal = len(matrix[0])
        def get_mat(indx):
            return matrix[indx // for_cal][indx % for_cal]

        # for i in range(12):
        #     print(get_mat(i))

        left,right = 0, for_cal*len(matrix)
        while left<right :
            mid = (left+right) // 2
            # print(left, mid, " : ", nums[left], nums[mid])
            mid_val = get_mat(mid)
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid
        
        if left != for_cal*len(matrix) and get_mat(left) == target :
            return True
        return False

# given ans 差不多概念

s = Solution()
# print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
# print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))
# print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 0))
print(s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 61))       