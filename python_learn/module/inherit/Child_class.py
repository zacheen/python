# import Father_class # 使用 Father_class.Father
from Father_class import Father

class Child(Father):
    def __init__(self):
        super().__init__()
        print("Child init")
    
    # overload
    def func1(self):
        print("Child func1")

child = Child()
child.func1()

# # 查看是否有繼承(inherit)關係 
# # isinstance(Child(), Father)
# print("relation1 :", isinstance(Father(), Father))    # returns True
# print("relation2 :", type(Father()) == Father)        # returns True
# print("relation3 :", isinstance(Child(), Father))    # returns True
# print("relation4 :", type(Child()) == Father)        # returns False
# print("relation5 :", isinstance(Father(), Child))    # returns False
# print("relation6 :", type(Father()) == Child)        # returns False