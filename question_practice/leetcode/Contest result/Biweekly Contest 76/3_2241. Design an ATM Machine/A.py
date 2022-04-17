# my 
# class ATM:
#     def __init__(self):
#         self.mem = [0,0,0,0,0]

#     def deposit(self, banknotesCount):
#         for i in range(5):
#             self.mem[i] += banknotesCount[i]
#         # print(self.mem)
#         return

#     def withdraw(self, amount):
#         cash = [20,50,100,200,500]
#         take_cash = [0,0,0,0,0]
        
#         for i in range(4,-1,-1) :
#             if amount >= cash[i] :
#                 # print(amount , cash[i] , self.mem[i])  # 又忘了關output一次...
#                 num = amount//cash[i]
#                 if self.mem[i] > num :
#                     take_cash[i] += num
#                     self.mem[i] -= num
#                     amount -= cash[i]*num
#                 else :
#                     take_cash[i] += self.mem[i]
#                     amount -= cash[i]*self.mem[i]
#                     self.mem[i] = 0
#         if amount == 0:
#             # print(self.mem)
#             return take_cash
#         else :
#             self.deposit(take_cash)
#             return [-1]
            
# 使用 given ans 優化
# Runtime: 719 ms, faster than 83.33% of Python3
class ATM:
    def __init__(self):
        # self.mem = [0,0,0,0,0]
        # 優化
        self.mem = [0]*5

    def deposit(self, banknotesCount):
        for i in range(5):
            self.mem[i] += banknotesCount[i]
        # print(self.mem)
        return

    cash = [20,50,100,200,500]
    def withdraw(self, amount):
        take_cash = [0,0,0,0,0]
        
        for i in range(4,-1,-1) :
            # if amount >= cash[i] :
                # num = amount//cash[i]
                # if self.mem[i] > num :
                #     take_cash[i] += num
                #     self.mem[i] -= num
                #     amount -= cash[i]*num
                # else :
                #     take_cash[i] += self.mem[i]
                #     amount -= cash[i]*self.mem[i]
                #     self.mem[i] = 0
                # 優化 用 min
            num = min(amount//ATM.cash[i], self.mem[i])
            take_cash[i] = num
            # self.mem[i] -= num
            amount -= ATM.cash[i]*num

        if amount == 0:
            # print(self.mem)
            # 優化 因為用了min 所以可以取出的時候再扣款
            self.deposit([-x for x in take_cash])
            return take_cash
        else :
            # self.deposit(take_cash)
            return [-1]


