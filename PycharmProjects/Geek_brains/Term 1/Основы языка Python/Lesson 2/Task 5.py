numbers = [7, 5, 3, 3, 2]
new = int(input('Введите натуральное число: '))
n = 0
while new:
    for i in numbers:
        if i < new:
            numbers.insert(int(numbers.index(i)), new)
            n += 1
            break
    if n == 0:
        numbers.append(new)
    n = 0
    print('Новый список: ', numbers)
    new = int(input('Введите натуральное число: '))
