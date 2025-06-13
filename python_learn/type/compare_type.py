# isinstance(var, TYPE) 
    # 繼承的 class 也會是 True
# type(var) == TYPE
    # 精準判斷type，不會考慮繼承

class Animal:
    pass
class Dog(Animal):
    pass

a = Dog()
print(type(a) == Dog)     # True
print(type(a) == Animal)  # False（即使 Dog 繼承自 Animal）
print(isinstance(a, Dog))     # True
print(isinstance(a, Animal))  # True

a = 0
print(type(a) == int)     # True
print(isinstance(a, int))     # True