'''Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать 
реализацию с использованием графического интерфейса. Допускается использовать любую графическую 
библиотеку питона. Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода (со скролингом), 
одно текстовое поле, одна кнопка.'''
from textwrap import wrap
import timeit
import re
import tkinter as tk
def alg(n):
    msumm,chislo=0,0
    a=[]
    for i in range(1,n,2):
        tsumm=0
        if int(str(i)[0]) % 2 != 0:
            a.append(i)
            for cz in str(i):
                tsumm+=int(cz)
            if tsumm%3==2 and msumm<=tsumm:
                    msumm=tsumm
                    chislo=i
    return a,msumm,chislo
def func(n):
    tsumm,msumm,chislo=0,0,0
    a = [str(ch) for ch in range(1,n,2)]
    matches=[]
    for el in a:
        match = re.match(r"^[13579]\d*$", el)
        if match:
            ch=[]
            for cz in el:
                ch.append(int(cz))
            tsumm=sum(ch)
            if tsumm%3==2 and msumm<=tsumm:
                msumm=tsumm
                chislo=int(el)
            matches.append(int(el))
    return matches,msumm,chislo
def is_n():
    btn1['state']='disabled'
    global n
    n=entry1.get()
    t.focus()
    t.delete(1.0,tk.END)
    if n.isnumeric():
        n=int(n)
        if n>0:
            alg_time =timeit.timeit('alg(n)', globals = globals(), number =1)
            func_time = timeit.timeit('func(n)', globals = globals(), number =1)
            te = f'n: {n} \n\nАлгоритмический метод\nПодходящие числа: \n{alg(n)[0]} \nНаибольшая сумма цифр в выведенных числах, которая при делении на 3 дает наибольший остаток(2), находится в наибольшем числе {alg(n)[2]}: {alg(n)[1]}\nВремя выполнение алгоритмическим способом формирования: {alg_time}\n\nФункциональный метод\nПодходящие числа: \n{func(n)[0]}\nНаибольшая сумма цифр в выведенных числах, которая при делении на 3 дает наибольший остаток(2), находится в наибольшем числе {func(n)[2]}: {func(n)[1]}\nВремя выполнение функциональным способом формирования: {func_time}'
            t.insert(1.0,te)
            scrollbar = tk.Scrollbar(orient="vertical", command = t.yview)
            t["yscrollcommand"]=scrollbar.set
            scrollbar.grid(row=3,column=0,columnspan=2,sticky='nse',pady=10)
            t.yview_scroll(number=1, what="units")
            scrollbar.config(command=t.yview)
        else: t.insert(1.0,'Вы ввели некорректное число n. Введите натуральное число n.')
    else: t.insert(1.0,'Вы ввели некорректное число n. Введите натуральное число n.')
def quit(): win.quit()
win = tk.Tk()
win.geometry('700x450')
win.config(background='#dbeda4')
win.title('Программа нахождения всех натуральных чисел до заданного n с условием.')
lblif = tk.Label(background='#dbeda4',foreground='#303817',font='9',text='Программа нахождения всех натуральных чисел до заданного, у которых первая и последняя цифры нечетные.')
lblif.grid(row=0,column=0,columnspan=2,pady=10)
win.update() 
width = lblif.winfo_width()
char_width = width / len(lblif['text'])
wrapped_text = '\n'.join(wrap(lblif['text'], int(700 / char_width)))
lblif['text'] = wrapped_text
lbl1 = tk.Label(background='#dbeda4',foreground='#303817',text='Введите натуральное число n: ',font='9')
lbl1.grid(row=1, column=0, pady=10)
win.columnconfigure(index=0, weight=350)
win.columnconfigure(index=1, weight=350)
btn1 = tk.Button(foreground='white',background='#596929',text='Выполнить вычисления',font='9', command=is_n, state='disabled')
btn1.grid(row=2, column=0, columnspan=2, pady=10)
var = tk.StringVar()
def btnvis(*args):
    if entry1.get()!='': btn1['state']='normal'
var.trace_add("write", btnvis)
entry1 = tk.Entry(font='9',foreground='#303817', textvariable=var)
entry1.grid(row=1,column=1, pady=10)
entry1.focus()
t = tk.Text(win,height=7,font='9', width = 700)
t.grid(row=3,column=0, columnspan=2, sticky='ew', pady=10)
btn2 = tk.Button(foreground='white',background='#596929',text='Закрыть программу',font='9', command=quit)
btn2.grid(row=4,column=0,columnspan=2,pady=10)
win.mainloop()

