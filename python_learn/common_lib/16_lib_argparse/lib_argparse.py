import argparse
parser = argparse.ArgumentParser()

def sumOF(a, b):
    print(int(a)+int(b))

# basic option
parser.add_argument('-n1', dest='a', help='the first input number', default=10)
parser.add_argument('-num2','-n2', dest='b', help='the second input number', default=30)

if __name__ == '__main__':
    a = parser.parse_args().a
    b = parser.parse_args().b
    sumOF(a, b)