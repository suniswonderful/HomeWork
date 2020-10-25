spisok = []
items = int(input('Сколько товаров Вы хотите внести? '))
for i in range(items):

    dictionary = {"Название": input('Название: '),
                  "Цена": input('Цена: '),
                  "Количество": input('Количество: '),
                  "Единицы": input('Единицы: ')}
    x = (i + 1, dictionary)
    spisok.append(x)
print(spisok)
my_dict = {"Название":list(), "Цена":list(), "Количество":list(), "Единицы":list()}

for element in spisok:
    position = element[1]
    for key, value in my_dict.items():
        value.append(position[key])
print(my_dict)
