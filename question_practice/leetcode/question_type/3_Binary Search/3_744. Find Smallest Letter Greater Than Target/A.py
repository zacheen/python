# my v1 Runtime: 164 ms, faster than 41.64% of Python3
# class Solution:
#     def nextGreatestLetter(self, letters, target):
#         # 處理 corner case
#         if letters[0] > target or letters[-1] <= target:
#             return letters[0]

#         l,r = 0, len(letters)-1
#         while l < r-1 :
#             mid = (l+r)//2
#             # print(l,mid,r, letters[mid] , target)
#             if letters[mid] <= target :
#                 l = mid 
#             else :
#                 r = mid
        
#         return letters[r]

# My v2 仔細思考範圍與判斷式
# Runtime: 127 ms, faster than 69.98% of Python3
# Runtime: 150 ms, faster than 51.92% of Python3
class Solution:
    def nextGreatestLetter(self, letters, target):
        # 處理 corner case
        if letters[0] > target or letters[-1] <= target:
            return letters[0]

        l,r = 0, len(letters)
        while l < r :
            mid = (l+r)//2 # 改成 >> 1 # 速度差不多 # Runtime: 146 ms
            # print(l,mid,r, letters[mid] , target)
            if letters[mid] > target :
                r = mid
            else :
                l = mid + 1
        
        return letters[r]

s = Solution()

print(s.nextGreatestLetter(letters = ["a","c","e","f","j"], target = "b"))
print(s.nextGreatestLetter(letters = ["a","c","e","f","j"], target = "d")) 
print(s.nextGreatestLetter(letters = ["a","c","e","f","j"], target = "e")) 

# print(s.nextGreatestLetter(letters = ["c","e","f","j"], target = "a"))
# print(s.nextGreatestLetter(letters = ["c","e","f","j"], target = "z"))
