# my 
class Solution:
    def minNumber(self, nums1, nums2):
        set_nums1 = set(nums1)
        
        same_item = []
        for n in nums2 :
            if n in set_nums1 :
                same_item.append(n)
                
        if same_item :
            return min(same_item)
        
        min_num1 = min(nums1)
        min_num2 = min(nums2)
        
        if min_num1 < min_num2 :
            return min_num1 * 10 + min_num2
        else :
            return min_num2 * 10 + min_num1

# given ans
# 想法概念差不多
# 不過我上面的找相同項目，幾乎其他人都用雙重 for 迴圈
    # 因為個數其實也才 10 個，說不定還比較快
    # 然後下面的找 min 也不用再找了

# 使用 given ans 概念改寫
class Solution:
    def minNumber(self, nums1, nums2):
        nums1.sort()
        for n1 in nums1 :
            if n1 in nums2 :
                return n1
        
        min_num1 = nums1[0]
        min_num2 = min(nums2)
        
        if min_num1 < min_num2 :
            return min_num1 * 10 + min_num2
        else :
            return min_num2 * 10 + min_num1

s = Solution()
print(s.minNumber(nums1 = [4,1,3], nums2 = [5,7]))
print(s.minNumber(nums1 = [3,5,2,6], nums2 = [3,1,7]))



