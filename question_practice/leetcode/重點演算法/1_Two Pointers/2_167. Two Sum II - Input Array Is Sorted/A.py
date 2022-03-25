# my Runtime: 132 ms, faster than 76.12% of Python3
class Solution:
    def twoSum(self, numbers, target) :
        left = 0
        right = len(numbers) - 1

        while right >= left :
            this_sum = numbers[left]+numbers[right]
            if this_sum == target : 
                return [left+1, right+1]
            elif this_sum > target :
                right -= 1
            else  :
                left += 1
                
        return None

s = Solution()
print(s.twoSum(numbers = [2,3,4], target = 6))
print(s.twoSum(numbers = [2,7,11,15], target = 9))
print(s.twoSum(numbers = [1,2,3,4,7,8], target = 7))