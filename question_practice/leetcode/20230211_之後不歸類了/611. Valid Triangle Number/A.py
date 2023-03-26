# my Time Limit Exceeded
class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        ans_count = 0
        for i in range(len(nums)) :
            for j in range(i):
                sub_res = nums[i] - nums[j]
                for k in range(j):
                    # j k is the small two edge
                    if nums[k] > sub_res :
                        ans_count += (j-k)
                        break
        return ans_count

# my ver2 Beats 5.71%
# import bisect # 其實也可以用 bisect 不過我優化了 可以使用 left, right 降低計算次數
class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        ans_count = 0
        for i in range(len(nums)) :
            for j in range(i):
                sub_res = nums[i] - nums[j]
                
                # j k is the small two edge, i is the largest edge
                # 優化
                # for k in range(j):
                    # if nums[k] > sub_res :
                    #     ans_count += (j-k)
                    #     break
                # 優化結果 : 使用 binary search 找符合結果的位置
                left, right = 0, j # right 通常會超出界線(因為執行的時候不會執行到這個數字)
                while left < right:
                    mid = (left + right) // 2
                    if nums[mid] <= sub_res : # 條件 (如果 == target 應該要是 False)
                        # 沒通過
                        left = mid + 1
                    else:
                        # 通過(包含 == target 的情況)
                        right = mid 
                ans_count += (j - left)
        return ans_count

# my ver3 Beats 6.67%
# 參考 ans : 其實就是 i 跟 j 的距離也可以判斷 提早結束
# import bisect # 其實也可以用 bisect 不過我優化了 可以使用 left, right 降低計算次數
class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        ans_count = 0
        for i in range(len(nums)) :
            for j in range(i-1, -1, -1):
                sub_res = nums[i] - nums[j]
                left, right = 0, j # right 通常會超出界線(因為執行的時候不會執行到這個數字)
                while left < right:
                    mid = (left + right) // 2
                    if nums[mid] <= sub_res : # 條件 (如果 == target 應該要是 False)
                        # 沒通過
                        left = mid + 1
                    else:
                        # 通過(包含 == target 的情況)
                        right = mid 
                
                poss_ans = j - left
                if poss_ans == 0 :
                    break
                ans_count += poss_ans     

        return ans_count

# given ans Beats 100%
# 我有再優化一下
class Solution:
    def triangleNumber(self, nums):
        ans = 0
        nums.sort()

        # k is the largest edge
        for k, largest_edge in enumerate(nums):
            # 使用 sliding widows
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > largest_edge:
                    # 現在 的邊長 是 k 跟 j，i總共有幾種解答 
                    # 每次 j 不一樣的時候就增加一次解答
                    ans += j - i 
                    j -= 1
                else:
                    # 找尋適合的 i
                    # (這裡用 binary search 應該不會比較快)
                    i += 1

        return ans

s = Solution()
print(s.triangleNumber([2,2,3,4]))
print(s.triangleNumber([4,2,3,4]))



