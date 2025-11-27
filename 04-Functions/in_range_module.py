def in_range(x,y,n):
    print(f'A number: {n}')
    if n in list(range(x,y+1)):print(f'Number {n} is in the range <{x},{y}>: yes')
    else:print(f'Number {n} is in the range <{x},{y}>: no')

    return n in list(range(x,y+1))