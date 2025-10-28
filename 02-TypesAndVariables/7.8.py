###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random
total = 0 
for x in range(3):
    dice_roll = random.randint(1,6)
    print(f'dice rolled = {dice_roll}')
    total+=dice_roll
print(total)