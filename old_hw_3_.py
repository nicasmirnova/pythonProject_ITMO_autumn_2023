# задача 3-1

salary = int(input('Введите зарплату сотрудника: '))
summa = 0
count = 0
while salary != 0:
    summa += salary
    count += 1
    salary = int(input('Введите зарплату сотрудника: '))

print(f'Средняя зарплата равна {round(summa / count, 3)}')


# задача 3-2

number = int(input('Введите целое число: '))

lst = [0] * 10

while number > 0:
    index = number % 10
    lst[index] += 1
    number //= 10

for index, value in enumerate(lst):
    print(f'{index} - {value}')


# задача 3-3

lst = input('Введите предложение: ').split()

if lst:
    max_len = len(lst[0])
    for slovo in lst:
        if len(slovo) > max_len:
            max_len = len(slovo)
    for slovo in lst:
        if len(slovo) == max_len:
            print(slovo)
else:
    print('Введена пустая строка')
