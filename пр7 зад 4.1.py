def alg(a,b):
    while b!=0:
        a,b=b,a%b
    return a
A=int(input('Введите A не равное нулю:'))
B=int(input('Введите B не равное нулю:'))
C=int(input('Введите C не равное нулю:'))
D=int(input('Введите D не равное нулю:'))

numer=A*D
denom=B*C

NOD=alg(numer,denom)
numer//=NOD
denom//=NOD

print(numer//denom)

