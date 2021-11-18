class Fabric:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def palto_sq(self):
        return self.width / 6.5 + 0.5

    def costume_sq(self):
        return self.height * 2 + 0.3

    @property
    def total_sq(self):
        return f'Total square of fabric needed is: {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}'

    # Как обратиться из функции в другую функцию? Хочу чтобы в total_sq было не то, что я написала
    # а чтобы мы суммировали результат двух функций выше.


class Palto(Fabric):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.palto_sqr = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Square of the fabric spent on a coat: {self.palto_sqr}'


class Costume(Fabric):
    def __init__(self, height, width):
        super().__init__(height, width)
        self.costume_sqr = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Square of the fabric spent on a costume: {self.costume_sqr}'


palto = Palto(1, 3)
costume = Costume(3, 2)
print(palto.total_sq)
print(costume.total_sq)
