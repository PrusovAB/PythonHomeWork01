# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.


def add_dot():
    dot_NumberOne = ["X", "Y"]
    dot_NumberTwo = ["X", "Y"]
    for i in range(2):
        dot_NumberOne[i] = int(
            input(f"Введите значение первой точки по {dot_NumberOne[i]}: "))

    for i in range(2):
        dot_NumberTwo[i] = int(
            input(f"Введите значение первой точки по {dot_NumberTwo[i]}: "))

    return dot_NumberOne, dot_NumberTwo


array = add_dot()


def calculateNumber(x):
    lengthSegment = ((x[1][0] - x[0][0]) ** 2 +
                     (x[1][1] - x[0][1]) ** 2) ** (0.5)
    return lengthSegment


rez = calculateNumber(array)

print(round(rez, 2))
