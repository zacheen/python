import bisect
class CountIntervals:
    
    def __init__(self):
        self.count_num = 0
        self.interval = []

    def add(self, left: int, right: int):
        if self.interval :
            ret = bisect.bisect_right(self.interval, (left, math.inf))
            ret = ret - 1
            # print("ret",ret, (left , right))
            
            # 我知道 self.count_num 的更新方式可以優化 
            # 不過為了看起來更簡單也比較不會出錯 比賽中才沒有優化
            front = self.interval[ret]
            if ret == -1 :
                # 直接插在最前面
                self.interval.insert(0, (left , right))
                self.count_num += right - left + 1
                ret = 0
            elif front[1] < right :
                if front[1] < left :
                    # 跟前面沒有重疊
                    self.interval.insert(ret+1, (left , right))
                    self.count_num += right - left + 1
                    ret = ret+1
                else :
                    # 有重疊
                    new_l = front[0]
                    # 先拿掉原本的
                    self.count_num -= (front[1] - front[0])
                    self.interval[ret] = (new_l , right)
                    self.count_num += (right - new_l)
            # else 完全包含 不需要做任何事
                    
            # 跟後面的合併
            # ret 已換到新的位置
            # print("after ret",ret, (left , right), len(self.interval))
            while ret+1 < len(self.interval) and self.interval[ret][1] >= self.interval[ret+1][0]:
                # 有重疊
                new_l = front[0]
                # 先拿掉原本的
                # print("1 :",self.count_num)
                self.count_num -= (self.interval[ret][1] - self.interval[ret][0] + 1)
                self.count_num -= (self.interval[ret+1][1] - self.interval[ret+1][0] + 1)
                # print("2 :",self.count_num)
                self.interval[ret] = (self.interval[ret][0], max(self.interval[ret+1][1], self.interval[ret][1]) )
                # print(self.interval, ret)
                self.count_num += (self.interval[ret][1] - self.interval[ret][0] + 1)
                # print("3 :",self.count_num)
                del(self.interval[ret+1])
            
        else :
            self.interval.append((left , right))
            self.count_num = right - left + 1
            
        return None

    def count(self):
        # print(self.interval)
        return self.count_num

# given ans
# 概念差不多 只是interval的融合 每個人使用的方法不同

obj = CountIntervals()
obj.add(2,3)
param_2 = obj.count()



