# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())

# AM = MC = BM. So triangle MBC is islosceles which means theta = angle MCB

theta = math.atan(AB/BC)                        # in radian
theta = round(math.degrees(theta))
degree = chr(176)                               # the degree sign
print(theta,degree, sep = "")
