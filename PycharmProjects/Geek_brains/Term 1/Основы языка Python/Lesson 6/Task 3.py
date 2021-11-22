class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Wage": wage, "Bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('Wage') + self._income.get('Bonus')


info = Position('Liza', 'Kozerenko', 'Manager', 50000, 250000)
print(info.get_full_name())
print(info.get_total_income())
