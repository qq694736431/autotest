money = input("请输入红包金额")
num = money.count(".")
if num <= 1:
    for i in money:
         if i not in "1234567890.":
            print("请输入数字！！")
            exit()
    if num == 1:
        xsws = len(money) - (money.index(".")+1)
        if xsws <=2:
            money = float(money)
            if money >= 0.01 and money <= 200:
                print("发送红包成功！金额:",money)
            else:
                print("红包的金额必须在0.01-200的范围内")
        else:
            print("只能输入两位小数")
    else:
        money = float(money)
        if money >= 0.01 and money <= 200:
            print("发送红包成功！金额",money)
        else:
            print("红包金额必须在0.01-200的范围内！")
else:
    print("请输入正确的数字")
    