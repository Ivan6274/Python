import random
print('''Task #7
Сделать скрипт используя функцию input().
    1. Функция должна на вход принимать целое число.
    2. Выводить должна "Вы ввели число = (введённое число) которое (меньше/больше/равно) 30"  
''')
r = int(input("Введите целое число - "))
if r > 30:
    print("Вы ввели число =", r, "которое больше 30")
elif r < 30:
    print("Вы ввели число =", r, "которое меньше 30")
else:
    print("Вы ввели число =", r, "которое равно 30")
print("")
print('''Task #8
Сделать скрипт используя функцию input().
    1. Функция должна на вход принимать целое число.
    2. Внутри функции должно сгенерироваться рандомное целое число 
    3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу"
''')
v = int(input("Введите целое число - "))
v1 = random.randint(1, 100)
print("Сгенерированное число =", v1)
if v > v1:
    print("Вы ввели число =", v, "которое больше сгенерированного числа", v1)
elif v < v1:
    print("Вы ввели число =", v, "которое меньше сгенерированного числа", v1)
else:
    print("Вы ввели число =", v, "которое равно сгенерированному числу", v1)
print("")
print('''Task #9
Сделать скрипт используя функцию input().
    1. Функция должна на вход принимать целое число.
    2. Внутри функции должно сгенерироваться рандомных 2 целых числа 
    3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"
''')
q = int(input("Введите целое число - "))
q1, q2 = random.randint(1, 100), random.randint(1, 100)
print("Первое сгенерированное число =", q1)
print("Второе сгенерированное число =", q2)

if q > q1:
    if q > q2:
        print("Вы вели число =", q, " которое больше первого сгенерированного числа", q1,
              " и больше второго сгенерированного числа", q2)
    elif q < q2:
        print("Вы вели число =", q, " которое больше первого сгенерированного числа", q1,
              " и меньше второго сгенерированного числа", q2)
    else:
        print("Вы вели число =", q, " которое больше первого сгенерированного числа", q1,
              " и равно второму сгенерированному числу", q2)
elif q < q1:
    if q > q2:
        print("Вы вели число =", q, " которое меньше первого сгенерированного числа", q1,
              " и больше второго сгенерированного числа", q2)
    elif q < q2:
        print("Вы вели число =", q, " которое меньше первого сгенерированного числа", q1,
              " и меньше второго сгенерированного числа", q2)
    else:
        print("Вы вели число =", q, " которое меньше первого сгенерированного числа", q1,
              " и равно второму сгенерированному числу", q2)
else:
    if q > q2:
        print("Вы вели число =", q, " которое равно первого сгенерированного числа", q1,
              " и больше второго сгенерированного числа", q2)
    elif q < q2:
        print("Вы вели число =", q, " которое равно первого сгенерированного числа", q1,
              " и меньше второго сгенерированного числа", q2)
    else:
        print("Вы вели число =", q, " которое равно первого сгенерированного числа", q1,
              " и равно второму сгенерированному числу", q2)