# John Asare
# Tue May 26 19:32


""" This is going to be a game of guessing numbers"""
from random import randint


def guess_the_number(user_number):

    winning_anoucement = 'you, won $100!'
    lossing_anoucement= 'You lost, give me $50 :('

    my_card_number = randint(0, 10)

    if user_number == my_card_number:
        print(f'Congratulations! {winning_anoucement}')
    else:
        print(f'{lossing_anoucement}. The correct number is {my_card_number}')


print('If you guess the correct number on my card, you will win $100. If you guessed wrong,'
          'I will take $50 from you.')
guess_the_number(int(input('\n What is the number on my card?: ')))