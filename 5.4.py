replace_phrases = {'One':'Один','Two':'Два','Three':'Три','Four':'Четыре'}

file = open('5.4.txt',encoding='utf-8')
output_file = open('5.4.res.txt','w',encoding='utf-8')

strings = file.readlines()

for string in strings:
    replace_text, digit = string.split('—')
    replace_text = replace_text.strip()
    new_string = string.replace(replace_text,replace_phrases[replace_text])
    output_file.write(new_string)

