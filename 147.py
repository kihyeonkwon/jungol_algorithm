n = int(input())

count = 1


for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range(n-i):
        print(count, end=' ')
        count += 1
    print()