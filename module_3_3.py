def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(10, 2)
print_params(111, c=False)
print_params(b='Hello world')
print_params(14, 2342, 123)

values_list = [555, True, 'Victory']
values_dict = {'a': 777, 'b': 245.12, 'c': '(-_-)'}

print_params(*values_list)
print_params(**values_dict)
