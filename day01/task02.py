# конвертер секунд
secund = int(input("Введи число секунд: "))
minuts = round(secund/60)
chas = round(minuts/60)
day = round(chas/24)
print(f'{day} дн. {chas-day*24} ч. {minuts-chas*60} мин. {secund-minuts*60} сек.')