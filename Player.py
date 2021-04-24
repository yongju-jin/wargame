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

  def draw(self):
    drawCards = []
    drawCardCount = min(3, len(self.deck))
    for item in range(drawCardCount):
      drawCards.append(self.pop())
    return drawCards

  def isLose(self):
    return len(self.deck) == 0

  def __str__(self) -> str:
    return f'Player has {len(self.deck)} cards'

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
  print(len(player.deck))
  print(player.draw())
  print(len(player.deck))
  try:
    wrongDeck = [Card(CardSuit.Clover, CardRank.Two)]
    wrongPlayer = Player(wrongDeck)
  except RuntimeError as err:
    print(f'error: {err}')
