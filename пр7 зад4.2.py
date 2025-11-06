def form_circil(x,y,a,b,R):
    form=(x-a)**2+(y-b)**2
    return form<R**2
a=float(input('Введите a: '))
b=float(input('Введите b: '))
R=float(input('Введите R: '))

p1=float(input('Введите p1: '))
p2=float(input('Введите p2: '))
f1=float(input('Введите f1: '))
f2=float(input('Введите f2: '))
l1=float(input('Введите l1: '))
l2=float(input('Введите l2: '))

k=0

if form_circil(p1,p2,a,b,R):
    k+=1
    print('Точка P лежит внутри окружности')
else:
    print('Точка P не лежит внутри окружности')
    
if form_circil(f1,f2,a,b,R):
    k+=1
    print('Точка F лежит внутри окружности')
else:
    print('Точка F не лежит внутри окружности')
    
if form_circil(l1,l2,a,b,R):
    k+=1
    print('Точка L лежит внутри окружности')
else:
    print('Точка L не лежит внутри окружности')

print(k)
