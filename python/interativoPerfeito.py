def per(n):
    res = 0
    for i in range(2,(n+1)):
        if(n % i == 0):
            res += (n // i)
    return res

def no(n):
    cont = 2
    fim = 1
    while (fim <= n):
        if(cont == per(cont)):
            fim += 1
            print('{} - {}'.format((fim-1), cont))
            cont += 1
        else:
            cont += 1
