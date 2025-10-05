massiv=list(map(int,input('Введите массив целых чисел с пробелом: ').split()))
numbers=[]

for num in massiv:
    if num%2!=0:
        numbers.append(num)
if not numbers:
    print('В массиве нет нечетных чисел')
else:
    numbers.sort(reverse=True)
    print(numbers)
