def QuestionsMarks(strParam):
    
  QCount = 0
  firstNum = -1
  OneAns = False
  for eachWord in strParam :
    # print(eachWord, QCount, firstNum)
    if eachWord == "?" :
      QCount = QCount + 1
    elif eachWord.isnumeric() :
      secondNum = int(eachWord)
      if firstNum + secondNum == 10 :
        if QCount != 3 :
          return False
        else :
          OneAns = True
      firstNum = secondNum
      QCount = 0

  return OneAns


# keep this function call here 
print(QuestionsMarks("5??aaaaaaaaaaaaaaaaaaa?5?a??5"))