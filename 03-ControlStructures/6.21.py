amount = int(input('enter amount in PLN: '))

coins = {5:0,2:0,1:0}
current_coin_indx = 0
while amount>0:
    if amount<list(coins.keys())[current_coin_indx]:
        current_coin_indx+=1
    else:
        amount-=list(coins.keys())[current_coin_indx]
        coins[list(coins.keys())[current_coin_indx]]+=1

print(coins)
for coin in coins:
    print(f'{coin} PLN coins: {coins[coin]}')