my_f = open("file_task2.txt", "r")
stroki = 0
for line in my_f.read().split('\n'):
    words = 0
    for word in line.split():
        words += 1
    stroki += 1
    print(f'Number of words in line {stroki}: {words}')
print(f'Number of strings in the file: {stroki}')
my_f.close()
