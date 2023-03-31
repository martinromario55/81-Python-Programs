'''Birthday Paradox Simulation'''
import datetime, random


def getBirthdays(num_of_birthdays):
    '''Returns a list of number random date objects for birthdays.'''
    birthdays = []

    for i in range(num_of_birthdays):
        # The year is unimportant for the simulation
        start_of_year = datetime.date(2001, 1, 1)

        # Get a random day into the year
        random_num_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_num_of_days
        birthdays.append(birthday)
    
    return birthdays


def getMatch(birthdays):
    '''Returns the date object of a birthday that occurs more than once in the birthdays list'''

    # Check if all birthdays are unique and return None if so.
    if len(birthdays) == len(set(birthdays)):
        return None
    
    # Compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA # Return the matching birthday
            

# Display message
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
      The Birthday Paradox shows us that in a group of N people, the odds
      that two of them have matching birthdays is surprisingly large.
      This program does a Monte Carlo simulation (that is, repeated randomsimulations) to explore this concept.
      
      (It's not actually a paradox, it's just a surprising result.)
      ''')

# Set up a tuple of month names in order
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

# Get valid input
while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    # Check if input is a positive integer less than or equal to 100
    if response.isdecimal() and (0 < int(response) <= 100):
        num_days = int(response)
        break

print()

# Generate and display the birthdays
print('Here are', num_days, 'birthdays:')
birthdays = getBirthdays(num_days)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Put a comma after the first birthday.
        print(', ', end='')
        month_name = MONTHS[birthday.month -1]
        date_text = '{} {}'.format(month_name, birthday.day)
        print(date_text, end='')

print()
print()

# Determine if there are two birthdays that match.
match = getMatch(birthdays)

# Display the results
print('In this simulation, ', end='')
if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = '{} {}'.format(month_name, match.day)
    print('Multiple people have a birthday on', date_text)
else:
    print('There are no matching birthdays.')

print()

# Run through 100,000 simulations
print('Generating', num_days, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
sim_match = 0 # Number of simulations with matching birthdays

for i in range(100_000):
    # Report on the progress every 10,000 simulations
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    # Count the number of simulations
    birthdays = getBirthdays(num_days)
    if getMatch(birthdays) != None:
        sim_match = sim_match + 1
print('100,000 simulations run.')


# Display simulation results
probability = round(sim_match / 100_000 * 100, 2)
print('Out of 100,000 simulations of', num_days, 'people, there was a ')
print('matching birthday in that group', sim_match, 'times. This means')
print('that', num_days, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')