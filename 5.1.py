def write():
    output_file = open('file.txt',mode='w')
    output_text = input('Enter text: ')
    while output_text:
        output_file.write(output_text + '\n')
        output_text = input('Enter text: ')

    output_file.close()

write()
