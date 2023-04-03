# BITMAP MESSAGE

This program uses a multiline string as a bitmap, a 2D image with only two possible colors for each pixel, to determine how it should display a message from the user. In this bitmap, space characters represent an empty space, and all other characters are replaced by characters in the user’s message. The provided bitmap resembles a world map, but you can change this to any image you’d like.

### How it works
Instead of individually typing each character of the world map pattern, you can copy and paste the whole thing from https://inventwithpython.com/bitmapworld.txt. 

A line of 68 periods at the top and bottom of the pattern acts as a ruler to help you align it correctly. However, the program will still work if you make typos in the pattern.
The bitmap.splitlines() method call returns a list of strings,
each of which is a line in the multiline bitmap string. 

Using a multiline string makes the bitmap easier to edit into whatever pattern you like. The program fills in any non-space character in the pattern, which is why asterisks, periods, or any other character do the same thing.

The message[i % len(message)] code on line 42 causes the repetition of the text in message. As i increases from 0 to a number larger than len(message), the expression i % len(message) evaluates to 0 again. This causes message[i %
len(message)] to repeat the characters in message as i increases.

### Exploring the Program
Try to find the answers to the following questions. Experiment with some modifications to the code and rerun the program to see what effect the changes have.
1. What happens if the player enters a blank string for the message?
2. Does it matter what the nonspace characters are in the bitmap variable’s
string?
3. What does the i variable created on line 45 represent?
4. What bug happens if you delete or comment out print() on line 52?