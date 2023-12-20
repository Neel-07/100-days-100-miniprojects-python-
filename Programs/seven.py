def getSevSegStr(number, minWidth=0):
    """Return a seven-segment display string of number. The returned
    string will be padded with zeros if it is smaller than minWidth."""

    # Convert number to string in case it's an int or float:
    number = str(number).zfill(minWidth)

    rows = ['']*3
    for numeral in number:
        if numeral == '.':  # Render the decimal point.
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue  # Skip the space in between digits.
        elif numeral == '-':  # Render the negative sign:
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':  # Render the 0.
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':  # Render the 1.
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':  # Render the 2.
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        # ... (continued for numerals 3 to 9)
        
        # Add a space (for the space in between numerals) if this
        # isn't the last numeral and the decimal point isn't next:
        if numeral != '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    return '\n'.join(rows)


# Example usage
myNumber = getSevSegStr(2, 2)
print(myNumber)
