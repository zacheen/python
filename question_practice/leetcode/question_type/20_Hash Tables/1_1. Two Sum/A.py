class Solution:
    def twoSum(self, nums, target):
        # 628 ms
        # k = 0
        # for i in nums:
        #     k += 1
        #     if target - i in nums[k:]:
        #         return(k - 1, nums[k:].index(target - i) + k)

        # 466 ms
        # for i in range(len(nums)):
        #     left = nums[i]
        #     right_start = i+1
        #     if target - left in nums[right_start:]:
        #         return(i, nums[right_start:].index(target - left) + right_start )
                
        # 以下方法有一個大前提 是因為只有一個最佳解

        # 40ms 先做好 hash
        # hash_table={}
        # for i in range(len(nums)) :    # 先做一個hash table
        #     hash_table[nums[i]]=i
            
        # for i, left in enumerate(nums):
        #     if target-left in hash_table:
        #         if hash_table[target-left] != i :
        #             return [i, hash_table[target-left]]
        # return []

        # hash_table={}
        # for i in range(len(nums)):    # 先做一個hash table
        #     hash_table[nums[i]]=i
        # for i in range(len(nums)):
        #     if target-nums[i] in hash_table:
        #         if hash_table[target-nums[i]] != i:
        #             return [i, hash_table[target-nums[i]]]
        # return []

        # 40ms 一邊做一邊加到 hash 裡面
        # 這樣還不用處理一樣的數字的情況
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return([hash_table[target - num], i])
                break    # 看到有人在這加了break, 理論上不會執行到, 但時間卻會比較短
            hash_table[num] = i
        return([])

        # hash_table = {}
        # for i, num in enumerate(nums):
        #     if target - num in hash_table:
        #         return([hash_table[target - num], i])
        #         break    # 看到有人在這加了break, 理論上不會執行到, 但時間卻會比較短
        #     hash_table[num] = i
        # return([])

        # 2022 05 14 又做一次
        # 判斷之前有沒有出現過 應該用set還是比較快 
        # for indx, n in enumerate(nums) :
        #     if target - n in nums[indx+1:] :
        #         return [indx, nums.index(target - n, indx+1)]



s = Solution()
print(s.twoSum(nums = [2,7,11,15], target = 9))