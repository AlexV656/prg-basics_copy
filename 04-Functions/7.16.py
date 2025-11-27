def fib(n):
    if n<=1:
        return n
    n1= 0
    n2=1
    for x in range(n-2):
        n2,n1=n2+n1,n2
    return n2
if __name__=="__main__":
    print(fib(5))
    print(fib(9))
    print(fib(3))