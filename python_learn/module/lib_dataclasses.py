from dataclasses import dataclass
# 簡化建立 class 的過程
    # 會自動生成 __init__、__repr__、__eq__

# < 使用 dataclass 定義 class >
@dataclass
class Person:
    name: str
    age: int
    # 可以直接預設
    kind1: str = "human1"   # 這個寫法才會被 print 印出
    kind2 = "human2"        # 這個寫法不會被 print 印出(但還是可以取用)
    

p1 = Person(name="Alice", age=30)
p2 = Person(name="Alice", age=30)
p3 = Person(name="Blice", age=30)

print("auto generate __repr__ :", p1)        # 自動產生的 __repr__
print("auto generate __eq__   :", p1 == p2)  # 自動產生的 __eq__
print("auto generate __eq__   :", p1 == p3)  # 自動產生的 __eq__

# < dataclass 常常被拿來建立 Config class!! >
@dataclass
class Config:
    gemma_dir: str = 'dir1'
    lora_dir: str = 'dir2'
    max_length: int = 2048
    batch_size: int = 4
cfg = Config()
print("direct init", cfg)

## 屬性測試 #######################################################################
@dataclass
class MyClass:
    class_var_str = "class_var_str"

c1 = MyClass()
c2 = MyClass()
c1.class_var_str = "change" 
# 這個覆寫了 c1.class_var_str (現在 c1.class_var_str 是 instance variable 了)
print("c1.class_var_str :", c1.class_var_str) # 有修改
print("c2.class_var_str :", c2.class_var_str) # 沒有修改

@dataclass
class MyClass:
    class_var_list = []

c1 = MyClass()
c2 = MyClass()
c1.class_var_list.append("change1")
c2.class_var_list.append("change2")
print("c1.class_var_list :", c1.class_var_list) # 有修改
print("c2.class_var_list :", c2.class_var_list) # 有修改


# ## 若未使用 dataclass 比較 ##############################################
# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"Person(name={self.name!r}, age={self.age!r})"

#     def __eq__(self, other):
#         if not isinstance(other, Person):
#             return NotImplemented
#         return self.name == other.name and self.age == other.age
# p1 = Person(name="Alice", age=30)
# p2 = Person(name="Alice", age=30)
# print(p1)      
# print(p1 == p2)