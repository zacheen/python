# my fail
# class Solution:
#     def removeDuplicateLetters(self, s):
#         from collections import Counter
#         all_counter = Counter(s)
#         print(all_counter)

#         all_counter_len = len(all_counter)
        
#         right = 0
#         left = 0
#         ans = ""
#         # min_right = 0
#         # min_left = 0
#         # min_len = 10001
#         # min_ans = None

#         lr_counter = Counter()

#         while right < len(s) :
#             if lr_counter[s[right]] == 0 :
#                 ans = ans + s[right]
#                 # min_ans = ans
#             else :
#                 # 移除新進的字 並加到最後面
#                 temp_ans = ans.replace(s[right], "")
#                 temp_ans = temp_ans + s[right]

#                 # 判斷 大小
#                 print("temp_ans < ans :", temp_ans < ans, temp_ans , ans)
#                 if temp_ans < ans :
#                     ans = temp_ans
                
#             lr_counter[s[right]] = lr_counter[s[right]] + 1
#             print("right :", ans, right)
#             right += 1

#         return ans

# given ans 
class Solution:
    def removeDuplicateLetters(self, s) :
        # 紀錄每個重復的字母 最後的位置
        last = {c: i  for i, c in enumerate(s)}
        print(last)

        stack = []
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                # 如果 stack 裡面有東西 && 這個字母小於目前stack最尾端的字 
                # && 目前stack最尾端的字母後面還有其他位置可以擺放
                while stack and c < stack[-1] and i < last[stack[-1]]:
                    seen.remove(stack.pop())
                    print("remove :",stack)
                seen.add(c)
                stack.append(c)
                print(stack)
        return ''.join(stack)
        
s = Solution()
# print(s.removeDuplicateLetters("cbacdcbc"))
# print(s.removeDuplicateLetters("bcacb"))
print(s.removeDuplicateLetters("bcab"))
