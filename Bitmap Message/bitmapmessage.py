import sys
# You can also copy and paste the image from https://inventwithpython.com/bitmapworld.txt
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
...................................................................."""

print('Bitmap Message')
print('Enter the message to display with the bitmap.')
message = input('> ')

if message == '':
    sys.exit()

# Loop over each line in the bitmap
for line in bitmap.splitlines():
    # loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space
            print(' ', end=(''))
        else:
            # Print a character from the message
            print(message[i % len(message)], end=(''))

    print() # Print a new line