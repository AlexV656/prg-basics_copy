###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif 10>month>=7:
    quarter= 3
elif 7>month>=3:
    quarter =2
elif 3>month:
    quarter =1

    ...

print(f'Month {month} is in quarter {quarter}')