def my_func(x, y):
    return x ** y

def my_func_var_2(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    return 1 / result



x = int(input('Enter positive X: '))
y = int(input('Enter negative Y: '))
if y < 0:
    print('{}'.format(my_func(x, y)))
    print('{}'.format(my_func_var_2(x, y)))
else:
    print('Y > 0, enter another Y')

