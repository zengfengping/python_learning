b=0

while b!=-1:
    a = input("输入一个数字: ")

    print("你输入了---",a)

    try:
        b = int(a)
        print("他的平方是： ",b*b*b)
    except:
        print("a不对呀，重新来吧")
