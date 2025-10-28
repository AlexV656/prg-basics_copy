#diameter = int(input('Enter tree circumference in cm: '))
#print(f'Tree can be cut down: {diameter>=50}')
tree_string = 'Tree 1: 160 Tree 2: 90 Tree 3: 230 Tree 4: 120'
tree_lst = [int(tree_string[tree_string.index(str(x)+':')+2:tree_string.index(str(x)+':')+6]) for x in range(1,5)]
print(tree_lst)
for tree_d in tree_lst:
    
    print(f'Tree can be cut down: {tree_d>=50}') 
