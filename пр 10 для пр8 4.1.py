input_file = open('Чеботарева_Виктория_УБ-51_ввод_4_1.txt', 'r')
output_file = open('Чеботарева_Виктория_УБ-51_вывод_4_1.txt', 'w')

lins, columns = map(int, input_file.readline().split())

matrix = []
sums=[]
for i in range(lins):
    row = list(map(int, input_file.readline().split()))
    matrix.append(row)
    sums.append(sum(row))

sums = [sum(row) for row in matrix]

max_sum = max(sums)
min_sum = min(sums)
max_index = sums.index(max_sum)
min_index = sums.index(min_sum)

output_file.write('Исходная матрица:\n')
for row in matrix:
    output_file.write(' '.join(map(str, row)) + '\n')

output_file.write('\nРезультаты:\n')
output_file.write('Максимальная сумма: ' + str(max_sum) + ' (строка ' + str(max_index + 1) + ')\n')
output_file.write('Минимальная сумма: ' + str(min_sum) + ' (строка ' + str(min_index + 1) + ')\n')

input_file.close()
output_file.close()


