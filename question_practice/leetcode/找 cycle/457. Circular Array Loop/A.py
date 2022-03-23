# 好像題目有問題
# 

# v1 理解錯誤 一定要繞一圈
# class Solution:
#     def circularArrayLoop(self, nums):
#         mem = [False]*len(nums) # 走過改成 True
#         last_mem = mem.copy()
#         for indx in range(len(nums)) :
#             last_indx = 0
#             last2_indx = 0
#             last_time = False
#             while True :
#                 if mem[indx] :
#                     if last_mem[indx] :
#                         last_time = True
#                     break
#                 print(indx)
#                 mem[indx] = True
#                 last2_indx = last_indx
#                 last_indx = indx
#                 indx += nums[indx]
#                 indx = indx % len(nums)

#             if last_time :
#                 continue
            
#             print(indx, last_indx, last2_indx)
#             if indx != last_indx and indx != last2_indx and last_indx and last2_indx :
#                 return True

#             last_mem = mem.copy()
        
#         return False

# v2 Runtime: 46 ms, faster than 80.91% of Python3 
# 只要繞一圈回來的地方不是自己即可
# class Solution:
#     def circularArrayLoop(self, nums):
#         mem = [False]*len(nums) # 走過改成 True
#         last_mem = mem.copy()
#         for indx in range(len(nums)) :
#             # print("last_mem :",last_mem)
#             last_time = False
#             while True :
#                 if mem[indx] :
#                     if last_mem[indx] :
#                         last_time = True
#                     break
#                 # print(indx)
#                 mem[indx] = True
#                 indx += nums[indx]
#                 indx = indx % len(nums)

#             last_mem = mem.copy()   
#             if last_time :
#                 continue
            
#             # print("重複的 : ",indx)

#             # 確定 不是回到自己 and 有繞超過一圈 所以從剛剛的 index 再跑一圈一次
#             # 還要判斷是不是全部的項目都是全正 或 全負的 ...
#             start_indx = indx
#             round_count = 0
#             is_ans = False

#             if nums[indx] > 0:
#                 is_pos = True
#             else :
#                 is_pos = False

#             while True :
#                 # print(nums[indx], nums[indx] > 0, is_pos)
#                 if (nums[indx] > 0) != is_pos :
#                     # print("不是全正或全負")
#                     is_ans = False
#                     break
#                 indx += nums[indx]
#                 round_count += indx // len(nums)
#                 indx = indx % len(nums)
#                 if indx == start_indx :
#                     break
#                 # 只要走過超過一個就可以確定不是回到自己
#                 is_ans = True   

#             if is_ans and round_count != 0 :
#                 return True

#         return False

# given ans Runtime: 32 ms, faster than 98.10% of Python3 
# 這裡還是用 神奇的 fast slow 找 cycle
class Solution:
    def circularArrayLoop(self, nums):
        # 找下一個位置
        def advance(i):
            return (i + nums[i]) % len(nums)

        # 例外判斷
        if len(nums) < 2:
            return False

        for i, num in enumerate(nums):
            # 題目好像有說 num 不會是 0
            if num == 0:
                continue

            slow = i
            fast = advance(slow)
            # num * nums[fast] > 0 判斷是否為全正或全負
            while num * nums[fast] > 0 and num * nums[advance(fast)] > 0:
                if slow == fast:
                    if slow == advance(slow):
                        break
                    return True
                slow = advance(slow)
                fast = advance(advance(fast))

            slow = i
            sign = num
            while sign * nums[slow] > 0:
                next = advance(slow)
                nums[slow] = 0
                slow = next

        return False

        
s = Solution()
# print(s.circularArrayLoop([2,-1,1,2,2]))
# print(s.circularArrayLoop([1,1,1,5,-1]))
# print(s.circularArrayLoop([1,1,1,1,-1]))
# print(s.circularArrayLoop([-1,-2,-3,-4,-5]))
# print(s.circularArrayLoop([1,-1,1,1,3]))

# print(s.circularArrayLoop([-2,1,-1,-2,-2]))
# print(s.circularArrayLoop([2,2,2,2,2,4,7]))
print(s.circularArrayLoop([1,1])) # True
print(s.circularArrayLoop([-1,3])) # False
print(s.circularArrayLoop([-2,1,-2,3,1])) # False

# 
# print(s.circularArrayLoop([1,2,2,-1]))
# print(s.circularArrayLoop([2,-1,1,2,2])) # True