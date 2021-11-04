def my_func(*args):
    if args[0] >= args[2] and args[1] >= args[2]:
        return args[0] + args[1]
    elif args[1] < args[0] < args[2]:
        return args[0] + args[2]
    else:
        return args[1] + args[2]


print(my_func(int(input('Enter a number: ')),int(input('Enter a number: ')),int(input('Enter a number: '))))
