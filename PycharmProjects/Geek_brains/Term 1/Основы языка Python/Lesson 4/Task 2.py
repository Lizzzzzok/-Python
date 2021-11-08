my_list = input('Введите числа через пробел: ').split()
new_list = [(el) for ind, el in enumerate(my_list) if el > my_list[ind - 1]]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")
