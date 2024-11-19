'''
a = 'variable'
print(id(a))
a = a+'2'
print(a)
print(id(a))
'''

'''
a = 100
b = a
print(id(a))
print(id(b))
a = a + 2
print(id(a))
print(id(b))
print(a)
print(b)
'''
'''
a = {'key':100}
b = a
print(id(a))
print(id(b))

a['key'] = a['key']+2

print(id(a))
print(id(b))

print(a)
print(b)
'''
'''
lst = [10,12,21]
a,b,c = lst
print(a)
print(b)
print(c)
'''

#Задание 2 сформировать картинку в виде списка в 16 ричночной системе( минимум 16x16)
#задание 3 преобразовать и вывести изображение в градациях серого
#задание 4 Применить к изображению фильтр Собеля


image = [[0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xff0000, 0xff0000, 0xffffff, 0xffffff, 0xffffff, 0xff0000, 0xff0000, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff],
 [0xffffff, 0xffffff, 0xffffff, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xffffff, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xffffff, 0xffffff, 0xffffff, 0xffffff],
 [0xffffff, 0xffffff, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xffffff, 0xffffff, 0xffffff],
 [0xffffff, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xffffff, 0xffffff],
 [0xffffff, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xffffff, 0xffffff],
 [0xffffff, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xffffff, 0xffffff],
 [0xffffff, 0xffffff, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xffffff, 0xffffff, 0xffffff],
 [0xffffff, 0xffffff, 0xffffff, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xffffff, 0xffffff, 0xffffff, 0xffffff],
 [0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff],
 [0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xff0000, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff],
 [0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xff0000, 0xff0000, 0xff0000, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff],
 [0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xff0000, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff],
 [0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff],
 [0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff],
 [0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff],
 [0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff, 0xffffff]]

for line in image:
    for pixel in line:
        pixel_r = pixel>>16
        pixel_g = (pixel>>8) & 0x00ff
        pixel_b = pixel & 0xff
        print(f"[38;2;{pixel_r};{pixel_g};{pixel_b}m"+ '\u2588', end='')
    print()