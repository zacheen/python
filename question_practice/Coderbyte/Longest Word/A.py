# Me
def LongestWord(sen):
      # print(sen)

  maxWord = ""
  maxNum = 0

  tempWord = ""
  tempNum = 0
  for eachword in sen :
    # print(eachword)
    if (eachword >= "a" and eachword <= "z") or (eachword >= "A" and eachword <= "Z") :
    # 優化成這個更好 if eachword.isalpha() or eachword.isnumeric() :
      tempWord = tempWord + eachword
      tempNum = tempNum + 1
    else :
      # print(tempNum, maxNum)
      if tempNum > maxNum :
        maxNum = tempNum
        maxWord = tempWord
      tempWord = ""
      tempNum = 0

  if tempNum > maxNum :
      maxNum = tempNum
      maxWord = tempWord

  return maxWord

# 使用 string 的內建 function
def LongestWord(sen):
    nw = ""
    for letter in sen:
      if letter.isalpha() or letter.isnumeric():
        nw += letter
      else :
        nw += " "
    return max(nw.split(),key=len)

# 方法 import lib
# import re
# pattern = re.compile(r'\W+')
# def LongestWord(sen): 
#     x = pattern.split(sen)
#     return max(x, key=len)

# keep this function call here 
# Input: "fun&!! time"
# Input: "I love dogs"
print(LongestWord("fun&!! time"))