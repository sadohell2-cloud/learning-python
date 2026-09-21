#калькулятор ИМТ
ves = float(input('Привет, это калькулятор ИМТ\nВведите пожалуйста ваш вес: '))
rost = float(input(f'Итак, ваш вес: {ves}\nТеперь нужен рост(сантиметры): '))
imt = round(float(ves / ((rost/100)**2)), 2)
def kategori(q):
    if q<=18.5: print('У вас недовес')
    if q>18.5 and q<25 : print('У вас нормальный вес')
    if q>25: print('У вас перевес')
print(f'Ваш ИМТ = {imt}')
kategori(imt)
