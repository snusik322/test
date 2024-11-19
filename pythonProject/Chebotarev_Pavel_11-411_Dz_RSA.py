p =  599
q = 631
N =  p *q
Phi = (p-1)*(q-1)
e = 691
Publ = [N,e]
#Алгоритм Евклида
a = Phi
b =e
x1 = 0
x2 = 1
y1 = 1
y2 = 0
while b>0:
    q = a//b
    r = a-q*b
    x = x2-q*x1
    y = y2-q*y1
    a = b
    b = r
    x2= x1
    x1 =x
    y2 = y1
    y1 = y
print('d =', Phi - abs(min(x2,y2)))
d = Phi - abs(min(x2,y2))
Sec = [N,d]
print('Публичный ключ = ', Publ)
print('Приватный ключ =', Sec)
mess = 'I <3 KFU'
print('сообщение = ', mess)
en_mess= mess.encode('utf-8')
en_numb = list(en_mess)
print('сообщение в UTF-8 = ', en_numb)
c = []
for i in en_numb:
    c.append((i**e) % N)
print('закодированное сообщение =', c)

m = []
for i in c:
    m.append((i**d)%N)
byte_mess = bytes(m)
dec_mess = byte_mess.decode('utf-8')
print('расшифрованное сообщение = ', dec_mess)
