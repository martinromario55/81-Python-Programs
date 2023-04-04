# BLACKJACK ♥♦♣♠
Blackjack, also known as 21, is a card game where players try to get as close to 21 points as possible without going over. This program uses images drawn with text characters, called ASCII art. American Standard Code for Information Interchange (ASCII) is a mapping of text characters to numeric codes that computers used before Unicode replaced it.
You can find other rules and the history of this card game at https://en.wikipedia.org/wiki/Blackjack.

### How It Works
The card suit symbols don’t exist on your keyboard, which is why we call the chr() function to create them. The integer passed to chr() is called a Unicode code point, a unique number that identifies a character according to the Unicode standard.
 Unicode is often misunderstood. However, Ned Batchelder’s 2012 PyCon US talk “Pragmatic Unicode, or How Do I Stop the Pain?” is an excellent introduction to Unicode, and you can find it at https://youtu.be/sgHbC6udIqc/. 
 Appendix B gives a full list of Unicode characters you can use in your Python programs.
 
### Exploring the Program
Try to find the answers to the following questions. Experiment with some modifications to the code and rerun the program to see what effect the changes have.

1. How can you make the player start with a different amount of money?
2. How does the program prevent the player from betting more money than they have?
3. How does the program represent a single card?
4. How does the program represent a hand of cards?
5. What do each of the strings in the rows list (created on line 190) represent?
6. What happens if you delete or comment out random.shuffle(deck) on line 143?
7. What happens if you change money -= bet on line 105 to money += bet?
8. What happens when showDealerHand in the displayHands() function is set to True? What happens when it is False?