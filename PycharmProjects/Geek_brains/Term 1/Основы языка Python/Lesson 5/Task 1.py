f = open("my_file1.txt", 'w')
something = input('Enter something: ')
while something:
    f.write(something + '\n')
    something = input('Enter something: ')

f.close()

