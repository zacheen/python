# 744. Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

# my : 0ms
class Solution:
    def nextGreatestLetter(self, letters, target):
        left = 0
        right = len(letters)-1
        while left+1 < right :
            mid = (left+right) >> 1
            if letters[mid] <= target :
                left = mid
            else :
                right = mid
        
        if letters[left] > target :
            return letters[left]
        elif letters[right] > target :
            return letters[right]
        else :
            return letters[0]

s = Solution()

print(s.nextGreatestLetter(letters = ["a","c","e","f","j"], target = "b"))
print(s.nextGreatestLetter(letters = ["a","c","e","f","j"], target = "d")) 
print(s.nextGreatestLetter(letters = ["a","c","e","f","j"], target = "e")) 

# print(s.nextGreatestLetter(letters = ["c","e","f","j"], target = "a"))
# print(s.nextGreatestLetter(letters = ["c","e","f","j"], target = "z"))
