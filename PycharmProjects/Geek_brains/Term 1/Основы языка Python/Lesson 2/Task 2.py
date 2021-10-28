element = input('Введите элемент: ')
list_ = []
while element:
    list_.append(element)
    element = input('Введите элемент: ')

for i in range(0, len(list_[:-1]), 2):
    list_[i], list_[i + 1] = list_[i + 1], list_[i]
print(list_)
