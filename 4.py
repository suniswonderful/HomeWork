n = input('Enter your number: ')
max_number = 1
while int(n) > 0:
    rest = int(n) % 10
    if rest > max_number:
        max_number = rest
    n = int(n) // 10
print(max_number)