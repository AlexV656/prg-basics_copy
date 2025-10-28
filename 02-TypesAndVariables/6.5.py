###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
print(f'Phone number: {'-'.join([phone[x:x+3] for x in range(len(phone)) if x%3==0])}')