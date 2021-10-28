number = int(input('Введите число от 1 до 12: '))
month = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
for i, j in month.items():
    if number in j:
        print(i)
