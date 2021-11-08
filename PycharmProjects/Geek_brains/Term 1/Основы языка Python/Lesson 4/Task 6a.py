from itertools import count

a = int(input('Enter a start number: '))
b = int(input('Enter an end number: '))
for el in count(a):
    if el <= b:
        print(el)
