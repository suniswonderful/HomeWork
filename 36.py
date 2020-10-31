def int_func(text):
    text = text.split(' ')
    capitalize_func = lambda x: x.capitalize()
    result = [capitalize_func(x) for x in text]
    return ' '.join(result)

text = input("Enter text: ")
capitalized_text = int_func(text)
print(capitalized_text)