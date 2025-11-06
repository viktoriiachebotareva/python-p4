lins=int(input('Введите количество строк: '))
columns=int(input('Ввдите количество столбцов: '))
matriza=[]
print('Ввдите элементы матрицы построчно: ')
for i in range(lins):
    line=list(map(int,input().split()))
    matriza.append(line)

summa=[]
for i in range(lins):
    line_sum=sum(matriza[i])
    summa.append(line_sum)
    print('Сумма строки: ',line_sum)

max_sum=max(summa)
min_sum=min(summa)
max_index=summa.index(max_sum)
min_index=summa.index(min_sum)

print('Строка с наибольшей суммой: ',matriza[max_index])
print(max_sum)

print('Строка с наименьшей суммой: ',matriza[min_index])
print(min_sum)
