def alg(a,b):
    while b!=0:
        a,b=b,a%b
    return a
A=int(input('Введите A:'))
B=int(input('Введите B:'))
C=int(input('Введите C:'))
D=int(input('Введите D:'))

numer=A*D
denom=B*C

NOD=alg(numer,denom)
numer//=NOD
denom//=NOD

print(numer//denom)
