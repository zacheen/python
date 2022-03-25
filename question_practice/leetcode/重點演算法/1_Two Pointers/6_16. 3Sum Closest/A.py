# My Runtime: 216 ms, faster than 83.13% of Python3
# 加了 <if indx != 0 and nums[indx] == nums[indx-1]: > 之後
#       Runtime: 188 ms, faster than 88.04% of Python3
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        closest_dist = abs(target - closest)
        for indx, i in enumerate(nums) :
            # 我看別人有加這個 但是我不知道 testcase  所以不確定會不會比較快
            if indx != 0 and nums[indx] == nums[indx-1]:
                continue
            
            l = indx+1
            r = len(nums) - 1

            while l < r :
                sum3 = i + nums[l] + nums[r]
                # print(sum3)
                sub_res = sum3 - target
                if abs(sub_res) < closest_dist:
                    closest_dist = abs(sub_res)
                    closest = sum3

                if sub_res > 0 :
                    r -= 1
                elif sub_res < 0 :
                    l += 1
                else :
                    return closest

        return closest


s = Solution()
# print(s.threeSumClosest([-1,2,1,-4], 1))
# print(s.threeSumClosest([1,1,1,0], -100))
# print(s.threeSumClosest([-3,-2,-5,3,-4,-3], -1))
print(s.threeSumClosest([-1,0,1,1,55],3))

