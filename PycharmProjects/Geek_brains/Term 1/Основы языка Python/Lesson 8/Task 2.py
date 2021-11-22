class Division:
    def __init__(self, number, divider):
        self.number = number
        self.divider = divider

    @staticmethod
    def okay(number, divider):
        try:
            return number / divider
        except:
            return 'Division by zero'


print(Division.okay(10, 5))
print(Division.okay(10, 0))
