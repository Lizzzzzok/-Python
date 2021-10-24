n = abs(int(input('Ввведите целое положительное число: ')))
max_ = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max_:
        max_ = n % 10
    if n > 9:
        continue
    else:
        print("Максимальнае цифра в числе: ", max_)
        break
