n = 10#int(input('Prime number lst length'))
x=1
prime_lst =[]
prime = True
while len(prime_lst)<n:
    for g in range(1,x):
        if x%g == 0 and g!=1:
            prime = False
            break
    if prime:prime_lst.append(x)
    prime=True
    x+=1
print(prime_lst)