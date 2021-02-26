def fib(nthNum):
    j =0 
    k=1 
    fib = 0

    for i in range(nthNum-1):
        fib = j+k
        j = k
        k = fib

    return fib
            