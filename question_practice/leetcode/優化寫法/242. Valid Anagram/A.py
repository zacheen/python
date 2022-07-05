# my v1 59 ms
# class Solution:
#     def isAnagram(self, s, t):
#         s_count = Counter(s)
#         t_count = Counter(t)
        
#         if len(s_count) != len(t_count) :
#             return False
        
#         for c, n in s_count.items() :
#             if t_count[c] != n :
#                 return False
#         return True

# My v2 Runtime: 55 ms, faster than 75.87% of Python3
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t) :
            return False    
    
        s_count = Counter(s)
        for c in t :
            s_count[c] -= 1
            if s_count[c] < 0 :
                return False
        return True

# given ans 跟 v2 一樣

s = Solution()
print(s.isAnagram())



