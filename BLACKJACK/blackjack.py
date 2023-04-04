import random, sys

# Set up the constants
HEARTS = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES = chr(9824) # Character 9824 is '♠'.
CLUBS = chr(9827) # Character 9827 is '♣'.
BACKSIDE = 'backside'

def main():
    print('''Blackjack
    Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.''')

    money = 5000
    while True: # Main game loop
        # Check if the player has run out of money.
        if money <= 0:
            print("You're broke! 😂😂😂")
            print("Good thing you weren't playing real money.")
            print("Thanks for playing!")
            sys.exit()

        # Let the player enter their bet for this round
        print('Money:', money)
        bet = getBet(money)

        # Give the dealer and player two cards from the deck each:
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handle player action
        print('Bet:', bet)
        while True: # Keep looping until player stands or busts.
            displayHands(playerHand, dealerHand, False)
            print()

            # Check if the player has bust
            if getHandValue(playerHand) > 21:
                break

            # Get the player's move, either H, S, or D
            move = getMove(playerHand, money = bet)

            # Handle the plaer actions
            if move == 'D':
                # Player is doubling down, they can incease their bet
                additionalBet = getBet(min(bet, (money-bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)

            
            if move in ('H', 'D'):
                # Hit/doubling down take another card.
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {}of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # The player has busted.
                    continue

            if move in ('S', 'D'):
                # Stand/Doubling down stops the player's turn.
                break

        # Handle the dealer's actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # The dealer hits
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break # The dealer has busted
                input('Press Enter to continue...')
                print('\n\n')

        
        # Show the final hands
        displayHands(playerHand, dealerHand, True)

        player_value = getHandValue(playerHand)
        dealer_value = getHandValue(dealerHand)

        # Handle whether the player won or lost or tied.
        if dealer_value > 21:
            print('Dealer buts! 💥 You win ${}!'.format(bet))
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print('You lost! 😢')
            money -= bet
        elif player_value > dealer_value:
            print('You won ${}!'.format(bet))
            money += bet
        elif player_value == dealer_value:
            print('It\'s a tie, the bet is returned to you.')
            
        input('Press Enter to Continue...')
        print('\n\n')



def getBet(max_bet):
    # Ask the player how much they want to bet for this round.
    while True: # Keep asking until user enters a valid amount.
        print('How much do you want to bet? (1={}, or QUIT)'.format(max_bet))
        bet= input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing! 👋')
            sys.exit()

        if not bet.isdecimal():
            continue # If value not a number

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet # Valid bet
        

def getDeck():
    # Return a list of (rank, suit) tuples for all 52 cards.
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit)) # Add the numbered cars.
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))

    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    # Show the player's and dealer's cards. Hide the dealer's first card if showDealerHand is False.
    if showDealerHand:
        print('DEALER', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('DEALER: ????')
        # Hide the dealer's first card.
        displayCards([BACKSIDE] + dealerHand[1:])

    # Show the player's cards
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    # Returns the value of the cards.
    # Face cards are worth 10, aces are worth 11 or 1 (most suitable ace value).
    value = 0
    number_of_aces = 0

    # Add the value for the non-ace cards
    for card in cards:
        rank = card[0] # card is a tuple like (rank, suit)
        if rank == 'A':
            number_of_aces += 1
        elif rank in ('K', 'Q', 'J'): # Face cards are worth 10 points
            value += 10
        else:
            value += int(rank) # Numbered cards are worth their number.

    # Add the value for the aces
    value += number_of_aces # Adds only 1 per ace
    for i in range(number_of_aces):
        #if another 10 can be added without busting, do so
        if value + 10 <= 21:
            value +=10

    return value


def displayCards(cards):
    # Display all the cards in the card list
    rows = ['', '', '', '', ''] # The text to display on each row.
    
    for i, card in enumerate(cards):
        rows[0] += ' ___ ' # Print the top line of the card.
        if card == BACKSIDE:
            # print a card's back
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the card's front
            rank, suit = card # the card is a tuple
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # print each rowon the screen
    for row in rows:
        print(row)


def getMove(playerHand, money):
    # Asks the player for their move and returns 'H' for hit, 'S' for stand and 'D' for double down.
    while True: # Keep loopint until the player enters a correct move.
        # Determine what moves the player can make
        moves = ['(H)it', '(S)tand']

        # The player can double down on thier first move, which can we can tell because they'll have exactly two cards
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the player's move
        move_prompt = ', '.join(moves) + '> '
        move = input(move_prompt).upper()
        if move in ('H', 'S'):
            return move # Player has entered a valid move.
        if move == 'D' and '(D)ouble down' in moves:
            return move # Player has entered a valid move.
        
# Run program
if __name__ == '__main__':
    main()