'''Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать 
реализацию с использованием графического интерфейса. Допускается использовать любую графическую 
библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода (со скролингом), 
одно текстовое поле, одна кнопка.'''
import timeit
import re
import tkinter as tk

def alg(n):
    summ=0
    a=[]
    for i in range(1,n,2):
        if int(str(i)[0]) % 2 != 0:
            a.append(i)
            if str(i)[0]==str(i)[-1]:
                summ+=i
    return a,summ
def func(n):
    summ=0
    a = [str(ch) for ch in range(1,n,2)]
    matches=[]
    for el in a:
        match = re.match(r"^[13579]\d*$", el)
        if match:
            if el[0]==el[-1]: summ+=int(el)
            matches.append(int(el))
    return matches,summ
def is_n():
    global n
    n=entry1.get()
    t.delete(1.0,tk.END)
    if n.isnumeric():
        n=int(n)
        if n>0:
            alg_time =timeit.timeit('alg(n)', globals = globals(), number =1)
            func_time = timeit.timeit('func(n)', globals = globals(), number =1)
            te = f'n: {n}\n\nАлгоритмический метод\nПодходящие числа: \n{alg(n)[0]}\nСумма всех чисел, в которых первая и последняя цифры совпадают: {alg(n)[1]}\nВремя выполнение алгоритмическим способом формирования: {alg_time}\n\nФункциональный метод\nПодходящие числа: \n{func(n)[0]}\nСумма всех чисел, в которых первая и последняя цифры совпадают: {func(n)[1]}\nВремя выполнение функциональным способом формирования: {func_time}'
            t.insert(1.0,te)
        else: t.insert(1.0,'Вы ввели некорректное число n. Введите целое число n.')
    else: t.insert(1.0,'Вы ввели некорректное число n. Введите целое число n.')
def quit():
    win.quit()
win = tk.Tk()
win.geometry('700x350')
lbl1 = tk.Label(text='Введите целое число n: ',font='9')
lbl1.grid(row=0, column=0, pady=10)
win.columnconfigure(index=0, weight=350)
win.columnconfigure(index=1, weight=350)
entry1 = tk.Entry(font='9')
entry1.grid(row=0,column=1, pady=10)
btn1 = tk.Button(text='Готово',font='9', command=is_n)
btn1.grid(row=1, column=0, columnspan=2, pady=10)
t = tk.Text(win,height=7,font='9', width = 700)
t.grid(row=2,column=0, columnspan=2, sticky='ew', pady=10)
btn2 = tk.Button(text='Закрыть',font='9', command=quit)
btn2.grid(row=3,column=0,columnspan=2,pady=10)
win.mainloop()

