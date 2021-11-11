f = open("file_task5.txt", 'w+')
f.write(input('Enter numbers divided by a space: '))
summa = 0
f.seek(0)
for num in f.read().split():
    summa += int(num)
print(summa)
f.close()
