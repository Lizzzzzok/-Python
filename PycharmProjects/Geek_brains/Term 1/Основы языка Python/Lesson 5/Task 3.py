my_f = open("file_task3.txt", "r")
average_oklad = 0
n = 0
for line in my_f.read().split('\n'):
    if int(line.split()[1]) < 20000:
        print(line.split()[0])
    average_oklad += int(line.split()[1])
    n += 1
print(f'Average salary is: {average_oklad / n}')
my_f.close()
