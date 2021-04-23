from typing import Tuple
from Card import Card
from CardSuit import CardSuit 
from CardRank import CardRank
import random

class Deck:
  def __init__(self) -> None:
      self.cards = []
      for suit in CardSuit:
        for rank in CardRank:
          self.cards.append(Card(suit, rank))

  def __str__(self) -> str:
    return '\n'.join(str(item) for item in self.cards)
  
  def shuffle(self):
    random.shuffle(self.cards)

  def provide_deck(self):
    return self.cards[1::2], self.cards[0::2]

if __name__=='__main__':
  deck = Deck()
  print(deck)
  print(len(deck.cards))
  deck.shuffle()
  print(deck)
  twoDeck = deck.provide_deck()
  print('first person first card')
  print(twoDeck[0][0])
  print('second person first card')
  print(twoDeck[1][0])
