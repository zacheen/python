from fractions import Fraction

# <初始化> 數字轉分數
f = Fraction(numerator=6, denominator=15) # 會自動約分
print(f)
# <取值>
print(f.numerator, f.denominator)
# # <盡量不要用 float 初始化>
# f = Fraction(1.5) # 會自動轉換成分數
# print(f)
# f = Fraction(1.1) # 但是有些 float 存在精确問題
# print(f)

# < 分數轉數字 >
print(float(f))

# < 分數相乘 > 也是會自動約分
f2 = Fraction(3, 2)
print(f * f2)
