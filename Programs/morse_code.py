# Dictionary for Morse code mappings
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def text_to_morse(text):
    # Convert text to Morse code
    morse_code = ''
    for char in text.upper():
        if char == ' ':
            morse_code += ' '
        elif char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
    
    return morse_code

def morse_to_text(morse_code):
    # Convert Morse code to text
    words = morse_code.split('  ')
    text = ''
    for word in words:
        chars = word.split(' ')
        for char in chars:
            if char in morse_code_dict.values():
                text += [key for key, value in morse_code_dict.items() if value == char][0]
        text += ' '
    
    return text

# Main menu
while True:
    print("Main Menu:")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("3. Quit")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        text = input("Enter the text to convert to Morse code: ")
        morse_code = text_to_morse(text)
        print(f"Morse Code: {morse_code}")
    elif choice == '2':
        morse_code = input("Enter the Morse code to convert to text: ")
        text = morse_to_text(morse_code)
        print(f"Text: {text}")
    elif choice == '3':
        print("Thanks for using the Morse Code Translator. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
