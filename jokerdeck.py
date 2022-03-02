from carddeck import CardDeck, Card

class JokerDeck(CardDeck):
    def _make_deck(self):
        super()._make_deck()
        for rank in '1', '2':
            card = Card(rank, '** JOKER **')
            self._cards.append(card)

    def scream(self):
        print("AAAAAAHHHHHHHHHHHHHHHHHH")

