class Road:
    def __init__(self, _length, _width, volume, depth):
        self._length = _length
        self._width = _width
        self.volume = volume
        self.depth = depth

    def mass(self):
        return f'Mass in kg: {self._width * self._length * self.depth * self.volume}'


result = Road(20, 5000, 25, 5)
print(result.mass())
