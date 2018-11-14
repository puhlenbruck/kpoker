#Poker Game!!!!!!!!!!
import numpy as np
import random as rnd
import math

class Deck():
    card_list = list(cards)

    def __init__(self, num_play):
        self.hands = {}
        self.tot_play = int(num_play) + 1  # add 1 for the dealer
        for i in range(1, self.tot_play + 1, 1):
            self.hands["hand_{}".format(i)] = []

    def generate(self):
        self.deck_of_cards = []
        for i in range(len(suits)):
            for j in range(len(self.card_list)):
                self.deck_of_cards.append(self.card_list[j] + ' of ' + suits[i])

    def shuffle(self):
        rnd.shuffle(self.deck_of_cards)

    def deal_hands(self):
        for i in range(2):
            self.handies = 1
            while self.handies < self.tot_play + 1:
                self.hands['hand_{}'.format(self.handies)].append(self.deck_of_cards.pop(0))
                self.handies += 1

    def burn(self):
        self.deck_of_cards.pop(0)

    def deal_board(self):
        self.board = []
        self.burn()

        # dealing the flop
        for i in range(3):
            self.board.append(self.deck_of_cards.pop(0))

        # dealing the turn
        self.burn()
        self.board.append(self.deck_of_cards.pop(0))

        # dealing the river
        self.burn()
        self.board.append(self.deck_of_cards.pop(0))


class Hand():
    def __init__(self, dealt_cards):
        self.card_1 = dealt_cards[0].split()
        self.card_2 = dealt_cards[1].split()

    def betting(self, balance, big_blind):
        self.balance = balance
        if self.balance == 0:
            print("\nSorry but you don't have any money to play.")
        else:
            print('\nYour current balance is {} dollars.'.format(self.balance))
            self.bet_size = input('\nPlace a bet for your hand. Bets must be multiples of the big blind. ')

            # checks to see if the bet is actually a number
            while self.bet_size.isnumeric() == False:
                self.bet_size = input('\nThat is not a legitimate bet. Please put in a proper number!')

            # checks to make sure the bet is larger than the big_blind
            while int(self.bet_size) < big_blind:
                self.bet_size = input('\nAll bet sizes must be multiples of 5. Please put in a proper bet!')

            # checks to see if the bet is larger than their stack
            self.bal_check = int(self.bet_size) <= self.balance
            while self.bal_check == False:
                self.bet_size = input("\nPlace a smaller bet for your hand! You don't have enough money!")
                self.bal_check = int(self.bet_size) <= self.balance
            self.balance = self.balance - self.bet_size

    # prompts the player to make a call, check, or raise
    def action(self, play_deck, pre_bet_amount):
        fold_flag = False
        if pre_bet_amount == 0:
            self.act = input('\nCheck, call, raise or fold? ')

            # checks to see if the player input an allowable action
            while self.act.isalpha() == False or (
                    self.act.lower() != 'check' and self.act.lower() != 'raise' and self.act.lower() != 'call' and self.act.lower() != 'fold'):
                self.act = input('\nThat is not an allowable action! Choose one of the aforementioned options! ')
        else:
            self.act = input('\nCall, raise or fold? ')

            # checks to see if the player input an allowable action
            while self.act.isalpha() == False or (
                    self.act.lower() != 'raise' and self.act.lower() != 'call' and self.act.lower() != 'fold'):
                self.act = input('\nThat is not an allowable action! Choose one of the aforementioned options! ')

            if self.act.lower() == 'check':

        if self.act.lower() == 'fold':
            fold_flag = True

        return fold_flag


play_n = 1
starting_deck = Deck(play_n)
# create our deck and our cards
starting_deck.generate()

# shuffle our deck
starting_deck.shuffle()

# deal out the hands to each player
starting_deck.deal()

# show each person their starting hands
hand_of_players = {}

# create a Hand object for each player and insert them in a dictionary so that we can see every player's hand
for p in range(1, total_num + 1):
    hand_of_players['Player {}'.format(p)] = Hand(starting_deck.hands['hand_{}'.format(p)])