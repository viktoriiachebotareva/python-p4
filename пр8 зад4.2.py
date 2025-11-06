N=int(input('Введите размер N: '))
matriza=[]
print('Введите элементы матрицы построчно: ')

for i in range(N):
    line=list(map(int,input().split()))
    matriza.append(line)

for i in range(N):
    for j in range(N):
        if matriza[i][j]<0:
            matriza[i][j]=0
        else:
            matriza[i][j]=1

print('Нижняя треугольная матрица: ')
for i in range(N):
    for j in range(N):
        if i>=j:
            print(matriza[i][j],end='')
        else:
            print('',end='')
    print()
