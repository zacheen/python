class Solution:
    def invalidTransactions(self, transactions):
        from collections import Counter
        coun = Counter(transactions)
        
        transactions_reg = []
        for each in coun :
            info = each.split(",")
            info[1] = int(info[1])
            info[2] = int(info[2])
            transactions_reg.append(info)

        # print(transactions_reg)
        
        invalid = []
        # writeInCache = {}
        def getKey (record):
            record[1] = str(record[1])
            record[2] = str(record[2])
            return ",".join(record)
        
        # 有 Counter 的 writein
        # Counter 歸0 代表有寫過
        def writein (record):
            key = getKey(record.copy())
            for i in range(coun[key]) :
                invalid.append(key)
            coun[key] = 0
            return 
        # def writein (record):
        #     key = getKey(record.copy())
        #     print("writein :",key)
        #     getwritein = writeInCache.get(key, None)
        #     if getwritein == None :
        #         invalid.append(key)
        #         writeInCache[key] = True
        #     return

        
        his = {}
        for each in transactions_reg :
            if each[2] > 1000 :
                writein(each)

            getHis = his.get(each[0], None)
            if getHis == None :
                his[each[0]] = [each]
            else :
                # print("his : ",getHis)
                for eachHis in getHis :
                    if eachHis[3] != each[3] and abs(eachHis[1]-each[1]) <= 60 :
                        writein(eachHis)
                        writein(each)
                his[each[0]].append(each)

        return invalid

            
s = Solution()
print(s.invalidTransactions(
    ["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"]))
# ["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"]
#
# my_out = s.invalidTransactions(
#     ["bob,55,173,barcelona","lee,113,952,zurich","maybe,115,1973,madrid","chalicefy,229,283,istanbul","bob,24,874,shanghai","alex,568,412,tokyo","alex,242,1710,milan","iris,722,879,shenzhen","chalicefy,281,1586,warsaw","maybe,246,778,bangkok","xnova,605,166,newdelhi","iris,631,991,hongkong","chalicefy,500,620,tokyo","chalicefy,380,428,istanbul","iris,905,180,barcelona","alex,810,732,shenzhen","iris,689,389,paris","xnova,475,298,singapore","lee,58,709,amsterdam","xnova,717,546,guangzhou","maybe,78,435,shenzhen","maybe,333,145,hongkong","lee,405,1230,hongkong","lee,456,1440,tokyo","chalicefy,286,1071,amsterdam","alex,55,271,shanghai","bob,91,273,warsaw","iris,195,1825,tokyo","maybe,639,417,madrid","maybe,305,882,chicago","lee,443,47,chicago","chalicefy,958,840,budapest","lee,162,1239,budapest","bob,701,505,montreal","alex,52,1575,munich","bob,533,1407,amsterdam","lee,621,491,tokyo","chalicefy,866,622,rome","alex,925,455,hongkong","lee,968,164,moscow","chalicefy,31,1119,newdelhi","iris,527,700,warsaw","bob,286,1694,dubai","maybe,903,29,barcelona","maybe,474,1606,prague","maybe,851,648,beijing","lee,48,655,chicago","maybe,378,25,toronto","lee,922,691,munich","maybe,411,903,taipei","lee,651,112,guangzhou","lee,664,506,dubai","chalicefy,704,924,milan","maybe,333,1264,budapest","chalicefy,587,1112,singapore","maybe,428,437,moscow","lee,721,366,newdelhi","iris,824,1962,beijing","chalicefy,834,489,istanbul","alex,639,1473,zurich","xnova,898,738,tokyo","chalicefy,585,1313,frankfurt","xnova,730,759,beijing","alex,69,892,montreal","lee,77,91,barcelona","lee,722,611,taipei","chalicefy,706,1982,jakarta","chalicefy,743,584,luxembourg","xnova,683,322,istanbul","chalicefy,60,861,prague","alex,366,871,shenzhen","chalicefy,77,870,shenzhen","iris,913,1501,warsaw","iris,846,1176,warsaw","bob,873,69,zurich","alex,601,181,chicago","chalicefy,118,145,hongkong","bob,879,982,montreal","lee,994,950,chicago","maybe,885,1900,shanghai","lee,717,1447,shanghai","chalicefy,71,434,istanbul","bob,870,968,toronto","maybe,718,51,beijing","alex,669,896,istanbul","chalicefy,639,506,rome","alex,594,934,frankfurt","maybe,3,89,jakarta","xnova,328,1710,rome","alex,611,571,chicago","chalicefy,31,458,montreal","iris,973,696,toronto","iris,863,148,rome","chalicefy,926,511,warsaw","alex,218,1411,zurich","chalicefy,544,1296,shenzhen","iris,27,23,montreal","chalicefy,295,263,prague","maybe,575,31,munich","alex,215,174,prague"])
# my_out.sort()
# expect = ["bob,55,173,barcelona","lee,113,952,zurich","maybe,115,1973,madrid","chalicefy,229,283,istanbul","bob,24,874,shanghai","alex,568,412,tokyo","alex,242,1710,milan","iris,722,879,shenzhen","chalicefy,281,1586,warsaw","maybe,246,778,bangkok","iris,631,991,hongkong","chalicefy,500,620,tokyo","iris,905,180,barcelona","iris,689,389,paris","lee,58,709,amsterdam","xnova,717,546,guangzhou","maybe,78,435,shenzhen","maybe,333,145,hongkong","lee,405,1230,hongkong","lee,456,1440,tokyo","chalicefy,286,1071,amsterdam","alex,55,271,shanghai","bob,91,273,warsaw","iris,195,1825,tokyo","maybe,305,882,chicago","lee,443,47,chicago","chalicefy,958,840,budapest","lee,162,1239,budapest","alex,52,1575,munich","bob,533,1407,amsterdam","lee,621,491,tokyo","chalicefy,866,622,rome","lee,968,164,moscow","chalicefy,31,1119,newdelhi","bob,286,1694,dubai","maybe,903,29,barcelona","maybe,474,1606,prague","maybe,851,648,beijing","lee,48,655,chicago","maybe,378,25,toronto","lee,922,691,munich","maybe,411,903,taipei","lee,651,112,guangzhou","lee,664,506,dubai","chalicefy,704,924,milan","maybe,333,1264,budapest","chalicefy,587,1112,singapore","maybe,428,437,moscow","lee,721,366,newdelhi","iris,824,1962,beijing","chalicefy,834,489,istanbul","alex,639,1473,zurich","chalicefy,585,1313,frankfurt","xnova,730,759,beijing","alex,69,892,montreal","lee,77,91,barcelona","lee,722,611,taipei","chalicefy,706,1982,jakarta","chalicefy,743,584,luxembourg","xnova,683,322,istanbul","chalicefy,60,861,prague","chalicefy,77,870,shenzhen","iris,913,1501,warsaw","iris,846,1176,warsaw","bob,873,69,zurich","alex,601,181,chicago","chalicefy,118,145,hongkong","bob,879,982,montreal","lee,994,950,chicago","maybe,885,1900,shanghai","lee,717,1447,shanghai","chalicefy,71,434,istanbul","bob,870,968,toronto","alex,669,896,istanbul","chalicefy,639,506,rome","alex,594,934,frankfurt","xnova,328,1710,rome","alex,611,571,chicago","chalicefy,31,458,montreal","iris,973,696,toronto","iris,863,148,rome","chalicefy,926,511,warsaw","alex,218,1411,zurich","chalicefy,544,1296,shenzhen","chalicefy,295,263,prague","alex,215,174,prague"]
# expect.sort()
# print(my_out)
# print(expect)

# print(s.invalidTransactions(
# ["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]))
# ["bob,689,1910,barcelona","bob,832,1726,barcelona","bob,820,596,bangkok"]


# print(s.invalidTransactions(["alice,20,800,mtv","bob,50,1200,mtv"]))
# print(s.invalidTransactions(["alice,50,1200,mtv"]))
