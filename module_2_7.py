def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [2, 'текст', False]
values_dict = {'a': 3, 'b': 'новый текст', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 'Ответ на главный вопрос жизни, вселенной и всего такого:']
print_params(*values_list_2, 42)