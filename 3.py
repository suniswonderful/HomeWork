n = input('Enter your number: ')
minus = ''
if int(n) < 0:
    minus = '-'
n_new = n.replace('-', '')
nn = n_new * 2
nnn = n_new * 3
n_new = '{}{}'.format(minus, n_new)
nn = '{}{}'.format(minus, nn)
nnn = '{}{}'.format(minus, nnn)
result = int(n_new) + int(nn) + int(nnn)
print('{} + {} + {} = {}'.format(n_new, nn, nnn, result))

