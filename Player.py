from Deck import Deck 
from Card import Card
from CardSuit import CardSuit
from CardRank import CardRank

class Player:
  
  def __init__(self, deck) -> None:
    if (len(deck) != 26):
      raise RuntimeError(f'Length of Deck has to equal to 26, current length is {len(deck)}')
    self.deck = list(deck)

  def pop(self):
    return self.deck.pop()

  def win(self, cards):
    self.deck.extend(cards)

if __name__=='__main__':
  deck = Deck()
  deck.shuffle()
  providedDeck = deck.provide_deck()
  player = Player(providedDeck[0])
  firstCard = player.pop()
  print(firstCard)
  secondCard = player.pop()
  print(secondCard)
  appendList = [firstCard, secondCard]
  player.win(appendList)
  print(player.deck[-2])
  print(player.deck[-1])
  try:
    wrongDeck = [Card(CardSuit.Clover, CardRank.Two)]
    wrongPlayer = Player(wrongDeck)
  except RuntimeError as err:
    print(f'error: {err}')
