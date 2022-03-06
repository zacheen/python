import re

# 多個字符替換
txt = "4w74sd89sdf 2!37wserf489sdre"
txt2 = re.sub('[0-9]', 'X', txt)
print(txt2)
print(txt)