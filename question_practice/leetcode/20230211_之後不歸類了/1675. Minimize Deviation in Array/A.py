# 再優化 
    # 使用 & 1 去判斷 /2 的餘數
    # 使用 << 去 *2 , >> 去 /2
# Beats 73.5%
import heapq
class Solution:
    def minimumDeviation(self, nums):
        for i in range(len(nums)):
            if nums[i] & 1 :
                nums[i] = -nums[i] << 1
            else :
                nums[i] = -nums[i]

        heapq.heapify(nums)

        min_num = max(nums)
        min_ans = min_num - nums[0]

        while True :
            # print(nums)
            max_value = heapq.heappop(nums) 
            # print(max_value, min_num)
            min_ans = min(min_ans, min_num - max_value)
            # print(max_value % 2)
            if max_value & 1 == 0 :
                after_devide = max_value >> 1
                heapq.heappush(nums, after_devide)
                min_num = max(min_num, after_devide)
            else :
                break
        return min_ans

# 再優化 直接使用負數處理
# Beats 59.37%
# import heapq
# class Solution:
#     def minimumDeviation(self, nums):
#         for i in range(len(nums)):
#             if nums[i]%2 == 1 :
#                 nums[i] = -nums[i] * 2
#             else :
#                 nums[i] = -nums[i]

#         heapq.heapify(nums)

#         min_num = max(nums)
#         min_ans = min_num - nums[0]

#         while True :
#             # print(nums)
#             max_value = heapq.heappop(nums) 
#             # print(max_value, min_num)
#             min_ans = min(min_ans, min_num - max_value)
#             # print(max_value % 2)
#             if max_value % 2 == 0 :
#                 after_devide = max_value//2
#                 heapq.heappush(nums, after_devide)
#                 min_num = max(min_num, after_devide)
#             else :
#                 break
#         return min_ans

# 方法 5 想法 : 如果只是要找出最大值 應該用 tree 去實作 ( O(logn) ) sort 是 ( O(nlogn) ) (直接少了 O(n)))
# Beats 46.75%
# 所以並不是我的邏輯有問題 只是沒有挑到對的演算法去計算
import heapq
class Solution:
    def minimumDeviation(self, nums):
        for i in range(len(nums)):
            if nums[i]%2 == 1 :
                nums[i] = -nums[i] * 2
            else :
                nums[i] = -nums[i]

        heapq.heapify(nums)
        # print(nums)

        min_num = -max(nums)
        min_ans = None
        while True :
            # print(nums)
            max_value = -1 * heapq.heappop(nums) 
            if min_ans == None :
                min_ans = max_value - min_num
            # print(max_value, min_num)
            min_ans = min(min_ans, max_value - min_num)
            # print(max_value % 2)
            if max_value % 2 == 0 :
                after_devide = max_value//2
                heapq.heappush(nums, -after_devide)
                min_num = min(min_num, after_devide)
            else :
                break
        return min_ans

# 方法 4 還是 Time Limit Exceeded
# class Solution:
#     def minimumDeviation(self, nums):
#         def binarySearch2(nums, target):
#             left, right = 0, len(nums)  
#             while left < right:
#                 mid = (left + right) // 2 
#                 if nums[mid] == target:
#                     return mid
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid
            
#             if left != len(nums) and nums[left] == target:  # 如果不是超過範圍 且 在範圍內找不到 target == 沒有此項目
#                 return -1
#             return left
#             # 回傳 -1 代表有重複的項目

#         for i in range(len(nums)):
#             if nums[i]%2 == 1 :
#                 nums[i] = nums[i] * 2
#         nums.sort()
#         # print(nums)

#         min_ans = nums[-1] - nums[0]
#         while True :
#             if nums[-1] % 2 == 0 :
#                 after_devide = nums[-1]//2
#                 # 判斷插入的位置
#                 insert_indx = binarySearch2(nums[:-1], after_devide)
#                 if insert_indx == -1 :
#                     nums = nums[:insert_indx] + nums[insert_indx:-1]
#                 else :
#                     nums = nums[:insert_indx] + [after_devide] + nums[insert_indx:-1]
#                 min_ans = min(nums[-1] - nums[0], min_ans)
#                 # print(nums)
#                 # print("min_ans :",min_ans)
#             else :
#                 break

#         return min_ans
            
        

# 方法 3 看解答修改 
    # Time Limit Exceeded 
    # 因為除可以無限除 但是乘只能乘一次 所以我應該要先弄成最大的可能 再往下找最佳解
    # 原本想要從小做到大 是因為一開始我以為我可以知道什麼時候終止 但發現沒辦法 
# class Solution:
#     def minimumDeviation(self, nums):
#         def binarySearch2(nums, target):
#             left, right = 0, len(nums)  
#             while left < right:
#                 mid = (left + right) // 2 
#                 if nums[mid][0] == target:
#                     return mid
#                 elif nums[mid][0] < target:
#                     left = mid + 1
#                 else:
#                     right = mid

#             return left

#         nums = [[n, 0] for n in nums]

#         for i in range(len(nums)) :
#             while nums[i][0] % 2 == 0 :
#                 nums[i][0] //= 2
#                 nums[i][1] += 1
#         # print(nums)

#         nums.sort()
#         # print(nums)

#         min_ans = nums[-1][0] - nums[0][0]
#         while True :
#             if nums[0][0] % 2 == 1 or nums[0][1]:
#                 after_mul = nums[0][0]*2
#                 # 判斷插入的位置
#                 insert_indx = binarySearch2(nums[1:], after_mul) + 1 # +1 是因為我丟進去就沒放第一個
#                 # print("insert_indx :", insert_indx, "nums :", nums, "after_mul :", after_mul)
#                 nums = nums[1:insert_indx] + [[after_mul, max(0, nums[0][1]-1)]] + nums[insert_indx:]
#                 # print(nums)

#                 min_ans = min(nums[-1][0] - nums[0][0], min_ans)
#             else :
#                 break

#         return min_ans

# 方法 2 全部都先/2 到不能再除 紀錄總共除了幾次 -> sort -> 如果可以(本身是奇數 或 有剩餘除了的次數) *2  -> 如果可以縮小距離 binary search 插入
# fail [[389], [395], [423], [610], [733]] 這種情況要同時把 [389], [395] 乘2 才會得到最小值
# class Solution:
#     def minimumDeviation(self, nums):
#         def binarySearch2(nums, target):
#             left, right = 0, len(nums)  
#             while left < right:
#                 mid = (left + right) // 2 
#                 if nums[mid][0] == target:
#                     return mid
#                 elif nums[mid][0] < target:
#                     left = mid + 1
#                 else:
#                     right = mid

#             return left

#         nums = [[n, 0] for n in nums]

#         for i in range(len(nums)) :
#             while nums[i][0] % 2 == 0 :
#                 nums[i][0] //= 2
#                 nums[i][1] += 1
#         # print(nums)

#         nums.sort()
#         # print(nums)

#         while True :
#             if nums[0][0] % 2 == 1 or nums[0][1]:
#                 after_mul = nums[0][0]*2
#                 # 如果插在最後一個 就要判斷會不會比較好
#                 if after_mul > nums[-1][0] :
#                     # 如果距離沒有變小 (原本的距離 < 後來的距離)
#                     print((nums[-1][0] - nums[0][0]), (after_mul - nums[1][0]))
#                     if (nums[-1][0] - nums[0][0]) < (after_mul - nums[1][0]) :
#                         break
#                 # 判斷插入的位置
#                 insert_indx = binarySearch2(nums[1:], after_mul) + 1 # +1 是因為我丟進去就沒放第一個
#                 print("insert_indx :", insert_indx, "nums :", nums, "after_mul :", after_mul)
#                 nums = nums[1:insert_indx] + [[after_mul, max(0, nums[0][1]-1)]] + nums[insert_indx:]
#                 # print(nums)
#             else :
#                 break

#         print("result nums :", nums)
#         return nums[-1][0] - nums[0][0]

# my 方法 1 sort -> 先處理大的 /2 -> 如果可以縮小距離 binary search 插入 -> 再處理小的 *2 -> 如果可以縮小距離 binary search 插入
    # 失敗 [10, 8] # 那時後有懷疑 但是沒有想到 testcase 可以反駁
# class Solution:
#     def minimumDeviation(self, nums):
#         def binarySearch2(nums, target):
#             left, right = 0, len(nums)  
#             while left < right:
#                 mid = (left + right) // 2 
#                 if nums[mid] == target:
#                     return mid
#                 elif nums[mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid

#             if left != len(nums) and nums[left] >= target:
#                 return left
#             return -1

#         # ll = [1, 3, 4, 5, 16]
#         # print(binarySearch2(ll, 8))

#         nums.sort()
#         while True :
#             if nums[-1] % 2 == 0 :
#                 after_devide = nums[-1]//2
#                 # 如果插在第一個 就要判斷會不會比較好
#                 if after_devide < nums[0] :
#                     # 如果距離沒有變小 (原本的距離 < 後來的距離)
#                     if (nums[-1] - nums[0]) < (nums[-2] - after_devide) :
#                         break
#                 # 判斷插入的位置
#                 insert_indx = binarySearch2(nums[:-1], after_devide)
#                 nums = nums[:insert_indx] + [after_devide] + nums[insert_indx:-1]
#                 # print(nums)
#             else :
#                 break

#         while True :
#             if nums[0] % 2 == 1 :
#                 after_mul = nums[0]*2
#                 # 如果插在最後一個 就要判斷會不會比較好
#                 if after_mul > nums[-1] :
#                     # 如果距離沒有變小 (原本的距離 < 後來的距離)
#                     if (nums[-1] - nums[0]) < (after_mul - nums[1]) :
#                         break
#                 # 判斷插入的位置
#                 insert_indx = binarySearch2(nums[1:], after_mul)
#                 nums = nums[1:insert_indx] + [after_mul] + nums[insert_indx:]
#                 print(nums)
#             else :
#                 break

#         return nums[-1] - nums[0]


# given ans

s = Solution()
print(s.minimumDeviation([1,2,3,4]))    # [2,2,3,2]   # 3 - 2 = 1
# print(s.minimumDeviation([4,1,5,20,3])) # [4,2,5,5,3] # 5 - 2 = 3
# print(s.minimumDeviation([2,10,8]))     # [2,5,4]     # 5 - 2 = 3
#                                   # 不能是 [4,5,4] 因為 2 是偶數不能再乘 2
# my test case
# print(s.minimumDeviation([10,8,8]))
# print(s.minimumDeviation([4,1,5,3,32,16])) # [4,2,5,5,3] # 5 - 2 = 3
print(s.minimumDeviation([610,778,846,733,395]))


