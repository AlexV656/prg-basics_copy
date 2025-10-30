###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if  x < 0 or y<0 :
    print(f'At least one of the numbers {y} and {x} is not negative')