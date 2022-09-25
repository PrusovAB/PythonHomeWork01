# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputAddNumbers(x):
    xyz = ["X", "Y", "Z"]
    array = []
    for i in range(x):
        array.append(input(f"Введите значение {xyz[i]}: "))
    return array


def checkPredic(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


rez = inputAddNumbers(3)

if checkPredic(rez) == True:
    print(f"истинна")
else:
    print(f"ложь")
