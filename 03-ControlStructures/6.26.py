pin= '0805'
for x in range(3):
    entered_pin = input('Enter the PIN code: ')
    if entered_pin!=pin:
        print('Incorrct...')
    else:
        print('Payment completed')
        break

if pin!=entered_pin:
    print("Sorry, your payment card has been blocked")