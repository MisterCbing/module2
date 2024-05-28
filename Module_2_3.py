my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_len = len(my_list)
i = 0
while i < list_len:
    if my_list[i] > 0:
        print(my_list[i])
    elif my_list[i] < 0:
        break
    i = i + 1