file = open('5.3.txt',encoding='utf-8')

employees = file.readlines()
common_value = 0
print('Сотрудники с окладом менее 20000:')
for employee in employees:
    surname, salary = employee.split(':')
    common_value +=int(salary)
    if int(salary) < 20000:
        print('\t{}'.format(surname))
print('Средняя величина доходов: {}'.format(common_value / len(employees)))