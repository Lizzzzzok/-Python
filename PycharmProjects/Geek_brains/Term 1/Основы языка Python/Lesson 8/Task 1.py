class Data:
    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)

    @classmethod
    def numbers(cls, d_m_y):
        number = (''.join(d_m_y.split())).split('-')
        return int(number[0]), int(number[1]), int(number[2])

    @staticmethod
    def okay(d, m, y):
        long = [1, 3, 5, 7, 8, 10, 12]
        short = [4, 6, 9, 11]
        if 0 < y:
            if 0 < m < 13:
                if m in long:
                    if 0 < d < 32:
                        return 'The date is valid.'
                    else:
                        return 'You entered invalid day.'
                elif m in short:
                    if 0 < d < 31:
                        return 'The date is valid.'
                    else:
                        return 'You entered invalid day.'
                elif m not in long and m not in short and y % 4 == 0:
                    if 0 < d < 30:
                        return 'The date is valid.'
                    else:
                        return 'You entered invalid day.'
                else:
                    if 0 < d < 29:
                        return 'The date is valid.'
                    else:
                        return 'You entered invalid day.'
            else:
                return 'You entered invalid month.'
        else:
            return 'You entered invalid year.'


print(Data.numbers('22 - 11 - 2021'))
print(Data.okay(22, 11, 2021))
print(Data.okay(22, 11, -9))
print(Data.okay(22, 13, 2021))
print(Data.okay(31, 4, 2021))
print(Data.okay(29, 2, 2021))
print(Data.okay(29, 2, 2020))
