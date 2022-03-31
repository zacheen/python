# 不能跑
# my Runtime: 808 ms, faster than 72.01% of Python3
class TimeMap:
    def __init__(self):
        self.mem = {}
    def set(self, key, value, timestamp):
        ret = self.mem.get(key ,None)
        if ret==None :
            self.mem[key] = [(value, timestamp)]
        else :
            insort_right(self.mem[key], (value, timestamp), key = lambda x : x[1])
    def get(self, key, timestamp):
        # print("in get self.mem :",self.mem)
        ret = self.mem.get(key ,None)
        if ret != None :
            # print(ret)
            find_indx = bisect_left(ret, timestamp, key = lambda x : x[1])
            if find_indx >= len(ret) :
                return ret[-1][0]
            else :
                if ret[find_indx][1] == timestamp :
                    return ret[find_indx][0]       
                else :
                    after_indx = find_indx-1
                    if after_indx >= 0 :
                        return ret[find_indx-1][0]
                    else :
                        return ""
        else :
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# given ans
class TimeMap:
    def __init__(self):
        self.values = defaultdict(list)
        self.timestamps = defaultdict(list)

    # 他沒有說 set 的 timestamp 會按照順序阿...
    def set(self, key, value, timestamp):
        self.values[key].append(value)
        self.timestamps[key].append(timestamp)

    def get(self, key, timestamp):
        if key not in self.timestamps:
            return ''
        # 反正不管怎樣就是取超出的位置 再-1就好
        i = bisect.bisect(self.timestamps[key], timestamp)
        return self.values[key][i - 1] if i > 0 else ''

s = Solution()
print(s.())

