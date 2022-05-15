def minion_game(string):
    # your code goes here
    score = [0,0]
    for i in range(len(string)):
        if string[i] in ["A","E","I","O","U"]:
            person = 1
        else :
            person = 0
        
        score[person] += (len(string) - i)
    # print(score)
    
    if score[0] > score[1] :
        print("Stuart " + str(score[0])) 
    elif score[0] < score[1] :
        print("Kevin " + str(score[1])) 
    else :
        print("Draw")

if __name__ == '__main__':
    s = "BANANA"#input()
    minion_game(s)