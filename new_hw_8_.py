# задача 8-1

lst = list(input())
print(lst)
for i in range(len(lst)-1):
    if lst[i] == 'А' and lst[i+1] == 'Г' or lst[i] == 'Г' and lst[i+1] == 'А':
        lst[i], lst[i+1] = lst[i+1], lst[i]
    elif lst[i] == 'Ц' and lst[i+1] == 'Т' or lst[i] == 'Т' and lst[i+1] == 'Ц':
        lst.insert(i+1, 'АГ')
print(lst)



# задача 8-2

lst = list(input())

for tsl in lst:
    tsl.sort(reverse=True)

def big_sort(lst):
    for tsl in lst:
        stroka = ''
        for number in tsl:
            stroka += str(number)
        print(stroka, len(stroka))

print(sorted(lst, key=big_sort(lst)))



# задача 8-3

lst = input().split()

print(sorted(lst, key = lambda word: (-len(set(word)), word)))