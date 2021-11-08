from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


list_ = [el for el in range(100, 1001) if el % 2 == 0]
print(list_)
print(reduce(my_func, list_))
