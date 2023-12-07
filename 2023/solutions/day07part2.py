import sys
import re

lines = [line.replace('\n','') for line in open(sys.argv[1],'r').readlines()]

cardOrder = 'J23456789TQKA'

fiveOfAKind = []
fourOfAKind = []
fullHouse = []
threeOfAKind = []
twoPair = []
onePair = []
highCard = []

for line in lines:
    cardCounts = {}
    hand = line.split(' ')[0]
    bid = line.split(' ')[1]
    #count the number of times each card value appears in the hand
    for card in hand:
        if card in cardCounts:
            cardCounts[card] += 1
        else:
            cardCounts[card] = 1
            
    #if the hand has jokers and doesn't only have jokers
    #add the number of jokers to the number of the most frequent non-joker card
    if 'J' in cardCounts and len(cardCounts) > 1:
        jokerCount = cardCounts['J']
        del cardCounts['J']
        mostFreqCard = max(cardCounts, key=cardCounts.get)
        cardCounts[mostFreqCard] += jokerCount
            
    if 5 in cardCounts.values():
        fiveOfAKind.append([hand, bid])
    elif 4 in cardCounts.values():
        fourOfAKind.append([hand, bid])
    elif 3 in cardCounts.values() and 2 in cardCounts.values():
        fullHouse.append([hand, bid])
    elif 3 in cardCounts.values():
        threeOfAKind.append([hand, bid])
    elif 2 == sum(s == 2 for s in cardCounts.values()):
        twoPair.append([hand, bid])
    elif 1 == sum(s == 2 for s in cardCounts.values()):
        onePair.append([hand, bid])
    else:
        highCard.append([hand, bid])


winnings = 0

fiveOfAKind = sorted(fiveOfAKind, key=lambda c:[cardOrder.index(i) for i in c[0]])
fourOfAKind = sorted(fourOfAKind, key=lambda c:[cardOrder.index(i) for i in c[0]])
threeOfAKind = sorted(threeOfAKind, key=lambda c:[cardOrder.index(i) for i in c[0]])
fullHouse = sorted(fullHouse, key=lambda c:[cardOrder.index(i) for i in c[0]])
twoPair = sorted(twoPair, key=lambda c:[cardOrder.index(i) for i in c[0]])
onePair = sorted(onePair, key=lambda c:[cardOrder.index(i) for i in c[0]])
highCard = sorted(highCard, key=lambda c:[cardOrder.index(i) for i in c[0]])

rank = 1
for x in highCard:
    winnings += int(x[1]) * rank
    rank += 1

for x in onePair:
    winnings += int(x[1]) * rank
    rank += 1
    
for x in twoPair:  
    winnings += int(x[1]) * rank
    rank += 1
    
for x in threeOfAKind:
    winnings += int(x[1]) * rank
    rank += 1
    
for x in fullHouse:
    winnings += int(x[1]) * rank
    rank += 1
    
for x in fourOfAKind:
    winnings += int(x[1]) * rank
    rank += 1
    
for x in fiveOfAKind:
    winnings += int(x[1]) * rank
    rank += 1
    
print(winnings)