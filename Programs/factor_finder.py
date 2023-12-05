import math, sys

while True:
    print('Enter a positive whole number to factor (or QUIT):')
    response = input('> ')
    if response.upper() == 'QUIT':
        sys.exit()

    if not (response.isdigit() and int(response) > 0):
        continue
    number = int(response)

    factors = []

    # Find the factors of the number:
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)

    # Convert to a set to eliminate duplicates:
    factors = list(set(factors))
    factors.sort()

    # Display the factors:
    factor_strings = [str(factor) for factor in factors]
    print(', '.join(factor_strings))
