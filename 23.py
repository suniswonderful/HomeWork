month = dict()
month['winter'] = [1, 2, 12]
month['spring'] = [3, 4, 5]
month['summer'] = [6, 7, 8]
month['autumn'] = [9, 10, 11]
number = int(input('Введите номер месяца: '))
for key, value in month.items():
    if number in value:
        print(key)
        break
