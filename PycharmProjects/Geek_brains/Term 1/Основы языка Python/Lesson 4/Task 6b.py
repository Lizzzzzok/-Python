from itertools import cycle

list_ = input('Enter elements separeted by a space: ').split()
a = int(input('Enter a number of repeating the cycle: '))
b = 0
for el in cycle(list_):
    if b == a:
        break
    print(el)
    b += 1
