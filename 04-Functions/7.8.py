def amount_to_pay(n):
    coin_amount = 0
    while n>0:
        if n>=5:
            n-=5
            coin_amount+=1
        elif n>=2:
            n-=2
            coin_amount+=1
        else:
            n-=1
            coin_amount+=1
    return coin_amount
if __name__=="__main__":
    for x in [23,8,2,0]:
        print(amount_to_pay(x))