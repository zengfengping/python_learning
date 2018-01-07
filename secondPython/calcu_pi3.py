from decimal import *

getcontext().prec = 1000
nominator = Decimal("1.0")
denominator = Decimal("1.0")
sum = Decimal("1.0")
j=1
k=Decimal("10")
for i in range(1,10000):
    p1 = sum * 2
    nominator *= i
    denominator *= (2*i+1)
    sum += (nominator/denominator)
    p2 = sum * 2
    p = p2 - p1
    if(p==0):
        print("达到最高精度了，程序退出")
        break
    if p*k <1:
        j +=1
        k *=10
    print("{} round, 小数点后第{}位".format(i,j))


    print("pi={}".format(p2))
