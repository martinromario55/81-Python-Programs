import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic game.
    
    I am thinking of a {}-digig number with no repeated digits.
    Try to guess what it is. Here are some clues.
    What I say:         That means:
    Pico                One digit is correct but in the wrong position.
    Fermi               One digit is correct and in the right position.
    Bagels              No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.
    '''.format(NUM_DIGITS))

    while True: # Main game loop
        # Store secret number
        secret_num = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until a valid guess is entered
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}:'.format(num_guesses))
                guess = input('> ')
            
            clues = getClues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num: # Correct answer
                break
            if num_guesses > MAX_GUESSES:
                print('You ran out of guesses. 💥')
                print('The answer was {}.'.format(secret_num))

        # Ask player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing! ❤')

def getSecretNum():
    '''Returns a string made up of NUM_DIGITS unique random digits.'''
    numbers = list('0123456789') # A list of digits 0 to 9.
    random.shuffle(numbers) # Shuffle into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def getClues(guess, secret_num):
    '''Returns a string with the pico, fermi, bagels clues for a guess and secret number pair.'''
    if guess == secret_num:
        return 'You got it! 🎉'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit in a correct place.
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # A correct digit in an incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # No correct digit.
    else:
        # Sort the clues into alphabetical order so their original order doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)


# Run program
if __name__ == '__main__':
    main()