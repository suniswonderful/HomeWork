amount = int(input("How many elements do you want in your list? "))
elements_list = []
for i in range(amount):
    element = input("Element {}: ".format(i +1))
    elements_list.append(element)
for i in range(0, amount - 1, 2):
    a = elements_list[i]
    elements_list[i] = elements_list[i + 1]
    elements_list[i + 1] = a
print(','.join(elements_list))
