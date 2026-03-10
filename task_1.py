time_str = '1h 45m,360s,25m,30m 120s,2h 60s'

values = time_str.split(',')

total_minutes = 0

for value in values:
    # Разделяем значение на части по пробелу (если несколько единиц)
    parts = value.split()
    for part in parts:
        # Извлекаемaя числовую часть, удаляя возможные буквы h, m, s
        num_str = part.replace('h', '').replace('m', '').replace('s', '')
        number = int(num_str)


        if 'h' in part:
            total_minutes += number * 60
        elif 'm' in part:
            total_minutes += number
        elif 's' in part:
            # Секунды кратны 60, поэтому переводим в минуты делением на 60
            total_minutes += number // 60

print(total_minutes)