MAX_n = 10
MAX_PICK = 5
MOD = 10**9+7
# MOD 要是比 MAX_n 大的質數 !!

# method 1 #########################################################
# 適合稀疏取用
class Factorial:
    def __init__(self, N, MOD) -> None:
        N += 1
        self.MOD = MOD
        self.fact = [1]*N      # mul from 1 to i
        self.invfact = [1]*N   
        for i in range(1, N):
            self.fact[i] = self.fact[i - 1] * i % self.MOD
        self.invfact[-1] = pow(self.fact[-1], MOD - 2, MOD)
        for i in range(N - 2, -1, -1):
            self.invfact[i] = self.invfact[i + 1] * (i + 1) % self.MOD

    def fac(self, n):
        return self.fact[n]

    def fac_inv(self, n):
        return self.invfact[n]

    def combi(self, n, m):
        if m < 0 or n < m: return 0
        return self.fact[n] * self.invfact[m] % self.MOD * self.invfact[n - m] % self.MOD

    def permu(self, n, m):
        if m < 0 or n < m: return 0
        return self.fact[n] * self.invfact[n - m] % self.MOD

    def catalan(self, n):
        return (self.combi(2 * n, n) - self.combi(2 * n, n - 1)) % self.MOD

    def inv(self, n):
        return self.fact[n-1] * self.invfact[n] % self.MOD

# print(Factorial(MAX_n, MOD).combi(9, 3)) 
# print(Factorial(MAX_n, 19).combi(9, 3))
# print(Factorial(MAX_n, 5).combi(9, 3)) # Wrong : 5 is smaller than MAX_n

# method 2 #########################################################
# 適合緊密取用
n = MAX_n
k = MAX_PICK # 最多從全部的項目中娶幾個(如果不知道可以直接帶n)
combi = [[0] * (k + 1) for i in range(n + 1)]
for i in range(n + 1):
    combi[i][0] = 1
    for j in range(1, min(i, k) + 1):
        combi[i][j] = (combi[i - 1][j - 1] + combi[i - 1][j]) % MOD

# # test same ########################################################
# fact = Factorial(MAX_n, MOD)
# for from_total in range(MAX_n) :
#     for pick_n in range(MAX_PICK) :
#         if combi[from_total][pick_n] != fact.combi(from_total, pick_n) :
#             print("not the same :",combi[from_total][pick_n], fact.combi(from_total, pick_n))
# print("finish")
