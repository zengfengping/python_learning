nominator = 1.0
denominator = 1.0
sum = 1.0
for i in range(1,150):
    p1 = sum * 2
    nominator *= i
    denominator *= (2*i+1)
    sum += (nominator/denominator)
    p2 = sum * 2
    p = p2 - p1
    print("{} round, pi={}, change {}".format(i, p2,p))

