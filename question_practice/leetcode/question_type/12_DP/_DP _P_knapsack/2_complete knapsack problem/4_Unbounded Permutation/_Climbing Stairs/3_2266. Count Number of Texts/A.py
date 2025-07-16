# 2266. Count Number of Texts
# https://leetcode.com/problems/count-number-of-texts/

# my using template C_Knap_perm v2 : 291ms Beats75.28%
MOD = 1000000007
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n2l = {str(i) : 3 for i in range(2,9)}
        n2l["9"] = 4
        n2l["7"] = 4

        dp = [1]
        for i, p_k in enumerate(pressedKeys,1):
            cnt = dp[i-1] # 前面一個一定可以
            # 前面兩個就一定要 確定數字是否相同
            # n 是有幾個字母已經相同了
            for n in range(2, n2l[p_k]+1) : # nums 轉換成 range
                if (pre_i := i-n) >= 0 and p_k == pressedKeys[pre_i]:
                    cnt += dp[pre_i]
                else :
                    break
            dp.append(cnt % MOD)
        return dp[-1] % MOD
    
# my opt above : 185ms Beats84.27%
MOD = 1000000007
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n2l = {str(i) : 3 for i in range(2,9)}
        n2l["9"] = 4
        n2l["7"] = 4

        dp = [1]
        last_same_l = 0
        last_c = ""
        for i, p_k in enumerate(pressedKeys,1):
            if p_k == last_c :
                last_same_l += 1
                if last_same_l > n2l[p_k] :
                    last_same_l = n2l[p_k]
                dp.append( sum(dp[-last_same_l:]) % MOD )
            else :
                last_c = p_k
                last_same_l = 1
                dp.append(dp[-1])
        return dp[-1] % MOD

# my 
class Solution:
    def countTexts(self, pressedKeys):
        @cache
        def comb_num(num, max_num) :
            if num == 0:
                return 1
            if num == 1:
                return 1
            
            total = 0
            for i in range(1, min(num+1, max_num+1)):
                # print(num-i, comb_num(num-i, max_num))
                total += comb_num(num-i, max_num)
            return total % 1000000007
        
        c = [[pressedKeys[0],0]]
        for cha in pressedKeys :
            if cha == c[-1][0] :
                c[-1][1] += 1
            else :
                c.append([cha,1])
        # print(c)
        
        total_comb = 1
        for item, count in c:
            if item == "7" or item == "9":
                total_comb = total_comb * comb_num(count, 4)
            else :
                total_comb = total_comb * comb_num(count, 3)
            total_comb = total_comb % 1000000007
        return total_comb

s = Solution()
print(s.countTexts("22233")) # 8
print(s.countTexts("222222222222222222222222222222222222")) # 82876089



