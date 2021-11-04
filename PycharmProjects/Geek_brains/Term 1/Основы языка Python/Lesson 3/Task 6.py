def int_func(string):
    stroka = ''
    for word in string.split():
        stroka += word.title()
        stroka += ' '
    return stroka


print(int_func(input('Enter a string: ')))
