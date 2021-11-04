def devision(*args):
    if args[1] == 0:
        return 'You can not divide by zero'
    return args[0] / args[1]


print(devision(int(input('Enter a number: ')), int(input('Enter the second number: '))))
