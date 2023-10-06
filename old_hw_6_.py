# задача 6-1

date = input().upper()

def roma_to_dec(st_roma):
    if not st_roma:
        return 'введена пустая строка'
    lst = []
    number = 0
    dct = {'M': 1000,
           'D': 500,
           'C': 100,
           'L': 50,
           'X': 10,
           'V': 5,
           'I': 1}
    for char in st_roma:
        if char not in dct:
            return 'римская цифра не найдена'
        lst.append(dct[char])
    if lst == sorted(lst, reverse=True):
        return sum(lst)
    else:
        for i in range(len(st_roma) - 1):
            if lst[i] >= lst[i + 1]:
                number += lst[i]
            elif lst[i] < lst[i + 1]:
                number -= lst[i]
    number += lst[-1]
    return number

print(roma_to_dec(date))



# задача 6-2

st1 = input().lower().split(', ')
st2 = input().lower().split(', ')

if st1 != [''] and st2 != ['']:
    print(len(set(st1) & set(st2)))
else:
    print(0)



# задача 6-3

from string import ascii_letters as lttrs, digits as dgts

st = input()

numbers = ''
letters = ''
chars = ''

for c in st:
    if c in lttrs:
        letters += c
    elif c in dgts:
        numbers += c
    else:
        chars += c

if st:
    if letters: print(*set(letters))
    if numbers: print(*set(numbers))
    if chars: print(*set(chars))
else:
    print('Пустая строка')
