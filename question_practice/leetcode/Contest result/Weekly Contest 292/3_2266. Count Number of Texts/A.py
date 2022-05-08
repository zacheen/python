# 一次 送出失敗
    # 忘了關output
# 二次 送出失敗
    # comb_num 的結果沒有 % 1000000007

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

# given ans 2
# 優雅
# class Solution {
# public:
#     int countTexts(string s) {
#         const int mod = 1e9 + 7;
#         vector<int> c(10, 3);
#         c[7] = c[9] = 4;
#         long long ans = 1;
#         for(int i = 0, j = 0; i < s.size(); i = j) {
#             while(j < s.size() && s[i] == s[j]) ++j;
#             int x = s[i] - '0', cnt = j - i;
#             vector<long long> s(cnt + 1);
#             s[0] = 1;
#             for(int i = 1; i <= cnt; ++i) {
#                 for(int j = 1; j <= c[x]; ++j) {
#                     if(i - j >= 0) s[i] = (s[i] + s[i - j]) % mod;
#                 }
#             }
#             ans = ans * s[cnt] % mod;
#         }
#         ans %= mod;
#         return ans;
#     }
# };

# given ans
# 有些人是一個字進來就處理一個字
# 如果跟前一個字一樣
    # 加上前一格的組合
# 如果跟再前面一個字一樣
    # 再加上前兩格的組合
# ... 



s = Solution()
print(s.countTexts("22233")) # 8
print(s.countTexts("222222222222222222222222222222222222")) # 82876089



