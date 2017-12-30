my_dict = {'x':'a', 'y':'b', 'z':'c'}
print(my_dict)
my_dict = {v: k for k, v in my_dict.items()}
print(my_dict)