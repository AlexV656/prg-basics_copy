import random
dice_rolled = random.randint(1,6)
print(dice_rolled)
print(f'Special number (1 or 6): {dice_rolled==1 or dice_rolled == 6}')