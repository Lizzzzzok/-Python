class Sklad:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}.'


class Orgtech:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = []
        self.info = {'Name: ': name, 'Price: ': price, 'Quantity: ': quantity}

    def give(self):
        try:
            name = input('Enter a name of a product: ')
            price = input('Enter a price of a product: ')
            amount = input('Enter a quantity of a product: ')
            new = {'Name: ': name, 'Price: ': int(price), 'Quantity: ': int(amount)}
            self.items.append(new)
            print(f'Current items: {self.items}')
        except:
            print('The data is invalid')

        n = input('To continue press 1, to exit press 0: ')
        if n == '1':
            return Orgtech.give(self)
        else:
            return f'Finish. Items available: {self.items}'


class Printer(Orgtech):
    def __init__(self, time, name, price, quantity):
        super().__init__(name, price, quantity)
        self.time = time


class Scanner(Orgtech):
    def __init__(self, time, name, price, quantity):
        super().__init__(name, price, quantity)
        self.time = time


class Kserox(Orgtech):
    def __init__(self, time, name, price, quantity):
        super().__init__(name, price, quantity)
        self.time = time


#  я не поняла что надо писать в дочерних классах

item1 = Printer('hp', 2000, 5, 10)
item2 = Scanner('Canon', 1200, 5, 10)
item3 = Kserox('Xerox', 1500, 1, 15)
print(item1.give())

# короче я запуталась, извините) Но я старалась!))
