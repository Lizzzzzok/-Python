def salary(*args):
    return f'Заработная плата сотрудника: {args[0] * args[1] + args[2]}'


print(salary(int(input('Выработка в часах: ')),
             int(input('Ставка в час: ')), int(input('Премия: '))))
