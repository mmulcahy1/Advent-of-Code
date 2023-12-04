import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

#dict of cards and cards won by each card
cards = {}


def playCard(cardNum):
    #if card already played, get the number of total cards won from the current card
    if cardNum in cards:
        cardsWon = cards[cardNum]
    #if card not in dict, find the number of cards won by this card
    else:
        cardsWon = 0
        winningNums = re.findall(r'\d+', lines[cardNum-1].split('|')[0].split(':')[1])
        
        for numYouHave in re.finditer(r'\d+', lines[cardNum-1].split('|')[1]):
            if numYouHave[0] in winningNums:
                cardsWon = cardsWon + 1
        
        #play each card that was just won by the current card
        for i in range(cardsWon):
            cardsWon = cardsWon + playCard(cardNum+i+1)
        
        cards[cardNum] = cardsWon   #update the dict with the number of cards won
    return cardsWon
    
#count the original cards
totalCards = len(lines)
#play each original card
for n in range(len(lines)):
    totalCards = totalCards + playCard(n+1)

print(totalCards)