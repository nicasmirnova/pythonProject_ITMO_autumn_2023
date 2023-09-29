# задача 5-1

n = int(input())

triangle = []

for level in range(n+1):
    triangle.append([1]+[0]*n)

for r in range(1, n+1):
    for c in range(1, r+1):
        triangle[r][c] = triangle[r-1][c] + triangle[r-1][c-1]

for r in range(n+1):
    for c in range(r+1):
        print(triangle[r][c], end=' ')
    print()



# задача 5-2

n = int(input())

for i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')



# задача 5-3

n = int(input('Введите длину последовательности: '))

n1 = 1
n2 = 1
for i in range(n):
    print(n1, end=' ')
    n1, n2 = n2, n1 + n2