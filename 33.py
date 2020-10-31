def my_func(a, b, c):
    if a < b and a < c:
        return b + c
    if b < a and b < c:
        return a + c
    if c < a and c < b:
        return a + b


a = int(input('Enter A: '))
b = int(input('Enter B: '))
c = int(input('Enter C: '))
print('{}'.format(my_func(a, b, c)))
