# #Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
#                 - 6 -> да
#                 - 7 -> да
#                 - 1 -> нет

num_date = int(input("Введите день недели: "))
if 6 <= num_date <= 7:
    print(f"{num_date} -> да")
else:
    print(f"{num_date} -> нет")
