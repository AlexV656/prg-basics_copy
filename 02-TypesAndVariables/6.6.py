###
# A program to print numerical representations of characters.
#
char_lst = list(input('char_lst').split(','))
print(char_lst)
for x in range(len(char_lst)):
    if len(char_lst[x])>1:
        print(ord(char_lst[x][1]))
    else:
        print(ord(char_lst[x]))
...
...