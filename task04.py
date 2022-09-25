# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

numberLocation = int(input("Введите номер кординаты от 1 до 4: "))


def SearcMeaning(number):
    if numberLocation == 1:
        print("X > 0 and Y > 0")
    elif numberLocation == 2:
        print("X < 0 and Y > 0")
    elif numberLocation == 3:
        print("X < 0 and Y < 0")
    elif numberLocation == 4:
        print("X > 0 and Y < 0")
    else:
        print("Нет такой четверти")


SearcMeaning(numberLocation)
