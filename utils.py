import os

from constants import CATEGORIES, PRINTED_CARDS, SHAPES, TYPES


class Card:
    def __init__(self, card_type, shape):
        if card_type not in TYPES:
            raise ValueError("Card type must be one of {}".format(TYPES))
        if shape not in CATEGORIES:
            raise ValueError("Shape must be one of {}".format(CATEGORIES))
        self.card_type = card_type
        self.shape = shape
        self.a_value = 0
    def get_strings(self):
        printed = PRINTED_CARDS[TYPES.index(self.card_type)]
        return [
            st\
                .replace("S", SHAPES[CATEGORIES.index(self.shape)]) for st in printed
            ]

    def __str__(self):
        return "\n".join(self.get_strings())

    def get_value(self):
        if self.card_type in ['J', 'Q', 'K']:
            return 10
        elif self.card_type == 'A':
            return self.a_value
        else:
            return int(self.card_type)

def repr_cards(cards):
    result = ""
    for row in range(len(cards[0].__str__())):
        line = ''
        if row > 8:
            break
        for col in range(len(cards)):
            line += cards[col].get_strings()[row] + ' '
        result += line + "\n"
    return result

def create_deck():
    return [Card(type, category) for category in CATEGORIES for type in TYPES]

def show_player_info(player_cards: list[Card], dealer_cards:list[Card] | None = None):
    os.system("clear")
    player_score = sum(card.get_value() for card in player_cards)
    pl_bl = ' (Blackjack!)' if player_score == 21 else ''
    if not dealer_cards:
        print(f"Score | Player: {player_score}{pl_bl}")
        print("Your cards:")
        print(repr_cards(player_cards))
    else:
        dealer_score = sum(card.get_value() for card in dealer_cards)
        dl_bl = ' (Blackjack!)' if dealer_score == 21 else ''
        print(f"Score | Player: {player_score}{pl_bl} | Dealer: {dealer_score}{dl_bl}")
        print("Your cards:")
        print(repr_cards(player_cards))
        print("Dealer's cards:")
        print(repr_cards(dealer_cards))
    