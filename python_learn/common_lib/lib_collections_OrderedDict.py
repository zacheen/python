from collections import OrderedDict
# 這裡的 order 不是指數值大小的 order 是指 加入時的順序 order

ll = [11,1,3,3,5,10,11,4,6,1,]
orderedDict = OrderedDict.fromkeys(ll)
print(list(orderedDict))

# 但是我正常使用普通的dict 還不知道什麼操作會改變dict印出來的順序
# Python3.6 中有所改變。內置的 dict 類現在也保持其項目的有序性
# 但 Python3.6 只是提出想法並沒有保證，Python3.7 之後有保證順序
# 但是看起來仍然有 OrderedDict 存在的價值 https://www.gairuo.com/p/python-ordered-dict
ll = [11,1,3,3,5,10,11,4,6,1,]
normal_dict = dict.fromkeys(ll)
print(list(normal_dict))

