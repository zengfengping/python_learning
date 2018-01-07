from decimal import *

getcontext().prec = 100
nominator = Decimal("1.0")
denominator = Decimal("1.0")
sum = Decimal("1.0")
for i in range(1,1000):
    p1 = sum * 2
    nominator *= i
    denominator *= (2*i+1)
    sum += (nominator/denominator)
    p2 = sum * 2
    p = p2 - p1
    print("{} round, pi={}, change {}".format(i, p2,p))
