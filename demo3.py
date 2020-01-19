'''
age = int(input("请输入你的年龄"))
if age > 10:
    print("你已经不是个小孩了")
#输出 你已经不是个小孩了

age = int(input("请输入你的年龄"))
if age > 10:
    print("你已经不是个小孩了")
else:
    print("你还是个孩子")
#输出 你还是个孩子




age = int(input("请输入你的年龄"))
if age > 60:                #从大到小不然要增加条件
    print("退休了")
elif age > 24:
    print("好好工作")
elif age > 18:
    print("好好读大学")
elif age > 10:
    print("好好学习")
else:
    print("你还是个孩子")



hh = [1,2,3,4,5,6,7]
for i in hh:                    #遍历    
    print(i)                     for i in hh 这句话的意思是定义了个变量叫i i的定义就在hh的数组里面
输出1                             hh这个数组里有7个值 所以打印i 这个i就是这里面的1234567
    2                             所有他会打印七次每次都是不同的值 这样就实现了七次的循环
    3
    4
    5
    6
    7


hh = [1,2,3,4,5,6,7]
for i in hh:
    print("哈哈")
输出哈哈
    哈哈
    哈哈
    哈哈
    哈哈
    哈哈
    哈哈


hh = [1,2,3,4,5,6,7]
num = 0
for i in hh:
    num = num + i
    print(num)
print(num)
输出1
3
6
10
15
21
28
28

for i in range(1,10):
    for j in range(1,i+1):
        print("{}X{}={}".format(i,j,i*j),end="  ")
    print()
输出
1X1=1
2X1=2  2X2=4
3X1=3  3X2=6  3X3=9
4X1=4  4X2=8  4X3=12  4X4=16
5X1=5  5X2=10  5X3=15  5X4=20  5X5=25
6X1=6  6X2=12  6X3=18  6X4=24  6X5=30  6X6=36
7X1=7  7X2=14  7X3=21  7X4=28  7X5=35  7X6=42  7X7=49
8X1=8  8X2=16  8X3=24  8X4=32  8X5=40  8X6=48  8X7=56  8X8=64
9X1=9  9X2=18  9X3=27  9X4=36  9X5=45  9X6=54  9X7=63  9X8=72  9X9=81
'''



a = [1,2,3,45,566,44,2324,34566,2341,546,2342]
b = []
c = []
d = []
for i in a:
    if i > 2000:
       b.append(i)
    elif  i > 100:
        d.append(i)
    else:
       c.append(i)


print(b,c,d)
 