f = open('3.txt', 'r')
d={
    '0':'ноль',
    '2':'два',
    '4':'четыре',
    '6':'шесть',
    '8':'восемь',
}
s = f.readline().split()
while s!=[]:
    for i in range(len(s)):
        if s[i].isnumeric() and int(s[i][0])%2!=0:
            print()
            for j in s[i]:
                if int(j)%2==0: print(d[j],end='')
                else: print(j, end='')
    s = f.readline().split()
