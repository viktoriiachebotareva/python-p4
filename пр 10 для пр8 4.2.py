input_filename = 'Чеботарева_Виктория_УБ-51_ввод_4_2.txt'
output_filename = 'Чеботарева_Виктория_УБ-51_вывод_4_2.txt'

with open(input_filename, 'r') as file:
    N = int(file.readline())
    matrix = []
    
    for x in range(N):
        row = list(map(int, file.readline().split()))
        matrix.append(row)

for i in range(N):
    for j in range(N):
        if matrix[i][j] < 0:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 1

with open(output_filename, 'w') as file:
    file.write('Нижняя треугольная матрица:\n')
    
    for i in range(N):
        for j in range(N):
            if i >= j:
                file.write(str(matrix[i][j]))
        file.write('\n')  

