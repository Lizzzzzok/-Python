def my_func(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return 1 / (x * my_func(x, abs(y) - 1))
    else:
        return x * my_func(x, y - 1)


print(my_func(int(input('Enter positive number: ')), int(input('Enter negative number: '))))
