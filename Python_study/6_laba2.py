'''Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта 
формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно 
ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую 
функцию для нахождения оптимального  решения.
Вывести все натуральные числа до n, которые начинаются и заканчиваются нечетной цифрой.
Найти наибольшую сумму цифр среди выведенных чисел, вывести с наибольшим остатком от деления 
на 3, причем это должно быть наибольшее число с данной суммой цифр.
'''
import timeit
import re

def alg(n):
    tsumm=0
    msumm=0
    chislo=0
    a=[]
    for i in range(1,n,2):
        if int(str(i)[0]) % 2 != 0:
            a.append(i)
            for cz in str(i):
                tsumm+=int(cz)
            if tsumm%3==2 and msumm<=tsumm:
                    msumm=tsumm
                    chislo=i
    print(f"Наибольшая сумма цифр в выведенных числах, которая при делении на 3 дает наибольший остаток(2), находится в наибольшем числе {chislo}: {msumm}")
    return a
def func(n):
    tsumm=0
    msumm=0
    chislo=0
    a = [str(ch) for ch in range(1,n,2)]
    matches=[]
    for el in a:
        match = re.match(r"^[13579]\d*$", el)
        if match:
            ch=[]
            for cz in el:
                ch.append(int(cz))
            tsumm=sum(ch)
            if tsumm%3==2 and tsumm>=msumm:
                msumm=tsumm
                chislo=int(el)
            matches.append(int(el))
    print(f"Наибольшая сумма цифр в выведенных числах, которая при делении на 3 дает наибольший остаток(2), находится в наибольшем числе {chislo}: {msumm}")
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
alg_time =timeit.timeit('alg(n)', globals = globals(), number =1)
print(f'Время выполнение алгоритмическим способом формирования: {alg_time}')
print()
print(func(n))
func_time = timeit.timeit('func(n)', globals = globals(), number =1)
print(f'Время выполнение функциональным способом формирования: {func_time}')