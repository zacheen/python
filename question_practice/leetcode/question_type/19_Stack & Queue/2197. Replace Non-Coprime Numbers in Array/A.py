# my Time Limit Exceeded
# [5,7,35] 這種 case 加入 35 有可能會影響到上兩位的
# 原因是因為合併後有 append 新的項目
class Solution:
    def replaceNonCoprimes(self, nums):
        def non_coprime(n1, n2) :
            for i in range(min(n1,n2), 1, -1) :
                if n1%i==0 and n2%i==0 :
                    return i
            return None
        
        stack = []
        for n in nums :
            stack.append(n)
            while len(stack)>=2 :
                ret = non_coprime(stack[-2], stack[-1])
                if ret :
                    temp = (stack[-2] * stack[-1]) // ret
                    stack.pop()
                    stack[-1] = temp
                else :
                    break
        return stack

# given ans
# 1.優化 stack 架構
# 2.使用內建lib找最大公因數
class Solution:
    def replaceNonCoprimes(self, nums):
        ans = []
        for num in nums:
            while ans and gcd(ans[-1], num) > 1:
                num = lcm(ans.pop(), num)
            ans.append(num)

        return ans

s = Solution()
# print(s.replaceNonCoprimes())
# print(s.replaceNonCoprimes())
# print(s.replaceNonCoprimes([517,11,121,517,3,51,3,1887,5]))
# print(s.replaceNonCoprimes([287,41,49,287,899,23,23,20677,5,825]))
print(s.replaceNonCoprimes([5,7,35]))



