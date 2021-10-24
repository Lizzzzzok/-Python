profit = float(input("Введите выручку фирмы: "))
costs = float(input("Введите издержки фирмы: "))
if profit > costs:
    print(f"Фирма работает прибыльно. Выручка составила {profit / costs:.2f}")
    employers = int(input("Введите количество сотрудников фирмы: "))
    print(f"Прибыль фирмы в расчёте на одного сторудника сотавила: {profit / employers:.2f}")
elif profit < costs:
    print("Фирма работает в убыток")
else:
    print("Фирма работает в ноль")
