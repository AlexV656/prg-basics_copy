###
# Credit card payment 
#
account_balance = 500
total_payment_lst = [140, 499, 500, 501, 720]
for payment in total_payment_lst:
    if payment <= account_balance:
        print('Payment completed')
    else:
        print('No funds')