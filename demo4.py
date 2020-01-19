'''
i = 0
while i < 30:
    i = i + 1
    print("绿灯",i)
输出 绿灯 1
绿灯 2
绿灯 3
绿灯 4
绿灯 5
绿灯 6
。。。绿灯 30

i = 0
while i < 30:
    i = i + 1
    if i == 5:    #跳过了 5
        continue   #扛提溜  continue 跳过这一次循环
    print("绿灯",i)
输出 绿灯 1   #跳过了 5
绿灯 2
绿灯 3
绿灯 4
绿灯 6
绿灯 7
。。。。绿灯 30

i = 0
while i < 30:
    i = i + 1
    if i == 5:
        break     #  break 不瑞克 终止循环
    print("绿灯",i)
输出 绿灯 1
绿灯 2
绿灯 3
绿灯 4
'''