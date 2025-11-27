def hide(card_number):
    return card_number[:2]+len(card_number[2:len(card_number)-1-4])*'*'+card_number[len(card_number)-4:len(card_number)]

if __name__ == '__main__':
    print(hide('5290312400019022'))