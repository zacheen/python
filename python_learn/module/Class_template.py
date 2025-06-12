class Class_template:
    static_int = 0
    
    def __init__(self, n):
        self.self_int = n
        pass
    
    # 比較
    def __lt__(self, other): # 如果要創建給 heap 的 class 只需要這個
        return self.self_int < other.self_int
    
    def __le__(self, other):
        return self.self_int <= other.self_int

    def __eq__(self, other):
        return self.self_int == other.self_int


    def __repr__(self):
        # print 的時候會呼叫此 function
        return f"My_Class(self_int={self.self_int})"

if __name__ == "__main__" :
    # do test
    my_class = Class_template(10)
    print(my_class)
