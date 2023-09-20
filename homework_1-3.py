#  задача 1-3

writeln = print
x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
res = x+y, x-y, x*y, x/y, x//y
writeln(sorted(res)[-2])
