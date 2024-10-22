import numpy as np
import matplotlib.pyplot as plt
K = int(input('Введите число K: '))
N = int(input('Введите число N от 3 до 100: '))
while True:
    if N<100 and N>2: break
    else: N=int(input('Введите число N от 3 до 100: '))
choice=input('Выберите, каким способом вы хотите заполнить массив:\n1-из файла 2-случайными числами\n')
while True:
    if choice.isnumeric():
        if choice == '1':
            A = np.loadtxt('1.txt',dtype=int, skiprows=0,usecols=list(range(0, N)), max_rows=N)
            break
        elif choice == '2':
            A = np.random.randint(-10,10,(N,N))
            break
        else:
            choice = input('Введите целое число:\n 1-из файла 2-случайными числами\n')
F=np.copy(A)
print(f'Первоначальная матрица А:\n{A}')
print(f'Первоначальная матрица F:\n{F}')
if N%2!=0: nch=1
else: nch=0
s=0
p=1
for x in range(N//2+nch,N):
    for y in range(N//2):
        if (y+1)%2!=0: s+=F[x][y]
        if (x+1)%2==0: p*=F[x][y]
if s>p:
    for x in range(N//2):
        for y in range(N//2):
            F[x][y],F[N-1-x][y]=F[N-1-x][y],F[x][y]
    print('Матрицы В и С были поменяны симметрично')
else:
    for x in range(N//2):
        for y in range(N//2):
            F[x][y],F[x][N//2+nch+y]=F[x][N//2+nch+y],F[x][y]
    print('Матрицы В и Е были поменяны несимметрично')
print(f'Измененная матрица F:\n{F}')
opred = np.linalg.det(A)
sumdiag = np.diagonal(F).sum() + np.diagonal(np.fliplr(F)).sum()
At=np.transpose(A)
print(f'Транспортированная матрица А:\n{At}')
G = np.tril(A)
print(f'Нижняя треугольная матрица G:\n{G}')
if np.linalg.det(G): 
    G=np.linalg.inv(G)
    print(f'Обратная нижняя треугольная матрица G:\n{G}')
A=np.linalg.inv(A)
print(f'Обратная матрица А:\n{A}')
F=np.linalg.inv(F)
print(f'Обратная матрица F:\n{F}')
if opred>sumdiag: result = A*At-K*F
else: result = (At+G-F)*K
print(f'Результат операций:\n{result}')
plt.figure(figsize=(8, 6))
plt.plot(np.diag(F), marker='o', linestyle='-')
plt.title('Линейный график диагональных элементов матрицы F')
plt.xlabel('Номер строки/столбца')
plt.ylabel('Значение элемента')
plt.figure(figsize=(8, 6))
plt.hist(F[0, :], bins=10, label='Строка 1')
plt.hist(F[1, :], bins=10, label='Строка 2')
plt.hist(F[2, :], bins=10, label='Строка 3')
plt.title('Гистограммы элементов по строкам')
plt.legend()
plt.figure(figsize=(8, 6))
plt.hist(F[:, 0], bins=10, label='Столбец 1')
plt.hist(F[:, 1], bins=10, label='Столбец 2')
plt.hist(F[:, 2], bins=10, label='Столбец 3')
plt.title('Гистограммы элементов по столбцам')
plt.legend()
plt.show()