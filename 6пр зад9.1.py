N=int(input('Введите количество элементов массива: '))
num=[]
for i in range(N):
    num.append(float(input('Введите элемент: ')))
min_elements=min(num, key=abs)
print(min_elements, num[::-1])
