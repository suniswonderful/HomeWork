def my_func(a,b):
    if b == 0:
        print('B = 0, prohibited')
        return None
    return a / b
a = int(input('Enter A: '))
b = int(input('Enter B: '))
print('A / B = {}'.format(my_func(a,b)))
