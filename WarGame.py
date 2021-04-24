from Player import Player
from Deck import Deck

dec = Deck()
dec.shuffle()
(firstDeck, secondDeck) = dec.provide_deck()

firstPlayer = Player(firstDeck)
secondPlayer = Player(secondDeck)

isContinuePlay = True
pileCards = []
turn = 0
while isContinuePlay:
  firstPlayerCard = firstPlayer.pop()
  secondPlayerCard = secondPlayer.pop()
  print(f'[{turn}] firstPlayerCard: {firstPlayerCard}')
  print(f'[{turn}] secondPlayerCard: {secondPlayerCard}')

  pileCards.append(firstPlayerCard)
  pileCards.append(secondPlayerCard)
  if firstPlayerCard.rank.value == secondPlayerCard.rank.value:
    print('Draw')
    pileCards.extend(firstPlayer.draw())
    pileCards.extend(secondPlayer.draw())
  elif firstPlayerCard.rank.value < secondPlayerCard.rank.value:
    print(f'secondPlayer is win, has {len(pileCards)} cards')
    secondPlayer.win(pileCards)
    pileCards = []
  else:
    print(f'firstPlayer is win, has {len(pileCards)} cards')
    firstPlayer.win(pileCards)
    pileCards = []

  print(f'[{turn}] {firstPlayer} isLose: {firstPlayer.isLose()}')
  print(f'[{turn}] {secondPlayer} isLose: {secondPlayer.isLose()}')
  turn = turn + 1
  isContinuePlay = not (firstPlayer.isLose() or secondPlayer.isLose())
