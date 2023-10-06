# задача 7-1

s = list(map(int, input().split()))

def nod(a, b):
    while a!= 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b

def nok2(a, b):
    return a * b // nod(a, b)

x = 1
for i in s:
    x = nok2(x, i)

print(x)



# задача 7-2

def code(string, n):
    res = ''
    for i in string:
        new_ord = ord(i) + n
        if chr(ord('a')) <= i <= chr(ord('a') + 25):
            new_ord = ord('a') + (new_ord - ord('a')) % 26
            res += chr(new_ord)
        elif chr(ord('A')) <= i <= chr(ord('A') + 25):
            new_ord = ord('A') + (new_ord - ord('A')) % 26
            res += chr(new_ord)
        else:
            res += i
    return res

while True:
    print(code(input(), int(input())))
    if input() == 'stop':
        break



# задача 7-3

lst = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]]
cmn = []
for i in lst:
    cmn.extend(i)
print(sorted(cmn)[-3:])
