###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)') == 'y'
extra_spin = input('Extra spin? (y/n)') =='y'
time = 0
if program=='j':
    time = 40
    print('washing_product = "jacket"')
elif program == 'u':
    print('washing_product = "underwear"')
    time = 70
elif program =='s':
    print('washing_product = "shoes"')

    time = 20
print(f'rine = {extra_rinse}')
print(f'spin = {extra_spin}')
if extra_rinse:
    time+=15
if extra_spin:
    time+=9
print(f'Total washing time {time} minutes')