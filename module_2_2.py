first, second, third = int(input()), int(input()), int(input())
txt = 'Количество одинаковых чисел:'
if first == second == third:
    print(txt, 3)
elif first == second or second == third or first == third:
    print(txt, 2)
else:
    print(txt, 0)