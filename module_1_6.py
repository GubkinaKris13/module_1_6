from Практика.Множества import list_

my_dict = {'Vova' : 1991, 'Alisa' : 2022, 'Kristina' : 1989}
my_dict ['Ira'] = 1870
print(my_dict)
my_dict.update({'Denis' : 1988, 'Anton' : 1995})
a = my_dict.pop('Vova')
print(a)
print(my_dict)

my_set = {1, 2, 13, 'peach', 3, 13, (4,25)}
print(my_set)
print(my_set.add(14), my_set.add(15))
print(my_set)
print(my_set.discard(1))
print(my_set)