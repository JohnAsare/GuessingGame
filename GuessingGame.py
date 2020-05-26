# John Asare
# Tue May 26 19:32


""" This is going to be a game of guessing numbers"""
from random import randint


def guess_the_number(user_number):
    intro = 'If you guess the correct number on my card, you will win $100. If you guessed wrong,' \
            'I will take $50 from you.'
    winning_anoucement = 'You have won $100!'
    lossing_anoucement= 'You lost, give me $50 :('

    print(intro)
    my_card_number = randint(0, 10000000)

    if user_number == my_card_number:
        print(f'{winning_anoucement}')
    else:
        print(f'{lossing_anoucement}')


guess_the_number(int(input('\n What is the number on my card?: ')))