def fib(n):
    lst = [0,1]
    for x in range(n):lst.append(lst[-2]+lst[-1])
    return lst
print(fib(20))