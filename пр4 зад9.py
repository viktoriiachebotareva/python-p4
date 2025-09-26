n=int(input())
f1=1
f2=1
summa=f1+f2
for i in range(2,n):
    next_f=f1+f2
    summa+=next_f
    f1=f2
    f2=next_f
print(summa)
