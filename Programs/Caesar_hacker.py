

def caesar_cipher_hack(message):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for key in range(len(SYMBOLS)):
        translated = ''
        for symbol in message:
            if symbol in SYMBOLS:
                num = SYMBOLS.find(symbol)
                num = (num - key) % len(SYMBOLS)
                translated += SYMBOLS[num]
            else:
                translated += symbol
        print(f'Key #{key}: {translated}')

print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ').upper()
caesar_cipher_hack(message)
