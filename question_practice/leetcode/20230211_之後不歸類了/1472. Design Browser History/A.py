# my Beats 82.13%
class BrowserHistory:
    def __init__(self, homepage):
        self.mem = [homepage]
        self.indx = 0

    def visit(self, url):
        self.mem = self.mem[:self.indx+1] + [url]
        self.indx += 1
        # print("visit :",self.indx)
        # print("visit :",self.mem)

    def back(self, steps):
        self.indx = max((self.indx - steps), 0)
        # print("back : ",self.indx)
        return self.mem[self.indx]

    def forward(self, steps):
        self.indx = min((self.indx + steps), len(self.mem)-1 )
        return self.mem[self.indx]

# given ans
# 我的寫法比較簡潔

s = Solution()
# print(s.())



