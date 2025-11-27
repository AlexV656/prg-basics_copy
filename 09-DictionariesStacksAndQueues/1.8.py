price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
# import random
# lst = [[random.randint(1,10),random.randint(1,20),random.randint(2,19)] for x in range(3)]
# print(lst)
# for num1,num2,num3 in lst:
#     print(num1,num2)
print(f'before discount - {price_list}')
print(sum([price for price in price_list.values()]))
disc_price_lst = {key:float(f"{value-value/10:.2f}") for key,value in price_list.items()}
print(disc_price_lst)