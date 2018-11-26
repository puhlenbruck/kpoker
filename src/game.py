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
                    "\nAll bet sizes must be equal to or larger than the big blind. Please put in a proper bet!"
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
        fold_flag: bool = False
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

            # checks to see if the player input an allowable action after someone has made a bet
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
            elif self.act.lower() == "fold":
                fold_flag = True

            elif self.act.lower() == "call":
                pass
            elif self.act.lower() == "raise":
                pass

        return fold_flag


def deal_hand(deck):
    return [deck.deal(), deck.deal()]


def deal_board(deck):
    board = []
    deck.deal()  # burning a card

    # dealing the flop
    for i in range(3):
        board.append(deck.deal())

    print("Board after flop: {}".format(board))

    # dealing the turn
    deck.deal()  # burning a card
    board.append(deck.deal())

    print("Board after turn: {}".format(board))

    # dealing the river
    deck.deal()  # burning a card
    board.append(deck.deal())

    print("Board after river: {}".format(board))
    return board


def flush_finder(in_cards):
    flush_flag = False
    suits = [in_cards[0].suite.value, in_cards[1].suite.value]
    if suits[0] == suits[1]:
        suit_count = [2, 0]
    else:
        suit_count = [1, 1]
    for index in range(2, len(in_cards)):
        if in_cards[index].suite.value == suits[0]:
            suit_count[0] += 1
        elif in_cards[index].suite.value == suits[1]:
            suit_count[1] += 1
    if suit_count[0] == 5 or suit_count[1] == 5:
        flush_flag = True
    return flush_flag, suits


def straight_finder(in_cards):
    # converts the cards in the numerical value for simple sorting within a list
    tot_vals = []
    for cd in in_cards:
        if cd.value.value == "Ace":
            tot_vals.append(1)
        elif cd.value.value == "King":
            tot_vals.append(13)
        elif cd.value.value == "Queen":
            tot_vals.append(12)
        elif cd.value.value == "Jack":
            tot_vals.append(11)
        else:
            tot_vals.append(cd.value.value)

    strt_flag = False
    # create a set of the different values to make checking for a straight easier
    strt_vals = tot_vals.copy()
    strt_vals.sort()
    strt_vals = set(tot_vals)
    strt_vals = list(strt_vals)
    strt_len = len(strt_vals)
    if strt_len >= 5:
        for ind in range(2, len(strt_vals) - 2):
            if (
                strt_vals[ind + 2] == strt_vals[ind] + 2
                and strt_vals[ind - 2] == strt_vals[ind] - 2
                and strt_vals[ind + 1] == strt_vals[ind] + 1
                and strt_vals[ind - 1] == strt_vals[ind] - 1
            ):
                strt_flag = True

    return strt_flag, tot_vals, strt_vals


def match_finder(in_values_sort, in_values):
    pair_flag = False
    twopair_flag = False
    set_flag = False
    fok_flag = False
    fullhouse_flag = False
    value_count = []
    for cd in in_values_sort:
        value_count.append(in_values.count(cd))

    if value_count.count(2) == 1:
        pair_flag = True
    elif value_count.count(2) >= 2:
        twopair_flag = True
    elif value_count.count(3) == 1:
        if value_count.count(2) >= 1:
            fullhouse_flag = True
        else:
            set_flag = True
    elif value_count.count(4) == 1:
        fok_flag = True

    return pair_flag, twopair_flag, set_flag, fullhouse_flag, fok_flag


# this function takes in the cards on the board and the remaining players' hands and evaluates the winning hand
def read_hand(rem_hands, board):
    total_cards = rem_hands + board
    card_1 = rem_hands[0]
    card_2 = rem_hands[1]
    # dictionary to flag down if there is a viable hand
    win_hands = {
        "Four of a Kind": False,
        "Full House": False,
        "Flush": False,
        "Straight": False,
        "Set": False,
        "Two Pair": False,
        "Pair": False,
    }

    # after the flop check for best hands
    # check for flush
    win_hands["Flush"], suits = flush_finder(total_cards)

    # check for straight
    win_hands["Straight"], tot_vals, tot_vals_sort = straight_finder(total_cards)

    # check if the hand has any matching cards
    win_hands["Pair"], win_hands["Two Pair"], win_hands["Set"], win_hands[
        "Full House"
    ], win_hands["Four of a Kind"] = match_finder(tot_vals_sort, tot_vals)

    return tot_vals, win_hands


class PokerGame:
    def __init__(self, num_players):
        sma_bl = 5
        big_bl = 10
        # create our deck and our cards
        self._num_players = num_players
        self._deck = Deck()

    def play_round(self):
        # show each person their starting hands
        hand_of_players = {}
        for p in range(1, self._num_players + 1):
            hand_of_players["Player {}".format(p)] = Hand(deal_hand(self._deck))

        board = deal_board(self._deck)
        print(hand_of_players["Player 1"]._cards + board)
        play_hands_vals, wins = read_hand(hand_of_players["Player 1"]._cards, board)
        for k, w in wins.items():
            if w == True:
                print("You have a {}!".format(k))
        print(wins)
        print(play_hands_vals)
        return [hand_of_players["Player 1"]._cards, board]
