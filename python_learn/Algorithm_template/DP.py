
# 如果交換位置算多一種答案的話
def dp_can_change(amount, coins):
    dp = [1]+[0]*(amount)
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i :
                dp[i] += dp[i - coin]

    # print("dp_can_change",dp)
    return dp[amount]

# print(dp_can_change(5,[1,2,5]))
# print(dp_can_change(5,[2]))
# print(dp_can_change(5,[5]))
# print(dp_can_change(32,[1,2,4,8,16]))

# 其實就是兩個for迴圈換位置
# 如果交換位置不算多一種答案的話
def dp_cant_change(amount, coins):
    dp = [1]+[0]*(amount)
    for coin in coins:
        for i in range(coin, amount + 1):  #記得要從 coin 開始for
            dp[i] += dp[i - coin]

    # print("dp_cant_change",dp)
    return dp[amount]

# print(dp_cant_change(5,[1,2,5]))
# print(dp_cant_change(5,[2]))
# print(dp_cant_change(5,[5]))
# print(dp_cant_change(32,[1,2,4,8,16]))

# 優化 ############################
# dp = [0]*(amount+1)
# for a in coins :
#     dp[a] = 1
# 可以優化成
# dp = [1]+[0]*(amount)