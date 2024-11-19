'''Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта 
формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно 
ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую 
функцию для нахождения оптимального  решения.
Вывести все натуральные числа до n, которые начинаются и заканчиваются нечетной цифрой.
'''
from timeit import Timer
from functools import partial
import re
def alg(n):
    a=[]
    for i in range(1,n):
        if int(str(i)[0]) % 2 != 0 and int(str(i)[-1]) % 2 != 0:
            a.append(i)
    return a
def func(n):
    a = str([ch for ch in range(1,n,2)])
    matches=[]
    for el in a:
        match = re.match(r"^[13579]\d*[13579]?$", el)
        if match: matches.append(int(el))
    return matches
n=input('Введите целое число n: ')
while True:
    if n.isnumeric():
        n=int(n)
        if n>0: break
        else: n=input('Вы ввели некорректное число n. Введите целое число n: ')
    else: n=input('Вы ввели некорректное число n. Введите целое число n: ')
print(f'n: {n}')
print()
print(alg(n))
alg_time = Timer(partial(alg,n)).timeit(number=1000)
print(f'Время выполнение алгоритмическим способом формирования: {alg_time}')
print()
print(func(n))
func_time = Timer(partial(alg,n)).timeit(number=1000)
print(f'Время выполнение функциональным способом формирования: {func_time}')