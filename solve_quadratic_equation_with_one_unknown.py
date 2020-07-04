import math

#获取用户输入
a = float(input("请输入a的值:"))
b = float(input("请输入b的值:"))
c = float(input("请输入c的值:"))

#计算delta
delta = b**2 - 4*a*c

#判断delta是大于小于还是等于0，然后分别计算并得出结果
if delta > 0: 
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print('x1=', x1)
    print('x2=', x2)
elif delta == 0:
    x = -b / (2 * a)
    print('x=', x)
else:
    print('无解啊')