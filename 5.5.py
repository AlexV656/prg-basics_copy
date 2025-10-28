price = float(input('Enter price: '))
discount = float(input('Enter discount %: '))
print(f'Price with discount: {price-price/100*discount:.2f} ')
print(f"Reduction: {price-(price-price/100*discount):.2f}")