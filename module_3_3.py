def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    
print_params(b = 25)
print_params(c = [1,2,3])


values_list = ['string', 12, 45.6]
values_dict = {'a': 'guitar', 'b': 36, 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [12, 'guitar']
print_params(*values_list_2, 42)