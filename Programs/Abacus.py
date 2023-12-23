NUMBER_OF_DIGITS = 10

def main():
    print('Soroban - The Japanese Abacus')
    
    print()

    abacusNumber = 0  # This is the number represented on the abacus.

    while True:  # Main program loop.
        displayAbacus(abacusNumber)
        displayControls()

        commands = input('> ')
        if commands == 'quit':
            # Quit the program:
            break
        elif commands.isdecimal():
            # Set the abacus number:
            abacusNumber = int(commands)
        else:
            # Handle increment/decrement commands:
            for letter in commands:
                if letter == 'q':
                    abacusNumber += 1000000000
                elif letter == 'a':
                    abacusNumber -= 1000000000
                elif letter == 'w':
                    abacusNumber += 100000000
                # ... (and so on for other letters)

        # The abacus can't show negative numbers:
        if abacusNumber < 0:
            abacusNumber = 0  # Change any negative numbers to 0.qaa
        # The abacus can't show numbers larger than 9999999999:
        if abacusNumber > 9999999999:
            abacusNumber = 9999999999


def displayAbacus(number):
    numberList = list(str(number).zfill(NUMBER_OF_DIGITS))
    # (The rest of the code for the displayAbacus function)

def displayControls():
    print('  +q  w  e  r  t  y  u  i  o  p')
    print('  -a  s  d  f  g  h  j  k  l  ;')
    print('(Enter a number, "quit", or a stream of up/down letters.)')


if __name__ == '__main__':
    main()
