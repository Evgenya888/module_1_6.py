my_dict = {'Евгения': 1967, 'Александр': 1970, 'Марина': 1985, 'Виктория': 1990, 'Мария': 2003}
print('Словарь:', my_dict)
print('Год рождения Марины:', my_dict['Марина'])
print('Год рождения Елены:', my_dict.get('Елена', 'нет такого ключа'))
my_dict.update({'Александр младший': 2000, 'Мария': 2003})
removed_year = my_dict.pop('Мария')
print('Значение удалённого элемента \'Мария\':', removed_year)
print('Изменённый словарь:', my_dict)

print()

my_set = {2, 3, 3, 2, 5, True, True, False, True, 'list', 'set', 'list', 'list'}
print('Множество:', my_set)
my_set.add('string')
my_set.add('float')
my_set.discard(2)
print('Изменённое множество:', my_set)