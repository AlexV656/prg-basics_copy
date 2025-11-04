x = 9
every_n = 3
str_swap = ''
while x>=0:
    if x%3==0:
        print(str_swap[::-1])
        str_swap=str(x)+' '
    else:
        str_swap+=str(x)+' '
    x-=1
