def convert_to_str(list):
    return [str(i) for i in list]
def convert_to_int(list):
    return [int(i) for i in list]
def write():
    output_list = list()
    try:
        output_text = int(input('Enter text: '))
        output_list.append(output_text)
    except ValueError:
        print('Not Digit')
        return False
    while output_text:
        try:
            output_text = int(input('Enter text: '))
            output_list.append(output_text)
        except ValueError:
            output_text = ''
            print('Not Digit')
            continue
    output_file = open('5.5.txt', mode='w')
    string_list = convert_to_str(output_list)
    output_file.write(' '.join(string_list))
    output_file.close()
    return True


def read():
    input_file = open('5.5.txt', mode='r')
    digits_string = input_file.read().split(' ')
    digits_int = convert_to_int(digits_string)
    input_file.close()
    return sum(digits_int)


success = write()

if success:
    print(read())