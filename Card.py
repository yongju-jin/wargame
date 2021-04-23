from CardSuit import CardSuit
from CardRank import CardRank


class Card:

  def __init__(self, suit, rank) -> None:
    self.suit = suit
    self.rank = rank

  def __str__(self) -> str:
    return self.rank.name + " of " + self.suit.name

if __name__=='__main__':
	two_hearts=Card(CardSuit.Hearts, CardRank.Two)
	print(two_hearts)
	print(two_hearts.suit)
	print(two_hearts.rank)