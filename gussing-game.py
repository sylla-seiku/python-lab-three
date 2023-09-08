# Learning how to create a guessing game.
secret_number = 9
guess_count = 0 
guess_limit = 3
you_won = False
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        #you_won = True
        print('You won!')
        break
    elif guess < secret_number:
        print('Too low.')
    elif guess > secret_number:
        print('Too high.')
        
else:
    print('Sorry, you failed!')