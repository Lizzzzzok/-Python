list_ = input('Введите числа через пробел').split()
print([el for el in list_ if list_.count(el) == 1])
