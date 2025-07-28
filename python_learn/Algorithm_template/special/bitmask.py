# 線性基 (linear basis)
    # 功能
        # 可以求 某個數字是否能由其他數字組合而成
            # 因此當然也可以找出 最小能夠組成其他數字的數組
        # 可以求一個數組中 XOR 最大的組合方法
    # 可套用運算
        # +
        # -
        # XOR ^
class XorBasis:
    def __init__(self, n: int):
        self.b = [0] * (n.bit_length() + 1)
        # b[i] : 最高位i 代表的基

    def insert(self, x: int) -> None: # 回傳是否為新的項目
        b = self.b
        while x:
            i = x.bit_length()  # x 的最高位
            if b[i] == 0:       # x 和之前的基是線性無關的
                b[i] = x        # 新增一個基，最高位為 i
                return True
            x ^= b[i]           # 確保參與 max_xor 的基的最高位是互不相同的，方便我們貪心
        
        # 正常循環結束，此時 x=0，說明一開始的 x 可以被已有基表出，不是一個線性無關基
        return False

    def max_xor(self) -> int:
        res = 0
        # 從高到低貪心：越高的位，越必須是 1
        # 由於每個位的基至多一個，所以每個位只需考慮異或一個基，若能變大，則異或之
        for base_n in self.b[::-1]:
            if (new_res := res ^ base_n) > res:
                res = new_res
        return res