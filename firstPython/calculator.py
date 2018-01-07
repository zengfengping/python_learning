import cmath as math

while(True):
    aa = input("输入第一个数字：")
    x = input("输入符号，+,-,*,/,log,exp:")
    bb = input("输入第二个数字: ")

    try:
        a = float(aa)
        b = float(bb)
    except:
        print("输入的数字出错啦，重新来吧～")
        continue

    if (x == '+'):
        c = a+b
        print("{}+{}={}".format(a,b,c))
    elif x == "-":
        c = a - b
        print("{}-{}={}".format(a, b, c))
    elif x == "*":
        c = a*b
        print("{}*{}={}".format(a, b, c))
    elif x == "/":
        if b==0:
            print("除数不能为0的哟～")
            continue
        c = a/b
        print("{}/{}={}".format(a,b,c))
    elif x=="log":
        c = math.log(a,b)
        print("log{}={}".format(a,c))
    elif x=="exp":
        c = a**b
        print("{} exp{}={}".format(a,b,c))
    else:
        print("必须是符号啊,记着啦，必须是+ - * /中间的一个啦！")
