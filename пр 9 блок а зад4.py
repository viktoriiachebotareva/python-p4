def sum_digits(n):
    if n<0:
        n=abs(n)
    if n<10:
        return n
    last_digit=n%10
    new_digit=n//10
    summa=sum_digits(new_digit)
    return last_digit+summa
print(sum_digits(45))
print(sum_digits(685))       
print(sum_digits(-352))
print(sum_digits(0))