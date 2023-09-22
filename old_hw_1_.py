#  задача 1-1

x, y = int(input('Введите число x: ')), int(input('Введите число y: '))
print(f'Сумма равна: {x+y}')
print(f'Произведение равно: {x*y}')


#  задача 1-2

x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
res = [x+y, x-y, x*y, x/y, x//y]
print(max(res))


#  задача 1-3

writeln = print
x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
res = x+y, x-y, x*y, x/y, x//y
writeln(sorted(res)[-2])
