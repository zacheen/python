# my Runtime: 49 ms, faster than 97.84% of Python3
# class Solution:
#     def convert(self, s, numRows):
#         # corner case
#         if numRows == 1 :
#             return s
        
#         ans_list = [""]*numRows
#         i = 0
#         direct = 1
#         for c in s :
#             # print(i)
#             ans_list[i]+=c
#             i += direct

#             # given ans : 可以先判斷 再加減direct
#             if i == numRows :
#                 i = numRows-2
#                 direct = -1
#             if i == -1 :
#                 i = 1
#                 direct = 1

#         return "".join(ans_list)

# given ans
class Solution:
    def convert(self, s, numRows):
        rows = [''] * numRows
        k = 0
        direction = (numRows == 1) - 1

        for c in s:
            rows[k] += c
            if k == 0 or k == numRows - 1:
                direction *= -1
            k += direction

        return ''.join(rows)

s = Solution()
print(s.convert(s = "PAYPALISHIRING", numRows = 3)) # PAHNAPLSIIGYIR
print(s.convert(s = "PAYPALISHIRING", numRows = 4)) # PINALSIGYAHRPI



