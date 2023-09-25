# задача 2-1

n = int(input())

for i in range(1, 10):
    print(f'{i} x {n} = {i*n}')


# задача 2-2

lst = []
n = int(input('Введите длину списка: '))
for i in range(n):
    number = int(input('Введите число: '))
    lst.append(number)
if lst:
    mini = lst[0]
    for i in range(1, len(lst)):
        if lst[i]<mini:
            mini = lst[i]
    print(mini)
else:
    print('Пустой список')


# задача 2-3

n = int(input())
pr = 1
for i in range(2, n+1):
    pr *= i
print(pr)