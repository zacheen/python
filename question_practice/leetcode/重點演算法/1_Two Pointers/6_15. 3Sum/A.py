from collections import Counter

# my Runtime: 2456 ms, faster than 27.97% of Python3
# class Solution:
#     def threeSum(self, nums):
#         ans = []
        
#         nums.sort()
#         count = Counter(nums)
        
#         for i in range(len(nums)) :
#             count[nums[i]] -= 1
#             if i>0 and nums[i] == nums[i-1] :
#                 continue
#             for_two_count = count.copy()
#             for j in range(i+1,len(nums)) :
#                 for_two_count[nums[j]] -= 1
#                 # 第一個 j 跟 i 相同的數字不算
#                 if j > i+1 and nums[j] == nums[j-1] :
#                     continue
#                 sum_two = nums[i] + nums[j]
#                 # print(for_two_count, -sum_two)
#                 if for_two_count[-sum_two] > 0 :
#                     ans.append([nums[i],nums[j],-sum_two])

#         return ans

# 看觀念自己實作
# Runtime: 756 ms, faster than 89.52% of Python3
class Solution:
    def threeSum(self, nums):
        nums.sort()
        # print(nums)

        ans = []
        for indx, i in enumerate(nums) :
            # 這裡是為了排除相同的答案
            if indx != 0 and nums[indx] == nums[indx-1] :
                continue
            l = indx+1
            r = len(nums)-1
            while l < r :
                # print(l , r)
                all_sum = nums[l] + nums[r] + i 
                if all_sum == 0 : #nums[l] + nums[r] == -i 
                    ans.append([nums[l],nums[r],i])
                    meet = False
                    # 不管怎樣 兩邊一定都會往前一格
                    l += 1
                    r -= 1
                    # 這裡是為了排除相同的答案
                    # l < r 是為了避免 [0,0,0,0,0] 這種 case  會衝到底 然後跳 error 
                    while nums[l] == nums[l-1] and l < r :
                        l += 1
                    while nums[r] == nums[r+1] and l < r :
                        r -= 1
                    if meet :
                        break
                    
                elif all_sum > 0 : 
                    r -= 1
                else :
                    l += 1

        return ans

                


s = Solution()
# print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,0,0,0,0]))
