###
# Reads from file, line by line
#
file_cont = open('08-FileHandling/countries.txt', 'r').read().split('\n')
# file_write = open('08-FileHandling/countries.txt', 'w')
n= 1
for line in file_cont:
    # file_write.write(f'{n}. '+ line+'\n')
    print(line)
    n+=1