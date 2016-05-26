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


def main():
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(deck[-1])

    # random pick can be used on this class
    print(choice(deck))
    print(choice(deck))

    # slice can be used
    print(deck[:3])
    print(deck[12::13])         # From 12, step 13

    # iterable
    for card in deck[:2]:
        print(card)

    # in operator is also ok
    print(Card('Q', 'hearts') in deck)
    print(Card('7', 'beasts') in deck)

if __name__ == '__main__':
    main()
