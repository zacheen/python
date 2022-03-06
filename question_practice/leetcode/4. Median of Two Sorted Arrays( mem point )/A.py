class Solution:
    def calAns(self, nums1, nums2, num1Count: int, num2Count: int, firstval: int, have2: bool) :
        if have2 :
            return (firstval + self.findnext(nums1,nums2,num1Count,num2Count))/2
        else :
            return firstval
                
    def findnext(self, nums1, nums2, num1Count: int, num2Count: int) :
        try :
            one = nums1[num1Count]
        except Exception :
            return nums2[num2Count]
        
        try :
            two = nums2[num2Count]
        except Exception :
            return nums1[num1Count]
        
        if one > two :
            return two
        else :
            return one
    
    def findMedianSortedArrays(self, nums1, nums2):
        # 方法 1 
        # 不好 因為兩個array已經排序好了
#         allList = nums1+nums2
#         allList.sort()
#         listLen = len(allList)
        
#         if listLen % 2 == 0:
#             midPos = int((listLen)/2)
#             return (allList[midPos-1]+allList[midPos])/2
#         else :
#             midPos = int((listLen-1)/2)
#             # print(midPos)
#             return allList[midPos]
        
        # 方法2 用兩個count紀錄現在到第幾個
        totallen = len(nums1) + len(nums2)
        midPos1 = -1
        have2 = False
        if totallen % 2 == 0:
            midPos1 = int((totallen)/2)
            have2 = True
        else :
            midPos1 = int((totallen+1)/2)
        print("midPos1 :",midPos1)
        
        num1Count = 0
        num2Count = 0
        count = 0
        lastNum = 0
        
        while True :
            count = count + 1 # base 1
            
            if num2Count >= len(nums2) :
                # arr 2 到底了
                lastNum = nums1[num1Count]
                num1Count = num1Count +1
            elif num1Count >= len(nums1) or nums1[num1Count] > nums2[num2Count] :
                # arr 1 到底了
                lastNum = nums2[num2Count]
                num2Count = num2Count +1
            else :
                lastNum = nums1[num1Count]
                num1Count = num1Count +1 
            
            if count == midPos1 :
                return self.calAns(nums1, nums2, num1Count, num2Count, lastNum, have2)

s = Solution()
print(s.findMedianSortedArrays([1,3], [2,7]))