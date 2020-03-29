from random import randint

# Question 1 
# take an input from a user and print the integer
# user_input = input('Please type a string between 1 to 5:> ')
# user_input = user_input.lower()
# if user_input == 'one':
#     print(1)
# elif user_input == 'two':
#     print(2)
# elif user_input == 'three':
#     print(3)
# elif user_input == 'four':
#     print(4)
# elif user_input == 'five':
#     print(5)
# else:
#     print('Please type a number in the range')

# Question 2 
# Create a variable containing an integer between 1 and 5 inclusive. Ask the user to guess the number. If they guess too high or too 
# low then tell them. Tell them if they win. 
secret_num = randint(1,5)
guess = input('please guess a number between 1 and 5: ')
if guess.isdigit():
    guess = int(guess)
    if guess == secret_num:
        print('You won!')
    elif guess > secret_num and guess < 6:
        print('The num you guessed is too high.')
    elif guess < secret_num and guess > 0:
        print('The num you guessed is too low.')
    else:
        print('Number out of range.')
else:
    print('Please type a number in the range')


