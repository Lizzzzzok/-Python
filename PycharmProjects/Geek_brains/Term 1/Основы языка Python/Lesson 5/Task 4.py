my_f = open("file_task4.txt", "r")
f = open("file2_task4.txt", 'w')
l = ['Один', 'Два', 'Три', 'Четыре']
i = 0
for line in my_f.read().split('\n'):
    f.write(l[i] + ' ' + line.split()[1] + ' ' + line.split()[2] + '\n')
    i += 1
f.close()
my_f.close()
