# 981. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/description/

# my : 95ms
class TimeMap:
    def __init__(self):
        self.value = defaultdict(list)
        self.timestamp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.value[key].append(value)
        self.timestamp[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        all_timestamp = self.timestamp[key]
        if len(all_timestamp) == 0 :
            return ""

        l = 0
        r = len(all_timestamp)-1

        while l+1 < r :
            mid = (l+r) >> 1
            if all_timestamp[mid] < timestamp :
                l = mid
            else :
                r = mid

        # print(l,r, all_timestamp[l], all_timestamp[r], timestamp)
        if all_timestamp[r] <= timestamp :
            return self.value[key][r]
        elif all_timestamp[l] <= timestamp :
            return self.value[key][l]
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

