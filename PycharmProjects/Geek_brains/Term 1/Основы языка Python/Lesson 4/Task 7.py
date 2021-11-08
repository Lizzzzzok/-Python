from itertools import count
from math import factorial


def generator():
    for element in count(1):
        yield factorial(element)


g = generator()
print(g)
a = 0
b = int(input('Enter an end number: '))
for el in g:
    if a == b:
        break
    print(el)
    a += 1
