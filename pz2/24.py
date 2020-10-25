elements_list = input('Enter your words  with spaces: ').split()
for i in elements_list:
    if len(i) > 10:
        print(i[0:9])
    else: print(i)