import re
from collections import defaultdict
from cardDict import CardDictionary
OrderRank =defaultdict(int)
UnOrderRank = defaultdict(int)
OrigHands = defaultdict(list)

cardDict = CardDictionary.CardDict()


def strongerHand(hand1, hand2):
    for i in range(len(hand1)):
        if cardDict[hand1[i]]> cardDict[hand2[i]]:
            return 1 # hand1 stronger
        elif cardDict[hand2[i]]> cardDict[hand1[i]]:
            return 2 #hand2 stronger
    
    return 0 #They the same

def HandSort(card):
    return cardDict[card]


def OnePair(hand:list, card):
    if hand.count(card) ==2:
        return True

def TwoPair(hand:list, card1, card2):
    if hand.count(card1) == hand.count(card2) == 2:
        return True
    
def ThreeKind(hand:list, card):
    if hand.count(card) ==3:
        return True

def FullHouse(hand:list, card1:str, card2:str):
    if (ThreeKind(hand, card1) and OnePair(hand, card2)) or (ThreeKind(hand, card2) and OnePair(hand, card1)):
        return True

def HandStrength(hand : list):
    onePair  = False
    Thrips = False

    if hand[0] == hand[-1]:
        return 7 #Five of a Kind
    elif hand[0] == hand[-2]:
        return 6#Four of a Kind
    
    for i in range(len(hand)):
        if not onePair:
            onePair = OnePair(hand,hand[i])
        if not Thrips:
            Thrips = ThreeKind(hand, hand[i])
        for j in range(i+1,len(hand)):
            if hand[i] != hand[j]:
                if FullHouse(hand, hand[i], hand[j]):
                    return 5
                if TwoPair(hand,hand[i], hand[j]):
                    return 3
        
    if Thrips:
        return 4
    if onePair:
        return 2       


    return 1
                        

with open('input.txt') as input:
    for line in input:
        line = line.strip()
        hand,bet = re.split(' ',line)
        hand.replace(" ",'')
        hand = list(hand)
        print(hand)
        origHand = hand
        hand.sort(reverse=True, key=HandSort)
        print(hand)
        bet.replace(" ","")
        OrigHands[(tuple)] = hand
        UnOrderRank[tuple(hand)] = HandStrength(hand)
        
print(UnOrderRank)

tempOrderedList = defaultdict(int)
FinalOrderedList = defaultdict(int)
for k,v in sorted(UnOrderRank.items(), key = lambda kv : kv[1]):
    OrderRank[k] = v

ans = 0


