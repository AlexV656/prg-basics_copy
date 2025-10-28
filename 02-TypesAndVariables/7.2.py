###
# A program that checks whether the password length
# read from the keyboard is correct.
#
passwords_lst = ['university','peter123','seven','anna333']
for x in range(len(passwords_lst)):
    password = passwords_lst[x]
    password_ok = len(password) >= 8

    print(f'Password length is valid: {password_ok}\nFor password: {password}')