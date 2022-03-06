import a_1
print("import a_2")

def testa_2(x):
    if x == 10 :
        print("finish!!")
    else :
        print(x)
        a_1.testa_1(x+1)
    # print("in testa_1")

if __name__ == "__main__":
    a_1.testa_1(0)