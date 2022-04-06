# my 
# class Solution:
#     def convertTime(self, current, correct):
#         cur_t = int(current[:2])*60 + int(current[-2:])
#         cor_t = int(correct[:2])*60 + int(correct[-2:])
#         sub_time = cor_t - cur_t
#         # print(sub_time)
        
#         ans = 0
#         for sub in [60,15,5,1] :
#             while sub_time >= sub :
#                 sub_time -= sub
#                 ans += 1
#         return ans

# given ans
# 概念差不多 只是有優化
# 找兩個時間用 .split(':') -> 就算格式不對也可以跑
# for 迴圈裡面沒有 while  直接除找這個跨度要調整幾次
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def f(x):
            a, b = map(int, x.split(':'))
            return a*60+b
        s = f(correct)-f(current)
        ans = 0
        for i in [60, 15, 5, 1]:
            x = s//i
            s %= i
            ans += x
        return ans

s = Solution()
print(s.convertTime(current = "02:30", correct = "04:35"))
print(s.convertTime(current = "11:00", correct = "11:01"))


