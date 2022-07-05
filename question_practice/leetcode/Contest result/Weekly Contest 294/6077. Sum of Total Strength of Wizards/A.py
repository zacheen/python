# my 
class Solution:
    def totalStrength(self, strength):
        # 從頭到此index的累計
        sum_acc = [0]
        now_sum = 0
        for n in strength :
            now_sum += n
            now_sum = now_sum % 1000000007
            sum_acc.append(now_sum)
        # print(sum_acc)
        
        def get_sum(l,r) :
            sub = sum_acc[l] - sum_acc[r]
            if sub < 0 :
                return sub + 1000000007
            else :
                return sub
        
        # min_lr[l][r] 從 index l 到 index r(包含) 的最小值
        min_lr = [[0]*(len(strength)+1) for _ in range(len(strength)+1)]
        for i in range(len(strength)) :
            min_lr[i][i] = strength[i]
            
        # 原因應該是因為我不知道 找各段區間 min 的演算法
        for l in range(0, len(strength)-1) :
            for i in range(0, len(strength)-l-1) :
                # print(i, i+l+1, " || ", i, i+l, " || ", i+l)
                index1 = i+l
                index2 = index1+1 
                min_lr[i][index2] = min(min_lr[i][index1],strength[index2])
            # print("-----")
        
        # print(min_lr)
        # min_lr[i][i+1] = min(min_lr[i][i],strength[i])
        # min_lr[i][i+2] = min(min_lr[i][i+1],strength[i+1])
        # min_lr[i][i+l+1] = min(min_lr[i][i+l],strength[i+l]) 
        
        ans = 0
        for i in range(len(strength)) :
            for ii in range(i+1,len(strength)+1) :  # ii 位置不包含
                ans += get_sum(ii,i) * min_lr[i][ii-1]
                ans = ans % 1000000007
        return ans

# given ans
class Solution:
    def totalStrength(self, strength):
        MOD = 1000000007
        ans = 0

        n = len(strength)
        pL = [0]*n
        pR = [0]*n
        sum1 = [0]*(n+1)
        sum2 = [0]*(n+1)

        for i in range(n) :
            sum1[i+1] = (sum1[i] + strength[i]) % MOD
            sum2[i+1] = (sum1[i] + i * strength[i]) % MOD
            pL[i] = i-1
            while pL[i] >= 0 and strength[pL[i]] >= strength[i] :
                pL[i] = pL[pL[i]]
        print(pL) # pL 是往右看比此位置大的位置

        for i in range(n-1,-1,-1) :
            pR[i] = i+1
            while pR[i] < 0 and strength[pR[i]] > strength[i] :
                pR[i] = pR[pR[i]]
            sL = ((sum2[i + 1] - sum2[pL[i] + 1]) - pL[i] * (sum1[i + 1] - sum1[pL[i] + 1])) % MOD
            sR = (pR[i] * (sum1[pR[i]] - sum1[i + 1]) - (sum2[pR[i]] - sum2[i + 1])) % MOD
            prd = (sL * (pR[i] - i) + (i - pL[i]) * sR) % MOD
            ans = (ans + prd * strength[i]) % MOD
        
        if ans < 0 :
            return ans + MOD
        else :
            return ans

s = Solution()
print(s.totalStrength([1,3,1,2])) # 44
# print(s.totalStrength([1,2,3,4]))
# print(s.totalStrength([4,3,2,1]))
# print(s.totalStrength([1,2,1,2,1,2]))


