from random import randint

print('Введите число К:')
flag = 0
while flag != 1:
    K = input()
    if K.isnumeric():
        K = int(K)
        flag = 1
    else:
        print('Введите целое число К:')

flag = 0    
print('Введите число N (размер матрицы) не менeе 3, не более 99:')
while flag != 1:
    N = input()
    if N.isnumeric():
        N = int(N)
        if N > 2 and N < 100:
            flag = 1
        else:
            print('Введённое число должно быть не менее 3 и не более 99. Введите число N:')
    else:
        print('Введите целое число N:')

A = []
F = []
V = []
At = []
for i in range(N):
    A.append([0]*N)
    F.append([0]*N)
    V.append([0]*N)
    At.append([0]*N)

print('Как Вы хотите заполнить матрицу?\n1 - из файла 2 - случайными числами')

flag = 0
choice = 0
while flag != 1:
    if choice != '2':
        choice = input()
    if choice.isnumeric():
        if int(choice) == 1:
            f = open('1.txt','r',encoding='utf8')
            rows = 0
            for x in range(N):
                s = f.readline().split()
                if s == []:
                    break
                for y in range(N):
                    A[x][y] = s[y]
                rows += 1
            if rows != N:
                print('Данных из файла не хватает, чтобы заполнить матрицу.\nОна будет автоматически заполнена случайными числами.\nЧтобы продолжить, нажмите Enter')
                input()
                choice = '2'
            else:
                print('Вы заполнили матрицу А из файла.')
                flag = 1
        else:
            if int(choice) == 2:
                print('Вы заполнили матрицу случайными числами от -10 до 10.')
                for x in range(N):
                    for y in range(N):
                        A[x][y] = randint(-10,10)
                flag = 1
            else:
                print('Введено неверное число. Ответом на вопрос должно быть число:\n 1 - из файла 2 - случайными числами')
    else:
        print('Ответом на вопрос должно быть целое число:\n 1 - из файла 2 - случайными числами')

for x in range(N):
    for y in range(N):
        A[x][y] = int(A[x][y])
        F[x][y] = A[x][y]
        At[x][y] = A[x][y]

count = 0
for i in range(N):
    for x in range(N):
        for y in range(N):
            if x > i and y <= i and x < (N-1-i) and y <= (N-1-i):
                if (y+1)%2 == 0 and F[x][y]%2 != 0:
                    count += 1
print(f'Количество нечетных чисел в четных столбцах во 2 области равно {count}.')

summa = 0
for i in range(N):
    for x in range(N):
        for y in range(N):
            if x < i and y >= i and y <= (N-1-i):
                if (x+1)%2 == 0:
                    summa += F[x][y]
print(f'Cумма чисел в четных строках в 1 области равна {summa}.')

if count > summa:
        for x in range(N):
            for y in range(x):
                    if y < (N-1-x):
                        F[x][y], F[y][x] = F[y][x], F[x][y]
        print('Матрица F была изменена симметрично.')
else:
    for x in range(N):
        for y in range(x):
            if y < (N-1-x):
                    F[x][y], F[y][N-1-x] = F[y][N-1-x], F[x][y]
    print('Матрица F была изменена несимметрично.')

print()
print('Начальная матрица А:')
for x in range(N):
    for y in range(N):
        print(A[x][y], end = ' ')
    print()

print()
print('Начальная матрица F:')
for x in range(N):
    for y in range(N):
        print(F[x][y], end = ' ')
    print()          

print()
print(f'Матрица F, умноженная на {K}:')
for x in range(N):
    for y in range(N):
        F[x][y] *= K
        print(F[x][y], end = ' ')
    print()

for i in range(N):
    for j in range(N):
        V[i][j] = F[i][j]


prom = 0
print()
print('Матрица F, перемноженная с матрицей А:')
for x in range(N):    
    for y in range(N):
        for i in range(N):
            prom += F[x][i] * A[i][y]
        V[x][y] = prom
        prom = 0
        print(V[x][y], end = ' ')
    print()

print()
print('Транспортированная матрица А:')
for x in range(N):
    for y in range(x):
        At[x][y], At[y][x] = At[y][x], At[x][y]
for x in range(N):
    for y in range(N):
        print(At[x][y], end = ' ')
    print()

print()
print('Транспортированная матрица А, умноженная на К:')
for x in range(N):
    for y in range(N):
        At[x][y] *= K
        print(At[x][y], end = ' ')
    print()

print()
print('Результат операции (К*A)*А–(K * At):')
for x in range(N):
    for y in range(N):
        V[x][y] -= At[x][y]
        print(V[x][y], end = ' ')
    print()       
