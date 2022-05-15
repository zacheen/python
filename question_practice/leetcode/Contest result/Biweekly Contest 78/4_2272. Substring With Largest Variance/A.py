# kadanes algo
# given ans
class Solution:
    def largestVariance(self, s):
        res = 0
        chars = list(set(s))
		
		# Loop through each pari of (c1, c2)
        for i in range(len(chars)):
            for j in range(i+1, len(chars)):
                c1, c2 = chars[i], chars[j]
				
				# keep track of count(c1) - count(c2) 
                diff = 0 
				
				# max and min of diff
				# result should be maximum of (diff - min_diff, max_diff - diff)
				# e.g. "baabaa", at index = 0, min_diff = -1. when index = 5, diff = 4 - 2 = 2, result = diff - min_diff = 2 - (-1) = 3
                max_diff = min_diff = 0
				
				# diff at the previous occurance of c1/c2
                last_c1_diff = last_c2_diff = 0 
				
				# check wether we have met c1/c2 during the loop
                meet_c1 = meet_c2 = False
				
                for c in s:
                    if c == c1:
                        meet_c1 = True
                        diff += 1
						
						#  use last_c1_diff instead of diff because we have to make sure that c1 is in the rest part of the substring. 
						# e.g. [c1, c1, c2, c2, c2]
						# At index = 1, if we use diff = 2 -> max_diff = 2
						# At index = 4, diff = 2 - 3 = -1, result = max_diff - diff = 3. 
						# Though we have [c2, c2, c2] as a substring, c1 is not in this string and the result is invalid
                        # 題目規定 substring 中一定要有兩種以上的字母
                        max_diff = max(last_c1_diff, max_diff)  # 紀錄從前面數過來(也可以說是某個區間) c2 最多比 c1 多幾個 
						
                        last_c1_diff = diff  
                    elif c == c2:
                        meet_c2 = True
                        diff -= 1
                        min_diff = min(last_c2_diff, min_diff)
                        last_c2_diff = diff  
                    else:
                        continue
					
					# update the result only when we have met both c1 and c2 
                    if meet_c1 and meet_c2:
                        res = max(diff - min_diff, max_diff - diff, res)
                        # max (c1>c2的情況, c2>c1的情況, 其他字母最大的情況) 
                        # c1>c2的情況 = c2最多比c1多幾個 - c1最多比c2多幾個 (推理過這兩個區間不會重疊)
        return res

# given ans Time Limit Exceeded
# 感覺跟上面的時間度沒差很多啊 ? 少一半 
# class Solution:
#     def largestVariance(self, s):
#         ans = 0
#         a_start = ord("a")
#         st = [chr(i) for i in range(a_start, a_start+26)]#set(s)
#         for x in st :
#             for y in st :
#                 if x != y :                                             
#                     can, have = False, False
#                     diff = 0
#                     for ch in s :
#                         if ch == y:
#                             diff += 1
#                         elif ch == x:
#                             if diff>0 :
#                                 can = True
#                             have = True
#                             diff -= 1

#                         if diff < 0 :
#                             diff = 0
#                             can = False
                        
#                         if have :
#                             if can :
#                                 ans = max(ans, diff)
#                             else :
#                                 ans = max(ans, diff-1)
#         return ans


s = Solution()
print(s.largestVariance(s = "aababbb"))
print(s.largestVariance(s = "abcde"))



