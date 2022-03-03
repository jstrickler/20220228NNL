import random
# class object:
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         pass
class InvalidDealerNameError(Exception):
    pass

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    # used by str()
    def __str__(self):
        return f"{self.rank}-{self.suit}"

    # used by repr()
    def __repr__(self):  # code-friendly representation
        # Card(rank, suit)
        return f"Card('{self.rank}', '{self.suit}')"


# in C++/Java/C#  'self' is represented by 'this'
class CardDeck:   # inherits from 'object'
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, name):
        self.dealer_name = name
        self._make_deck()

    def _make_deck(self):
        self._cards = list()
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)


    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    # poor programming
    def show_name(self):
        pass

    @property  #  decorator
    def dealer_name(self):  # getter property
        return self._name

    @dealer_name.setter
    def dealer_name(self, name):  # setter property
        if isinstance(name, str):
            self._name = name
        else:
            raise InvalidDealerNameError("Dealer must be a string, not " + str(name))

    @property
    def dealer_name_upper(self):
        return self._name.upper()

    # @property
    # def spam(self):
    #     return self._spam
    #
    # @spam.setter
    # def spam(self, value):
    #     self._spam = value
    #
    # @property
    # def ham(self):
    #     return self._ham
    def __len__(self):
        return len(self._cards)