# Python. HW_1

# 1) Создать переменную типа String
a_string = 'стринговая_перемннная'

# 2) Создать переменную типа Integer
b_int = 756

# 3) Создать переменную типа Float
c_float = 23.22

# 4) Создать переменную типа Bytes
d = "Bytes"
d_bytes = bytes(d, "utf-8")

# 5) Создать переменную типа List
e_list = [a_string, b_int, c_float]

# 6) Создать переменную типа Tuple
f_tuple = (12, 'HI_everyone', 122.5,)

# 7) Создать переменную типа Set
g_set = {'a', 'b', 'c', 'd'}

# 8) Создать переменную типа Frozen set
h = [1, 2, 3, 4, 5]
h_frozen_set = frozenset(h)

# 9) Создать переменную типа Dict
i_dict = {'anna': 5, 'veronika': 3, "ksenia": 4}

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print('#1 Task', a_string, type(a_string))
print('#2 Task', b_int, type(b_int))
print('#3 Task', c_float, type(c_float))
print('#4 Task', d_bytes, type(d_bytes))
print('#5 Task', e_list, type(e_list))
print('#6 Task', f_tuple, type(f_tuple))
print('#7 Task', g_set, type(g_set))
print('#8 Task', h_frozen_set, type(h_frozen_set))
print('#9 Task', i_dict, type(i_dict))

# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
a, b = "Petya", "Masha"
ab_sum = a + b
print('#11 Task', ab_sum)

# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
c, d = int(221), int(34)
cd_sum = d + c
print('#12 Task', cd_sum)

# 13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
div_cd = c / d
print('#13 Task', div_cd)

# 14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
mult_cd = c * d
print('#14 Task', mult_cd)

# 15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
div_no_rem_cd = c // d
print('#15 Task', div_no_rem_cd)

# 16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
rem_with_div_cd = c % d
print('#16 Task', rem_with_div_cd)

