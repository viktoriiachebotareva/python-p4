massiv=list(map(int, input('Введите массив целых чисел: ').split()))
max_element=max(massiv)
max_index=massiv.index(max_element)
print(max_element, max_index)
