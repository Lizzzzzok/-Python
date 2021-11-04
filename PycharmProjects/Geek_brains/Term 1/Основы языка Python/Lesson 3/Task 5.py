print('If you want to exit, enter !')
summa = 0
stop = 0
while True:
    new = input('Enter a string: ').split()
    for el in new:
        if el == '!':
            stop = 1
            break
        summa += int(el)
    print(summa)
    if stop == 1:
        break
