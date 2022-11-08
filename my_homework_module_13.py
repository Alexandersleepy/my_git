kolichestvo = int(input("Введите количество билетов: "))
cena = 0
summa = 0
for i in range(kolichestvo):

    vozrast = int(input(f"Введите возраст посетителя № {i+1}: "))
    if vozrast < 18:
        cena = 0
        summa = cena + summa

    elif 18 <= vozrast < 25:
        cena = 990
        summa = cena + summa

    elif vozrast >= 25:
        cena = 1390
        summa = cena + summa

if kolichestvo > 3:
    skidka = summa / 100 * 10
    print(f"Общая сумма за билеты: {summa - skidka} Руб.")

else:
    print(f"Общая сумма за билеты: {summa} Руб.")
