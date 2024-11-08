'''Задана рекуррентная функция. Область определения функции – натуральные числа. Написать 
программу сравнительного вычисления данной функции рекурсивно и итерационно. Определить границы 
применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования 
времени вычисления представить в табличной форме. Обязательное требование – минимизация времени 
выполнения и объема памяти. F(1)=1,F(n)= (-1)^n*(F(n–1) + (n + 1)! / (2n)!), при n > 1'''
from timeit import Timer
from functools import partial
import math
n=input('Введите натуральное число n > 1: ')
while True:
    if n.isnumeric():
        n=int(n)
        if n>1: break
    n = input('Вы неправильно ввели n. Введите натуральное число n > 1: ')
def fact(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial
def recursive_f(n):
  if n == 1: return 1
  else:
    try: return (-1)**n * (recursive_f(n - 1) + fact(n + 1) / fact(2*n))
    except: return 0
def iterative_f(n):
    f = 1
    for i in range(2, n + 1): f = (-1)**i * (f + fact(i + 1) / fact(2*i))
    return f
def compare_methods(n):
    print(f"n: {n}")
    recursive_result = recursive_f(n)
    if recursive_result==0:
        print('Невозможно вычислить эту функцию рекурсивно.')
    else:
        recursive_time = Timer(partial(recursive_f,n)).timeit(number=1000)
        print(f"Рекурсивный результат: {recursive_result}")
        print(f"Время рекурсивного вычисления: {recursive_time:.6f} секунд")
    iterative_result = iterative_f(n)
    iterative_time = Timer(partial(recursive_f,n)).timeit(number=1000)
    print(f"Итеративный результат: {iterative_result}")
    print(f"Время итеративного вычисления: {iterative_time:.6f} секунд")
compare_methods(n)
print("Границы применимости:")
print("Рекурсивный подход: подходит для небольших значений n, так как время вычисления растет экспоненциально.")
print("Итеративный подход: более эффективен для больших значений n, так как время вычисления линейно зависит от n.")