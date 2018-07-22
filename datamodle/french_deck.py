from collections import namedtuple
from random import choice

Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    # iter()
    def __getitem__(self, position):
        return self._cards[position]


def spaeds_high(card):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


def get_len(deck):
    print(len(deck))


def get_choice(deck):
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))


def get_slice(deck):
    print(deck[:3])
    print(deck[12::13])


def iter_item(deck):
    for card in deck:
        print(card)


def sorted_in_order(deck):
    for card in sorted(deck, key=spaeds_high):
        print(card)


if __name__ == '__main__':
    deck = FrenchDeck()
    get_len(deck)
    get_choice(deck)
    get_slice(deck)
    iter_item(deck)
    sorted_in_order(deck)
