def get_matrix(n, m, value):
    if n <= 0 or m <= 0:
        return []
    else:
        return [[value] * m for _ in range(n)]

print(get_matrix(3, 5, 7))
print(get_matrix(0, 6, 1))