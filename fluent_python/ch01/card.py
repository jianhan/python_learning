import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(len(deck))

beer_card = Card('7', 'diamonds')
print(beer_card)

print(choice(deck))

for card in deck:
    print(card, card.rank, "****")

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


# print(Card('Q', 'hearts') in deck, Card('7', 'beasts') in deck)
# print(deck.ranks)
for card in sorted(deck, key=spades_high):
    print(card)

# sort example

ns = [4, 5, 1, 2, 10, 22]


def number_sort(n):
    return n


for n in sorted(ns, key=number_sort):
    print(n)
