file = open('5.2.txt',encoding='utf-8')
text_from_file = file.readlines()
print('Количество строк в файле: {}'.format(len(text_from_file)))
for i in text_from_file:
    words = i.split(' ')
    print('Количество слов в строке: {}. равно: {}'.format(i.replace('\n',''),len(words)))