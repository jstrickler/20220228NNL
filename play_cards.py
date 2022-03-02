from carddeck import CardDeck, InvalidDealerNameError
from jokerdeck import JokerDeck

d1 = CardDeck("Alice") # instantiate
d2 = CardDeck("Mary")

print(d1)

print(d1._name)  # NAUGHTY!!!

# d1.show_name()  # CardDeck.show_name(d1)
# d2.show_name(use_upper=True)  # CardDeck.show_name(d2, use..)

print(d1.dealer_name, d2.dealer_name)
print(d1.dealer_name_upper)


names = ['Fernando', 'Lucretia', 123.4, ['a', 'b', 'c']]
for name in names:
    try:
        d1.dealer_name = name
    except InvalidDealerNameError as err:
        print(err)
    else:
        print(d1.dealer_name)
        print(d1.dealer_name_upper)

d1.shuffle()
print(d1.cards, '\n')

print(len(d1))
for i in range(5):
    print(d1.draw())
print(len(d1))
print('-' * 60)

j1 = JokerDeck("Anastasia")
print(j1)
j1.shuffle()
print(j1.cards)

j1.scream()



