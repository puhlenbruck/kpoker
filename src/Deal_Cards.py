# Poker Game!!!!!!!!!!
from deck import Deck


class Hand:
    def __init__(self, dealt_cards):
        self._cards = dealt_cards

    def __repr__(self):
        return str(self._cards)

    def betting(self, balance, big_blind):
        self.balance = balance
        if self.balance == 0:
            print("\nSorry but you don't have any money to play.")
        else:
            print("\nYour current balance is {} dollars.".format(self.balance))
            self.bet_size = input(
                "\nPlace a bet for your hand. Bets must be multiples of the big blind. "
            )

            # checks to see if the bet is actually a number
            while self.bet_size.isnumeric() == False:
                self.bet_size = input(
                    "\nThat is not a legitimate bet. Please put in a proper number!"
                )

            # checks to make sure the bet is larger than the big_blind
            while int(self.bet_size) < big_blind:
                self.bet_size = input(
                    "\nAll bet sizes must be multiples of 5. Please put in a proper bet!"
                )

            # checks to see if the bet is larger than their stack
            self.bal_check = int(self.bet_size) <= self.balance
            while self.bal_check == False:
                self.bet_size = input(
                    "\nPlace a smaller bet for your hand! You don't have enough money!"
                )
                self.bal_check = int(self.bet_size) <= self.balance
            self.balance = self.balance - self.bet_size

    # prompts the player to make a call, check, or raise
    def action(self, play_deck, pre_bet_amount):
        fold_flag = False
        if pre_bet_amount == 0:
            self.act = input("\nCheck, call, raise or fold? ")

            # checks to see if the player input an allowable action
            while self.act.isalpha() == False or (
                self.act.lower() != "check"
                and self.act.lower() != "raise"
                and self.act.lower() != "call"
                and self.act.lower() != "fold"
            ):
                self.act = input(
                    "\nThat is not an allowable action! Choose one of the aforementioned options! "
                )
        else:
            self.act = input("\nCall, raise or fold? ")

            # checks to see if the player input an allowable action
            while self.act.isalpha() == False or (
                self.act.lower() != "raise"
                and self.act.lower() != "call"
                and self.act.lower() != "fold"
            ):
                self.act = input(
                    "\nThat is not an allowable action! Choose one of the aforementioned options! "
                )

            if self.act.lower() == "check":
                pass

        if self.act.lower() == "fold":
            fold_flag = True

        return fold_flag


def deal_hand(deck):
    return [deck.deal(), deck.deal()]


board = []


def deal_board(deck):
    global board
    board = []
    deck.deal()

    # dealing the flop
    for i in range(3):
        board.append(deck.deal())

    print("Board after flop: {}".format(board))

    # dealing the turn
    deck.deal()
    board.append(deck.deal())

    print("Board after turn: {}".format(board))

    # dealing the river
    deck.deal()
    board.append(deck.deal())

    print("Board after river: {}".format(board))


if __name__ == "__main__":
    play_n = 1

    # create our deck and our cards
    deck = Deck()

    # show each person their starting hands
    hand_of_players = {}

    # create a Hand object for each player and insert them in a dictionary so that we can see every player's hand
    for p in range(1, play_n + 1):
        hand_of_players["Player {}".format(p)] = Hand(deal_hand(deck))

    print(hand_of_players)

    deal_board(deck)
