special_char = '#'

def my_func():
    global result
    result = 0
    while True:
        numbers = input('Enter your numbers  with spaces: ').split(' ')
        for number in numbers:
            if number == special_char:
                return result
            result+=int(number)
        print(result)
summ = my_func()
print(summ)