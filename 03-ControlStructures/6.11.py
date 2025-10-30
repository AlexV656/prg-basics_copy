price2= int(input('Current product price'))
price1 = int(input('Previous product price'))

product_price_reduction = (price1-price2)/(price1/100)
print(product_price_reduction)
if product_price_reduction>=10:
    print(f'Buy the product!!\nProduct price reduced by {product_price_reduction}%')
