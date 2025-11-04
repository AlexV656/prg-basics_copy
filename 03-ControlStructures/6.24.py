for x in range(10):
    if x<6:
        print('* '*x)
        number_to_sub= x
    else:
        print('* '*(x-(2*(x-number_to_sub))))
    print('')