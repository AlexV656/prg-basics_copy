decimal = int(input('Enter number'))
reminder = 0
binary = ''
while decimal>0:
    binary +=str(decimal%2)
    decimal//=2
print(binary)