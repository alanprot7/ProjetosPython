def fib(n):
    a,b = 0,1
    for i in range(1,n):
        a,b = b,a+b
    if(n == 0):
        return 0
    else:
        return b
