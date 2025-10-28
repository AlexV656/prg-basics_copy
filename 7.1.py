###
# People up to and including 26 years of age are exempt
# from paying taxes in Poland. Write a program that,
# based on the person's age entered from the keyboard,
# prints True if the person is exempt from paying taxes
# and prints False otherwise.
#
for x in [38, 27, 26, 22, 18]:
    print(f'Exemption from paying taxes: {x<=26} at age {x}')