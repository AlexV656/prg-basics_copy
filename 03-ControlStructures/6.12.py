discount = 0.25
number_of_products =int(input('Number of products purchased'))
price = int(input('Product price '))
if number_of_products>2:
    print(number_of_products*price-(number_of_products*price*discount))
else:
    print(number_of_products*price)