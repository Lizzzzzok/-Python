f = open("file.task6.txt", 'r')
lessons = {}
for line in f.read().split('\n'):
    summa = 0
    n = ' '.join(line.split()[1:])
    n = ' '.join(n.split('-'))
    n = n.split()
    for i in n:
        summa += int(i)
    lessons[line.split()[0]] = summa
print(lessons)
f.close()
