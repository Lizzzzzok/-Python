seconds = int(input("Введите время в секундах "))
hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
time = ''
if hours < 10:
    time += f'0{hours}:'
else:
    time += f'{hours}:'

if minutes < 10:
    time += f'0{minutes}:'
else:
    time += f'{minutes}:'

new_sec = seconds - (hours * 3600 + minutes * 60)

if new_sec < 10:
    time += f'0{new_sec}'
else:
    time += f'{new_sec}'

print(f"Время в формате чч:мм:сс: {time}")
