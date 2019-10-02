from math import *

C = 50
H = 30

def calc(D):
    return sqrt((2*C*D)/H)

D = input("Please input a sequence seperated by commas (no spaces): ").split(",")
D = [str(round(calc(int(i)))) for i in D]
print(",".join(D))
