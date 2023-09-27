# задача 4-1

while True:
    lst = input().split()
    if lst == ['0']:
        break
    else:
        a, operand, b = int(lst[0]), lst[1], int(lst[2])
    if b == 0 and operand == '/':
        print('Деление на 0')
        break
    else:
        operands = {'+':a+b, '-':a-b, '*':a*b, '/':a/b}
        print(operands[operand])


# задача 4-2

n = int(input())

matrix = [['_']*n for i in range(n)]

i = 1
x = 0
y = -1
lenght = len(str(n**2))

go_row = 0
go_col = 1

while i <= n**2:
    if 0 <= x + go_row < n and 0 <= y + go_col < n and matrix[x + go_row][y + go_col] == '_':
        x += go_row
        y += go_col
        matrix[x][y] = i
        i += 1
    else:
        if go_col == 1:
            go_col = 0
            go_row = 1
        elif go_row == 1:
            go_row = 0
            go_col = -1
        elif go_col == -1:
            go_col = 0
            go_row = -1
        elif go_row == -1:
            go_row = 0
            go_col = 1

for row in range(n):
    for char in range(n):
        print(f'{matrix[row][char]:{lenght}}', end = ' ')
    print()


# задача 4-3

sent1 = input().lower()
sent2 = input().lower()

dct1 = {}
dct2 = {}

for char in sent1:
    if char.isalpha():
        dct1[char] = dct1.get(char, 0) + 1

for char in sent2:
    if char.isalpha():
        dct2[char] = dct2.get(char, 0) + 1

print(dct1 == dct2)