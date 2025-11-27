def neg_in_rng(x,y):
    neg_even_count = 0
    for number in list(range(x,y+1)):
        if number<0 and number%2==0:
            neg_even_count+=1
    return neg_even_count
if __name__=="__main__":
    print(neg_in_rng(-7,8))
    print(neg_in_rng(-1,11))