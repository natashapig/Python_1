k,n = map(int,input().split())

f = open("1.txt","r",encoding="utf8")
s = f.readline()
Q = []
while s!='':
    Q.extend(s.split())
    s=f.readline()
for i in range(len(Q)):
    Q[i]=int(Q[i])

a=[]
F=[]
V=[]
At=[]
for i in range(n):
    a.append([0]*n)
    F.append([0]*n)
    V.append([0]*n)
    At.append([0]*n)

for x in range(n):
    for y in range(n):
        a[x][y]=Q[0]
        Q.pop(0)   

for i in range(n):
    for j in range(n):
        F[i][j]=a[i][j]
        At[i][j]=a[i][j]

count=0
for i in range(n):
    for x in range(n):
        for y in range(n):
            if x>i and y<=i and x<(n-1-i) and y<=(n-1-i):
                if (y+1)%2==0 and F[x][y]%2!=0:
                    count+=1

print('Количество чисел во 2 области равно',count)

summa=0
for i in range(n):
    for x in range(n):
        for y in range(n):
            if x<i and y>=i and y<=(n-1-i):
                if (x+1)%2==0:
                    summa+=F[x][y]
print('Сумма в 1 области равна',summa)

if count>summa:
        for x in range(n):
            for y in range(x):
                    if y<(n-1-x):
                        F[x][y],F[y][x]=F[y][x],F[x][y]
        print("Матрица была изменена симметрично")
else:
    for x in range(n):
        for y in range(x):
            if y<(n-1-x):
                    F[x][y],F[y][n-1-x]=F[y][n-1-x],F[x][y]
    print('Матрица была изменена несимметрично')

print()
print('Начальная матрица А:')
for x in range(n):
    for y in range(n):
        print(a[x][y], end = ' ')
    print()

print()
print('Изменённая матрица F:')
for x in range(n):
    for y in range(n):
        print(F[x][y], end = ' ')
    print()  
print()        

print('Матрица F, yмноженная на',k,':')
for x in range(n):
    for y in range(n):
        F[x][y]*=k
        print(F[x][y], end = ' ')
    print()

for i in range(n):
    for j in range(n):
        V[i][j]=F[i][j]


p=0
print()
print('Матрица F, перемноженная с матрицей А:')
for x in range(n):    
    for y in range(n):
        for i in range(n):
            p+=F[x][i]*a[i][y]
        V[x][y]=p
        p=0
        print(V[x][y], end = ' ')
    print()

print()
print('Транспортированная матрица А:')
for x in range(n):
    for y in range(x):
        At[x][y],At[y][x]=At[y][x],At[x][y]
for x in range(n):
    for y in range(n):
        print(At[x][y], end = ' ')
    print()

print()
print('Перемноженная транспортированная матрица А:')
for x in range(n):
    for y in range(n):
        At[x][y]*=k
        print(At[x][y], end = ' ')
    print()
print()

print('Результат операций:')
for x in range(n):
    for y in range(n):
        V[x][y]-=At[x][y]
        print(V[x][y], end = ' ')
    print()        
