goods = []
amount = int(input('Введите количество товаров: '))
for i in range(amount):
    name = input('Введите название товара: ')
    price = int(input('Ведите стоимость товара как натуральное число: '))
    quantity = int(input('Введите количество товара как натуральное число: '))
    type_ = input('Введите единицы измерения товара: ')
    dict_ = {'Название': name, 'Цена': price, 'Количество': quantity, 'Ед.': type_}
    tuple_ = (i + 1, dict_)
    goods.append(tuple_)

names = []
prices = []
quantities = []
types = []
for i in goods:
    names.append(i[1].get('Название'))
    prices.append(i[1].get('Цена'))
    quantities.append(i[1].get('Количество'))
    types.append(i[1].get('Ед.'))
analytics = {'Название': names, 'Цена': prices, 'Количество': quantities, 'Ед.': types}
print(analytics)

