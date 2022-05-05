# leetcode 的某一題
# 計算對稱括號的分數
# (XX) 把 XX 計算出來的分數*2
# XX + XX 把兩個 XX 的分數相加
# () 這樣算一分

# stack 比較快
def dp(s):
    stack = []

    for c in s :
        if c == "(" :
            stack.append("(")
        else :
            total_score = 0
            while True :
                top = stack.pop()
                if top != "(" :
                    total_score += top
                else :
                    break
            if total_score == 0 :
                stack.append(1)
            else :
                stack.append(2*total_score)
            
    return sum(stack)

# 使用 recursive
# def dp(s):
#     score = 0
#     l = 0
#     r = 0
#     p_count = 0
#     while r < len(s):
#         if s[r] == "(" :
#             p_count += 1
#         else:
#             p_count -= 1

#         if p_count == 0:
#             if r - l == 1 :
#                 score += 1
#             else :
#                 score += 2*dp(s[l+1:r])
#             l = r+1
#         r += 1
#     return score

print(dp("()"))
print(dp("()()"))
print(dp("(())"))
# print(dp("()()()"))
# print(dp("((()))"))
# print(dp("((())())"))
