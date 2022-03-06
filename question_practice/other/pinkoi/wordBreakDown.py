# Task
# I member that the task is find out that whether strList[1] can compose strList[0]
# If can than return the least using word of combination that can compose strList[0]
def wordBreakDown(strList) :
    # change list to data
    target = strList[0]
    targetLen = len(strList[0])
    composeList = strList[1].split(",")
    # print(composeList)
    composeList.sort(key=len, reverse=True)
    # print(composeList)

    # mem is for speed up
    mem = {}

    def recursive(startPoint, compList) :
        if startPoint == targetLen :
            return compList

        isFind = mem.get(startPoint, None)
        if isFind :
            # print("same len as before",compList)
            return None

        for eachCompWord in composeList :
            # print(compList, eachCompWord)
            endPoint = startPoint + len(eachCompWord)
            if endPoint > targetLen :
                continue

            elif target[startPoint:endPoint] == eachCompWord :
                passList = compList.copy()
                passList.append(eachCompWord)
                ret = recursive(endPoint, passList)
                if ret != None :
                    return ret

        mem[startPoint] = True
        return None

    return recursive(0,[])

# testcases
print(wordBreakDown(["pinkoi","pink,pin,poi,djfkli,sdf,ee,a,g,y,koi"]))
print(wordBreakDown(["abcdefghijk","a,aa,ab,ac,abcd,cde,efght,efgh,ghij,jl"]))
print(wordBreakDown(["abcdefghijk","a,aa,ab,ac,abcd,cde,efght,efgh,ghi,ijk"]))
# This testcases's intention is for demonstrate using "mem" can speed up
print(wordBreakDown(["aaaaaaaaaaaaaaaaaaaaa","aa,aaaa,aaaaaa,ac,b,c,d,e,f,g,h"]))