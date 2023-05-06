# 題目 : 
    # 從字串中按照順序抽取字母排列，且每個字母都要有
    # 排出最小的字串 "abc" < "acb"

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

# given ans Beats 87.13%
class Solution:
    def removeDuplicateLetters(self, s) :
        # 紀錄每個重復的字母 最後的位置
        last = {c: i  for i, c in enumerate(s)}
        print(last)

        stack = []
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                # 如果 stack 裡面有東西 
                # && 這個字母小於目前stack最尾端的字 
                # && 目前stack最尾端的字母後面還有其他位置可以擺放
                while stack and c < stack[-1] and i < last[stack[-1]]:
                    seen.remove(stack.pop())
                    print("remove :",stack)
                seen.add(c)
                stack.append(c)
                print(stack)
        return ''.join(stack)
    
# # 20230426 重新練習
# # 我會錯題目的意思... #我以為要找最短的包含全部字母的字串
# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         c = {}
#         max_key = 0
#         min_range = (0,0) # right include
#         l = 0
#         for right, ch in enumerate(s) :
#             if ch in c.keys() :
#                 c[ch]+=1
#                 while c[s[l]] > 1 :
#                     c[s[l]] -= 1
#                     l += 1
#                     if (min_range[1] - min_range[0]) > (right - l):
#                         min_range = (l, right)
#             else :
#                 max_key += 1
#                 c[ch] = 1
#                 min_range = (l, right)
#         # return "".join(set(s[min_range[0]: min_range[1]+1]))
#         return s[min_range[0]: min_range[1]+1]
        
s = Solution()
print(s.removeDuplicateLetters("cbacdcbc"))
print(s.removeDuplicateLetters("bcacb"))
print(s.removeDuplicateLetters("bcab"))
