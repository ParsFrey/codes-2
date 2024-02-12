import math
print('a x**x + b x + c = 0')
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
print(a,'x*x',' + ',b,'x',' + ',c,'=   0')
delta = b**2 - 4*a*c
print('▲=', delta)
if delta < 0:
    print('There is no answer, because delta is negetive')
if delta == 0:
    print(-b/(a*2))
if delta > 0:
    print('(-b+√▲)/a*2','=')
    print(-b+math.sqrt(delta)/a*2)

    print('(-b-√▲)/a*2','=')
    print(-b-math.sqrt(delta)/a*2)
