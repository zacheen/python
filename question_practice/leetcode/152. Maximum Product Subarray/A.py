# given ans
class Solution:
    def maxProduct(self, nums):
        if min(nums)>0:
            return reduce(lambda x, y: x*y, nums)
        if not nums:
            return 
        locMin = locMax = gloMax = nums[0]
        for i in range(1,len(nums)): # 不包含第一個數字
            if nums[i]<0:
                temp = locMax
                locMax = max(locMin*nums[i], nums[i]) # 這個是為了處理0 也同時處理了相乘之後有沒有更大
                locMin = min(temp*nums[i], nums[i])
            else:
                locMax = max(locMax*nums[i], nums[i])
                locMin = min(locMin*nums[i], nums[i])
            print(locMax, locMin)
            gloMax=max(gloMax, locMax)
        return gloMax

# 想要用前後去做
# class Solution:
#     def maxProduct(self, nums):
#         import sys
#         MaxMul = -sys.maxsize+1
#         Maxl,Maxr = 0,0
        
#         metZero = False
        
#         if len(nums) == 0 :
#             return 0

#         # init
#         nowMul = 1
#         l,r = 0,0
#         if nums[0] > 0 :
#             nowPos = True
#         else :
#             nowPos = False

#         calAns = False
#         while True :
#             if r >= len(nums) :
#                 calAns = True
#             else :
#                 print("now :",nums[r], nowMul)
            
#             if metZero :
#                 if nums[r] > 0 :
#                     nowPos = True
#                 elif nums[r] < 0:
#                     nowPos = False
#                 else :
#                     r = r + 1
#                     continue
#                 l = r + 1
#                 nowMul = nums[r]
#                 # nowMul = 1
#                 metZero = False
#                 r = r + 1
#                 continue
            
#             if (calAns or nums[r] <= 0) and nowPos :
#                 # 現在是正的但我遇到了一個負的數字 或 0
#                 if nowMul > MaxMul :
#                     MaxMul = nowMul
#                     Maxl,Maxr = l,r

#                 if calAns :
#                     break

#                 # reset 
#                 l = r + 1
#                 print("l :",l )
#                 print("nowMul reset")
#                 nowMul = 1
#                 nowPos = False
            
#             elif (calAns or nums[r] >= 0) and nowPos==False :
#                 # 現在是負的但我遇到了一個正的數字
#                 # 到上一個為止的總和
#                 if nowMul > MaxMul :
#                     MaxMul = nowMul
#                     Maxl,Maxr = l,r
                
#                 if l < r :
#                     print("判斷看看少一個的結果 l, r",l, r)
#                     nowMul = nowMul / nums[l]
#                     if nowMul > MaxMul:
#                         MaxMul = nowMul
#                         Maxl,Maxr = (l+1),r

#                 if calAns :
#                     break

#                 # reset 
#                 l = r + 1
#                 print("l :",l )
#                 print("nowMul reset")
#                 nowMul = 1
#                 nowPos = True

#             if nums[r] == 0 :
#                 metZero = True
#                 if 0 > MaxMul :
#                     MaxMul = 0
                    
#             if calAns == False :
#                 nowMul = nums[r] * nowMul
                

#             r = r + 1

#         return Maxl, Maxr, MaxMul



s = Solution()
# print(s.maxProduct([2,3,0,4]))
print(s.maxProduct([2,3,0,-2,4,-2]))
# print(s.maxProduct([-2]))