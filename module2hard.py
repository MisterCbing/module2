n = int(input())

result = ''

for i in range(1, n//2 + 1):
    for j in range(i + 1, n - i + 1):
        if n % (i + j) == 0:
            result += str(i) + str(j)

print(result)