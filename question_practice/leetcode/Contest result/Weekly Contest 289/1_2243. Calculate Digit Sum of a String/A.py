# my Runtime: 31 ms, faster than 100.00% of Python3
class Solution:
    def digitSum(self, s, k):
        while len(s) > k :
            new_s = ""
            total = 0
            for i in range(len(s)) :
                total += int(s[i])
                if i % k == k-1 :
                    new_s += str(total)
                    total = 0
                    
            if len(s) % k != 0 :
                new_s += str(total)
            
            # print(new_s)
            s = new_s
            
        return s

# given ans 跟其他答案概念差不多

# given ans 有用recursive解的 想法很特別
# class Solution:
#     def digitSum(self, s, k):
#         if len(s) <= k:
#             return s
#         t = ''
#         for i in range(0, len(s), k):
#             r = 0
#             for j in s[i:i+k]:
#                 r += int(j)
#             t += str(r)
#         return self.digitSum(t, k)

s = Solution()
print(s.digitSum(s = "11111222223", k = 3))
print(s.digitSum(s = "00000000", k = 3))



