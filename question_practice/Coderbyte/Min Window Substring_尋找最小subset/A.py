# MY
def MinWindowSubstring(strArr):
  longStr = strArr[0]
  longLen = len(longStr)
  minsubCount = 10000
  minStart = 0
  minEnd = 0
  for i in range(longLen) :
    countLen = 0
    copysub = list(strArr[1]).copy()
    for ii in range(i, longLen) :
      try :
        copysub.remove(longStr[ii])
      except ValueError :
        pass
      if len(copysub) == 0 :
        shortLen = ii - i
        if shortLen < minsubCount :
          minsubCount = shortLen
          minStart = i
          minEnd = ii
        break


  # print(minStart, minEnd)
  return longStr[minStart : minEnd+1]

# keep this function call here 
print(MinWindowSubstring(["aabdccdbcacd", "aad"]))