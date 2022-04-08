# my Runtime: 28 ms, faster than 95.71% of Python3
class Solution:
    def letterCombinations(self, digits):
        # corner case
        if digits == "" :
            return []
        
        ans = []
        c_list = [[],[],["a","b","c"],["d","e","f"],
                  ["g","h","i"],["j","k","l"],["m","n","o"],
                  ["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
        def recur(digits, now_str) :
            if digits == "" :
                ans.append(now_str)
                return 
            for c in c_list[int(digits[0])]:
                recur(digits[1:], now_str+c)
            return 
        recur(digits, "")
        return ans

# given ans 想法差不多

s = Solution()
print(s.letterCombinations(digits = "23"))
print(s.letterCombinations(digits = ""))



