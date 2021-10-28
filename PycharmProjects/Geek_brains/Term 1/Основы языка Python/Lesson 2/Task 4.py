stroka = input('Введите строку: ').split()
for i in stroka:
    if len(i) > 10:
        print(stroka.index(i) + 1, ": ", i[:10])
    else:
        print(stroka.index(i) + 1, ': ', i)
