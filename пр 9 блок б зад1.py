def naib_max():
    n=int(input())
    if n==0:
        return 0
    next_max=naib_max()
    return n if n>next_max else next_max
result=naib_max()
print(result)
