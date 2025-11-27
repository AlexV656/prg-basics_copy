def asterisks(n):
    starting_string = '*'
    if n==1:return starting_string
    for x in range(n-1):
        starting_string+='/*'
    return starting_string
print(asterisks(4))
print(asterisks(1))