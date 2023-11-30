try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing.

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def caesar_cipher(message, mode, key):
    message = message.upper()
    translated = ''
    
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            if mode == 'encrypt':
                num = (num + key) % len(SYMBOLS)
            elif mode == 'decrypt':
                num = (num - key) % len(SYMBOLS)
            
            translated += SYMBOLS[num]
        else:
            translated += symbol
    
    return translated


def get_user_input():
    while True:
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        response = input('> ').lower()
        if response.startswith('e'):
            mode = 'encrypt'
            break
        elif response.startswith('d'):
            mode = 'decrypt'
            break
        print('Please enter "e" for encryption or "d" for decryption.')

    while True:
        max_key = len(SYMBOLS) - 1
        print(f'Please enter the key (0 to {max_key}) to use.')
        response = input('> ')
        if not response.isdecimal() or int(response) not in range(len(SYMBOLS)):
            continue
        key = int(response)
        break

    print(f'Enter the message to {mode}:')
    message = input('> ')
    return message, mode, key


def main():
    
    print('The Caesar cipher encrypts letters by shifting them over by a')
    print('key number. For example, a key of 2 means the letter A is')
    print('encrypted into C, the letter B encrypted into D, and so on.')
    print()

    message, mode, key = get_user_input()
    translated_text = caesar_cipher(message, mode, key)

    print(f'{mode.capitalize()}ed text: {translated_text}')

    try:
        pyperclip.copy(translated_text)
        print(f'Full {mode}ed text copied to clipboard.')
    except:
        pass


if __name__ == '__main__':
    main()

