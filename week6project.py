import random

count = 2

number = random.randint(1,100)

while number != 'guess' or count < 10:
    guess = int(input('Guess a number between 1 and 100: '))

    if count > 10:
        print('You are out of attempts.')
        break
    
    elif guess < number:
        print('Guess higher')
        count += 1

    elif guess > number:
        print('Guess lower')
        count += 1

    else:
        print('You guessed it!')
        break  