def calc_dig_sum(number):
    return sum([int(x) for x in str(number)])
integer = int(input('Enter number'))
print(f'some of integer number is {calc_dig_sum(integer)}')