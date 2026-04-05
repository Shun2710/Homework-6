# Task 6.2

n = int(input())

days = n // 86400
n %= 86400

hours = n // 3600
n %= 3600

minutes = n // 60
seconds = n % 60

if 11 <= days % 100 <= 14:
    day_word ="дней"
elif days % 10 == 1:
    day_word = "день"
elif 2 <= days % 10 <= 4:
    day_word = "дни"
else:
    day_word = "дней"

print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")