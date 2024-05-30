def super_sum(el):
    if isinstance(el, int) or isinstance(el, float):
        return el
    elif isinstance(el, str):
        return len(el)
    elif isinstance(el, list) or isinstance(el, tuple) :
        if len(el) < 1:
            return 0
        else:
            return super_sum(el[0]) + super_sum(el[1:])
    elif isinstance(el, dict):
        temp = [[x, y] for x, y in el.items()]
        return super_sum(temp)
    elif isinstance(el, set):
        temp = 0
        for i in el:
            temp += super_sum(i)
        return temp
    else:
        return 0

def calculate_structure_sum(st):
    res = 0
    for i in st:
        res += super_sum(i)
    return res

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)