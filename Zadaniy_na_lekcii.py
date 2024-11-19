#1
'''
a = 1
b = 2 
if a<=b:
    a = 0
    print(a,b)
else:
    print(a,b)
'''
#2
'''
a = 10
b = 15
c = -100
if a>=0:
    a**=2
if b>=0:
    b**=2
if c>=0:
    c**=2
print(a,b,c)
'''
#3
'''
a = 3322
a = str(a)
suma = 0
for i in range(len(a)):
    suma+=int(a[i])
print(suma)
'''
'''
#4
a = 2.1
b = 2.999
c = 1.0001
res = []
if 1<a<3:
    res.append(a)
if 1<b<3:
    res.append(b)
if 1<c<3:
    res.append(c)
res.sort()
print(res)
'''
#5
'''
a = int(input('vvedite chislo: '))
flag = 0
while flag == 0 :
    x = int(input('vvedite chislo:'))
    if x<a:
        flag = 1
    else:
        a = x
print('vse')
'''
#6
'''
import math
x = float(input('vvedite chs: '))
print('viberete: 1 - voz v kv; 2 - izv kor; 3 - sin; 4 - cos;')
a = int(input())
if a == 1:
    print(x**2)
if a == 2:
    print(x**0.5)
if a == 3:
    print(math.sin(x))
if a == 4:
    print(math.cos(x))
'''
#7
'''
k = 5
for i in range(1,10):
    print(k*i, sep = ' ')
'''
