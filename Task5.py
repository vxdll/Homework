# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
#                 - A (3,6); B (2,1) -> 5,09
#                 - A (7,-5); B (1,-1) -> 7,21

import math
xa = int(input("Введите координату Xa = "))
ya = int(input("Введите координату Ya = "))
xb = int(input("Введите координату Xb = "))
yb = int(input("Введите координату Yb = "))
result = math.sqrt(((xb - xa)**2) + ((yb - ya)**2))
print(f"A ({xa},{ya}; B ({xb},{yb}) -> {round(result,2)}")
