import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-n")
parser.add_argument("-b")
args=parser.parse_args()
print (args.n)
for _ in range(int(args.n)):
    print ("meow")