a = int(input("Введите сколько км пробежал спортсмен в первый день: "))
b = int(input("Введите сколько км должен пробежать спортсмен: "))
total_days = 1
while a < b:
    a = a + (0.1 * a)
    total_days += 1
print(f"Спортсмен пробежит требуемое количество километров на {total_days} день")
