import sys

# Define your bitmap image here:
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""

# Function to display the bitmap message:
def display_bitmap_message(message):
    if message == '':
        sys.exit("Message cannot be empty!")

    # Loop over each line in the bitmap:
    for line in bitmap.splitlines():
        # Loop over each character in the line:
        for i, bit in enumerate(line):
            if bit == ' ':
                # Print an empty space since there's a space in the bitmap:
                print(' ', end='')
            else:
                # Print a character from the message:
                print(message[i % len(message)], end='')
        print()  # Print a newline.

# Provide instructions to the user:
print('Bitmap Message Display')
print('This program uses a bitmap to display a message.')
print('Enter the message to display with the bitmap.')
print('Press Enter to exit.')

# Get user input for the message:
user_message = input('> ')

# Display the bitmap message:
display_bitmap_message(user_message)
