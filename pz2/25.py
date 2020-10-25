my_list = [7, 5, 3, 3, 3]
print(my_list)
entered_element = int(input('Enter your element: '))

try:
    x = my_list[::-1].index(entered_element)
    my_list.insert(len(my_list) - x, entered_element)

except ValueError as e:
    min_value = True
    for i in range(len(my_list)):
        if entered_element > my_list[i]:
            my_list.insert(i, entered_element)
            min_value = False
            break
    if min_value is True:
        my_list.insert(len(my_list), entered_element)
print(my_list)

