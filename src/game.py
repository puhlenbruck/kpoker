# Poker Game!!!!!!!!!!
from deck import Deck
from numpy import zeros, ones
from math import floor

class Hand:
    def __init__(self, dealt_cards,p):
        self._cards = dealt_cards
        self._identity = p
        self.balance = 500

    def __repr__(self):
        return str(self._cards)

    def betting(self,big_blind,pre_bet_amount):

        if pre_bet_amount == 0:
            self.bet_size = input(
                    "\nPlace a bet for your hand. Bets must be equal to or greater than the big blind. "
            )

        # checks to see if the bet is actually a number
        while self.bet_size.isnumeric() == False:
            self.bet_size = input(
                "\nThat is not a legitimate bet. Please put in a proper number! "
            )

        # checks to make sure the bet is larger than the big_blind
        while int(self.bet_size) < big_blind:
            self.bet_size = input(
                "\nAll bet sizes must be equal to or larger than the big blind. Please put in a proper bet! "
            )

        # checks to see if the bet is larger than their stack
        self.bal_check = int(self.bet_size) <= self.balance
        while self.bal_check == False:
            self.bet_size = input(
                "\nPlace a smaller bet for your hand! You don't have enough money! "
            )
            self.bal_check = int(self.bet_size) <= self.balance

        self.balance = self.balance - self.bet_size

    def action(self, big_blind, pre_bet_amount):

        self.fold_flag = False

        if self.balance <= 0:
            print("\nSorry but you don't have any money to play.")
        else:
            print("\nYour current balance is {} dollars.".format(self.balance))

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
                if self.act.lower() == "check":
                    self.bet_size = 0
                    print("\nPlayer {} has checked his/her hand.".format(self._identity))

                elif self.act.lower() == "fold":
                    self.bet_size = 0
                    print("\nPlayer {} has folded his/her hand.".format(self._identity))
                    fold_flag = True

                elif self.act.lower() == "call":
                    self.bet_size = pre_bet_amount
                    print("\nPlayer {} has called.".format(self._identity))

                elif self.act.lower() == "raise":
                    self.betting(self.balance,big_blind)
                    print("\nPlayer {} has raised by .".format(self._identity))

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

                if self.act.lower() == "fold":
                    fold_flag = True

                elif self.act.lower() == "call":
                    self.bet_size = pre_bet_amount

                elif self.act.lower() == "raise":
                    self.betting(self.balance,big_blind)


class Dealer():
    def __init__(self, num_players,sm_blind,big_blind):
        self._num_players = num_players
        self._winners = list(zeros(num_players,dtype = int))
        self._poss_hand_vals = {
            "Straight Flush": 9,
            "Four of a Kind": 7,
            "Full House": 6,
            "Flush": 5,
            "Straight": 4,
            "Set": 3,
            "Two Pair": 2,
            "Pair": 1,
            "High": 0
        }
        self._pot = sm_blind + big_blind
        self._high_cards = []
        # reading the dealer's cards
        #self.d_card_1 = start_d_cards[0]
        #self.d_card_2 = start_d_cards[1]

    def calc_win(self, tot_vals_sort, final_hand, p):
        if final_hand[0]['Flush'] == True and final_hand[0]['Straight'] == True:
            self._high_cards.append(str(convertval_str(max(final_hand[1]))))
            self._winners[p - 1] = self._winners[p - 1] + self._poss_hand_vals['Flush'] + self._poss_hand_vals[
            'Straight']
        else:
            hand_vals = []
            hand_flag = False
            for k, w in final_hand[0].items():
                if w == True:
                    hand_flag = True
                    #implement only highest hand is announced
                    if k == 'Four of a Kind':
                        self._high_cards.append(str(convertval_str(max(final_hand[3]))))

                    elif k == "Full House":
                        self._high_cards.append(
                            [str(convertval_str(final_hand[3][1])), str(convertval_str(final_hand[3][2]))])

                    elif k == "Flush":
                        self._high_cards.append(str(convertval_str(max(final_hand[1]))))

                    elif k == "Straight":
                        self._high_cards.append(str(convertval_str(max(final_hand[2]))))

                    elif k == "Set":
                        self._high_cards.append(str(convertval_str(max(final_hand[3]))))

                    elif k == 'Two Pair':
                        self._high_cards.append(
                            [str(convertval_str(final_hand[3][1])), str(convertval_str(final_hand[3][2]))])

                    elif k == "Pair":
                        self._high_cards.append(str(convertval_str(max(final_hand[3]))))

                    hand_vals.append(self._poss_hand_vals[k])


            if hand_flag == False:
                hand_vals.append(0)
                self._high_cards.append(str(convertval_str(max(tot_vals_sort))))

            self._winners[p - 1] += max(hand_vals)


    def announce_win(self):
        self._win_val = max(self._winners)
        self._winner = self._winners.index(self._win_val)
        for v in self._winners:
            if v == self._win_val:
                for key, value in self._poss_hand_vals.items():
                    if value == self._win_val:
                        if key == "Straight Flush":
                            print("Player {} has won with a {} high straight flush!".format(self._winner + 1,self._high_cards[self._winner]))

                        elif key == "Four of a Kind":
                            print("Player {} has won with four {}'s!".format(self._winner + 1,self._high_cards[self._winner]))

                        elif key == "Two Pair":
                            print("Player {} has won with a pair of {}'s and a pair of {}'s".format(self._winner + 1,
                                                                                                self._high_cards[
                                                                                                    self._winner][0],
                                                                                                self._high_cards[
                                                                                                    self._winner][1]))
                        elif key == "Full House":
                            print("Player {} has won with {}'s full of {}'s".format(self._winner + 1,
                                                                                                self._high_cards[
                                                                                                    self._winner][0],
                                                                                                self._high_cards[
                                                                                                    self._winner][1]))
                        elif key == "Flush":
                            print("Player {} has won with a {} high flush!".format(self._winner + 1,self._high_cards[self._winner]))

                        elif key == "Straight":
                            print("Player {} has won with a {} high straight!".format(self._winner + 1,self._high_cards[self._winner]))

                        elif key == "Set":
                            print("Player {} has won with a set of {}'s!".format(self._winner + 1,self._high_cards[self._winner]))

                        elif key == "Pair":
                            print("Player {} has won with a pair of {}'s!".format(self._winner + 1,self._high_cards[self._winner]))

                        else:
                            print("Player {} has won with a {} high".format(self._winner + 1,self._high_cards[self._winner]))


def deal_hand(deck):
    return [deck.deal(), deck.deal()]


def deal_board(deck):
    board = []
    deck.deal()  # burning a card

    # dealing the flop
    for i in range(3):
        board.append(deck.deal())

    # dealing the turn
    deck.deal()  # burning a card
    board.append(deck.deal())

    # dealing the river
    deck.deal()  # burning a card
    board.append(deck.deal())

    return board


def ask_for_players(max_num):
    new_resp = input("Enter the number of players playing the game please! ")
    flag = new_resp.isnumeric()
    if flag == False:
        while flag == False:
            new_resp = input("\nThat is not a whole number! Put in an integer please! ")
            flag = new_resp.isnumeric()
    else:
        new_resp = floor(float(new_resp))
        while new_resp > max_num:
            new_resp = input(
                "\n{} is the maximum number of players allowed for Poker. Please put in another number".format(max_num))
            new_resp = floor(float(new_resp))
    return new_resp


def flush_finder(in_cards):
    flush_flag = False
    suits = [in_cards[0].suite.value, in_cards[1].suite.value]
    suited_cards = [[],[]]
    board_suit_count = 0
    suitc_vals = zeros(5,dtype = int)

    if suits[0] == suits[1]:
        suit_count = [2, 0]
    else:
        suit_count = [1, 1]

    for index in range(2, len(in_cards)):
        if in_cards[index].suite.value == suits[0]:
            suit_count[0] += 1
            suited_cards[0].append(in_cards[index])
        elif in_cards[index].suite.value == suits[1]:
            suit_count[1] += 1
            suited_cards[1].append(in_cards[index])

    if suit_count[0] == 5:
        flush_flag = True
        suitc_vals = convert_pack(suited_cards[0])
    elif suit_count[1] == 5:
        flush_flag = True
        suitc_vals = convert_pack(suited_cards[1])
    elif suit_count[0] == 1 and suit_count[1] == 1:
        for index in range(3, len(in_cards)):
            if in_cards[index].suite.value == in_cards[2].suite.value:
                board_suit_count += 1
        if board_suit_count == 5:
            flush_flag = True
            suitc_vals = convert_pack(in_cards[2:].value.value)

    return flush_flag, suits, suitc_vals


def convert_value(card_name):
    ace_flag = False
    if card_name.value.value == "Ace":
        ace_flag = True
        card_value = [1, 14]
    elif card_name.value.value == "King":
        card_value = 13
    elif card_name.value.value == "Queen":
        card_value = 12
    elif card_name.value.value == "Jack":
        card_value = 11
    else:
        card_value = card_name.value.value

    return card_value, ace_flag


def convert_pack(pack_names):
    sc_vals = []
    for cd in pack_names:
        cd_val, a_flag = convert_value(cd)
        if a_flag == False:
            sc_vals.append(cd_val)
        else:
            sc_vals.append(cd_val[0])
            sc_vals.append(cd_val[1])

    return sc_vals


def convertval_str(cd_value):
    if cd_value == 14 or cd_value == 1:
        card_name = "Ace"
    elif cd_value == 13:
        card_name = "King"
    elif cd_value == 12:
        card_name = "Queen"
    elif cd_value == 11:
        card_name = "Jack"
    else:
        card_name = cd_value
    pass

    return card_name

def convertpack_str(pack_vals):
    cd_names = []
    for cd in pack_vals:
        cd_name = convertval_str(cd)
        cd_names.append(cd_name)

    return cd_names


def straight_finder(in_cards):
    # converts the cards in the numerical value for simple sorting within a list
    tot_vals = []
    for cd in in_cards:
        card_value, a_flag = convert_value(cd)
        if a_flag == False:
            tot_vals.append(card_value)
        else:
            tot_vals.append(card_value[0])
            tot_vals.append(card_value[1])

    strt_flag = False
    # create a set of the different values to make checking for a straight easier
    strt_vals = tot_vals.copy()
    strt_vals.sort()
    strt_vals = set(tot_vals)
    strt_vals = list(strt_vals)
    print(strt_vals)
    strt_len = len(strt_vals)
    strt_cards = zeros(5,dtype=int)

    if strt_len >= 5:
        for ind in range(2, strt_len - 2):
            if (
                strt_vals[ind + 2] == strt_vals[ind] + 2
                and strt_vals[ind - 2] == strt_vals[ind] - 2
                and strt_vals[ind + 1] == strt_vals[ind] + 1
                and strt_vals[ind - 1] == strt_vals[ind] - 1
            ):
                strt_flag = True
                strt_cards = strt_vals[ind-2:ind+3]

    return strt_flag, tot_vals, strt_vals, strt_cards


def match_finder(in_values_sort, in_values):
    #still have to fix the error of two pair with just a pair of aces
    pair_flag = False
    twopair_flag = False
    set_flag = False
    fok_flag = False
    fullhouse_flag = False

    value_count = []
    in_val_cy = in_values.copy()
    match_vals = [0]

    for cd in in_values_sort:
        if cd == 1:
            in_val_cy.remove(cd)
        value_count.append(in_val_cy.count(cd))

    in_val_rev = in_values_sort.copy()
    in_val_rev.reverse()
    val_count_rev = value_count.copy()
    val_count_rev.reverse()
    if value_count.count(2) == 1 and value_count.count(3) != 1:
        pair_flag = True
        match_vals.append(in_values_sort[value_count.index(2)])
    elif value_count.count(2) >= 2:
        twopair_flag = True
        match_vals.append(in_val_rev[val_count_rev.index(2)])
        match_vals.append(in_values_sort[value_count.index(2)])
    elif value_count.count(3) == 1:
        match_vals.append(in_values_sort[value_count.index(3)])
        if value_count.count(2) >= 1:
            fullhouse_flag = True
            match_vals.append(in_val_rev[value_count.index(2)])
        else:
            set_flag = True
    elif value_count.count(4) == 1:
        fok_flag = True
        match_vals.append(in_values_sort[value_count.index(4)])
    print(value_count)
    print(in_values_sort)
    print(match_vals)
    return pair_flag, twopair_flag, set_flag, fullhouse_flag, fok_flag, match_vals


# this function takes in the cards on the board and the remaining players' hands and evaluates the winning hand
def read_hand(pl_hands, board):
    total_cards = pl_hands + board
    card_1 = pl_hands[0]
    card_2 = pl_hands[1]
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
    win_hands["Flush"], suits, flush_values = flush_finder(total_cards)

    # check for straight
    win_hands["Straight"], tot_vals, tot_vals_sort, strt_values = straight_finder(total_cards)

    # check if the hand has any matching cards
    win_hands["Pair"], win_hands["Two Pair"], win_hands["Set"], win_hands[
        "Full House"
    ], win_hands["Four of a Kind"], match_values = match_finder(tot_vals_sort, tot_vals)
    final_hand = [win_hands, flush_values, strt_values, match_values]

    return tot_vals_sort, final_hand


class PokerGame:
    def __init__(self, num_players):
        self._sma_bl = 5
        self._big_bl = 10
        # create our deck and our cards
        self._num_players = num_players
        self._deck = Deck()
        self._dealer = Dealer(self._num_players,self._sma_bl,self._big_bl)
        self._num_rounds = 1
        self.active_players = ones(num_players)
        self._deal_chip = list(zeros(num_players, dtype=int))
        self._deal_chip[0] = 1


    def play_round(self):
        # show each person their starting hands
        hand_of_players = {}
        for p in range(1, self._num_players + 1):
            hand_of_players["Player {}".format(p)] = Hand(deal_hand(self._deck),p)

        if self._num_rounds % self._num_players == 0:
            self._sma_bl *= 2
            self._big_bl *= 2

        #pre-flop action\

        board = deal_board(self._deck)

        #after flop

        #after turn

        #after river
        #break up the board dealing for each round to prompt for action and to allow each player to bet
        for p in range(1, self._num_players + 1):
            print(hand_of_players["Player {}".format(p)]._cards + board)
            tot_vals_sort, final_hand = read_hand(hand_of_players["Player {}".format(p)]._cards, board)
            self._dealer.calc_win(tot_vals_sort, final_hand, p)

        self._dealer.announce_win()
        #print(final_hand)
        self._num_rounds += 1
        #print(play_hands_vals)
        return [hand_of_players["Player 1"]._cards, board]
