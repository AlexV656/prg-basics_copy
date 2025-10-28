###
# A program that prints a numerical representation of each letter of your name.
#
name = input('enter your name - ') # replace John with your name
for x in range(len(name)):
    print(f'The letter {name[x]} has a code {ord(name[x])}')

...