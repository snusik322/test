'''
a = 100
print(type(a))

a = '100'
print(type(a))

print(100)
a = 962
b = 34
c = a**b
print(c)
print(type(c))

# Побитовые операции
a = 0b01
b = 0b10
c = 0b11
print(a&b)
print(c&b)
print(c&a)

# Задание 1 вывести таблицу "умножения" для побитовых операций в разных цветах


#сдвиги
a = 0b001101

print(a>>2) #сдвиг вправо на 1 позицию эквивалентен делению на 2
print(a<<2) #сдвиг влево на 1 позицию эквивалентен умножению на 2
print('100'+'1')

print('\x1B[38;2;255;0;0m')
print('Красная надпись')
'''

'''
print('\x1B[38;2;0;0;255m')
print(f"  {'A':^2}  {'B':^5}  {'A&B':^3}  {'A|B':^5}  {'A^B':^4}  {'A<<B':^5} {'A>>B':^5} {'~A':^5} {'~B':^5}")
print('\x1B[38;2;252;15;192m')
print("-" * 55)
for a in (0, 1):
    for b in (0, 1):
        and_op = a & b
        or_op = a | b
        xor_op = a ^ b
        vlv = a<<b
        vpr = a>>b
        otra = ~a
        otrb = ~b
        print('\x1B[38;2;255;0;0m')
        print(f"  {a:^2}  {b:^5}  {and_op:^3}  {or_op:^5}  {xor_op:^4} {vlv:^6} {vpr:^4} {otra:^6} {otrb:^6}" )
        print('\x1B[38;2;255;255;0m')
        print("-" * 55)
'''
'''
print(' таблица истинности для A&B:')
print("A  B  A&B")
for a in range(0,2):
    for b in range(0,2):
        print(f"{a}  {b}   {a&b}")

print(' таблица истинности для A|B:')
print("A  B  A|B")
for a in range(0,2):
    for b in range(0,2):
        print(f"{a}  {b}   {a|b}")

print(' таблица истинности для A^B:')
print("A  B  A^B")
for a in range(0,2):
    for b in range(0,2):
        print(f"{a}  {b}   {a^b}")

print(' таблица истинности для ~A:')
print("A   ~A")
for a in range(0,2):
        print(f"{a}   {~a}")

print(' таблица истинности для ~B:')
print("B   ~B")
for b in range(0,2):
        print(f"{b}   {~b}")

print(' таблица истинности для A>>B:')
print("A  B  A>>B")
for a in range(0,2):
    for b in range(0,2):
        print(f"{a}  {b}   {a>>b}")

print(' таблица истинности для A<<B:')
print("A  B  A<<B")
for a in range(0,2):
    for b in range(0,2):
        print(f"{a}  {b}   {a<<b}")
'''

print('\x1B[38;2;0;255;0m')
print(f"{"|"}{'-'*43}{"|"} ")
print('\x1B[38;2;255;255;0m')
print(f"| {'A':^2}  {'B':^3}  {'A&B':^3} {'A|B':^5} {'~A':^5} {'~B':^5} {'A>>B':^5} {'A<<B':^5}|")
print('\x1B[38;2;0;255;0m')
print(f"{"|"}{'-'*43}{"|"} ")
for a in range(0,2):
    for b in range(0,2):
        print('\x1B[38;2;255;0;0m')
        print(f"|{a:^3}  {b:^3}   {a&b:^2} {a|b:^5} {~a:^4} {~b:^6} {a>>b:^4} {a<<b:^6}|")
        print('\x1B[38;2;0;0;255m')
        print('|' + '-' * 43 +   "|")



