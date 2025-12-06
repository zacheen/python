# import Father_class # 使用 Father_class.Father
from Father_class import Father

class Child(Father):
    def __init__(self):
        super().__init__()
        print("Child init")

    # override
    def test_polymofisim(self):
        print("Child polymofisim")

father = Father()
child = Child()
instances = [father, child]
for instance in instances:
    instance.test_inherit()
    instance.test_polymofisim()

# # 查看是否有繼承(inherit)關係 
print("relation1 :", isinstance(father, Father))    # returns True
print("relation2 :", type(father) == Father)        # returns True
print("relation3 :", isinstance(child, Father))    # returns True
print("relation4 :", type(child) == Father)        # returns False
print("relation5 :", isinstance(father, Child))    # returns False
print("relation6 :", type(father) == Child)        # returns False
