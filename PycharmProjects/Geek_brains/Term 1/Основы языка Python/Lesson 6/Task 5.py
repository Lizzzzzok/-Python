class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Start of drawing: {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Now the drawing <{self.title}> will be made by a pen.'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Now the drawing <{self.title}> will be made by pencil.'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Now the drawing <{self.title}> will be made by handle.'


pen = Pen('Mona Lisa')
pencil = Pencil('3 Bears')
handle = Handle('Winter in London')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
