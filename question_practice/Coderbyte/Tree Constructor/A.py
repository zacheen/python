def TreeConstructor(strArr):
  mem = {}

  for eachLink in strArr :
    eachLink = eval(eachLink)
    

    # child 補 parent
    child = mem.get(eachLink[0], None) 
    if child == None :
      mem[eachLink[0]] = [eachLink[1],-1,-1]
    else :
      if child[0] == -1 :
        child[0] = eachLink[1]
        mem[eachLink[0]] = child
      else :
        return False

    # parent 補 child
    parent = mem.get(eachLink[1], None) 
    if parent == None :
      mem[eachLink[1]] = [-1, eachLink[0], -1]
    else :
      if parent[1] == -1 :
        parent[1] = eachLink[0]
        mem[eachLink[1]] = parent
      elif parent[2] == -1 :
        # print("有進嗎? parent: ",parent)
        parent[2] = eachLink[0]
        # print("有進嗎? parent: ",parent)
        mem[eachLink[1]] = parent
      else :
        return False

    # print(eachLink, mem)
    
  return True

# keep this function call here 
print(TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]))