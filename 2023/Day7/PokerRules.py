from card import Card
from cardDict import CardDictionary
cardDict = CardDictionary.CardDict()
class PokerRules():
    def __init__(self) -> None:
        pass




def strongerHand(Card1:Card, Card2:Card)->int:
    hand1 = Card1.OrigHand
    hand2 = Card2.OrigHand
    for i in range(len(hand1)):
        if cardDict[hand1[i]]> cardDict[hand2[i]]:
            return 1 # hand1 stronger
        elif cardDict[hand2[i]]> cardDict[hand1[i]]:
            return 2 #hand2 stronger
    
    return 0 #They the same
    

def OnePair(Card1:Card, card):
    hand = Card1.SortedHand
    if hand.count(card) ==2:
        return True
    return False
    

def TwoPair(Card1:Card, card1:str, card2:str):
    hand = Card1.SortedHand
    if hand.count(card1) == hand.count(card2) == 2:
        return True
    return False
    
def ThreeKind(Card1:Card, card):
    hand = Card1.SortedHand
    if hand.count(card) ==3:
        return True
    return False

def FullHouse(Cards:Card, card1:str, card2:str):
    if (ThreeKind(Cards, card1) and OnePair(Cards, card2)) or (ThreeKind(Cards, card2) and OnePair(Cards, card1)):
        return True
    return False



def OnePairP2(Card1:Card, card):
    hand = Card1.SortedHand
    if hand.count('J') == 1:
        return True
    if card == 'J':
        return False
    if hand.count(card) ==2 and hand.count('J')==0:
        return True
    return False

def TwoPairP2(Card1:Card, card1:str, card2:str):
    if card2 == 'J' and card1 == 'J':
        return False
    hand = Card1.SortedHand
    if hand.count('J') == 0 and hand.count(card1) == hand.count(card2)==2:
        return True
    return False

def ThreeKindp2(Card1:Card, card):
    hand = Card1.SortedHand
    if hand.count('J') == 2:
        otherList = [i for i in hand if i !='J']
        if otherList[0] !=otherList[1]:
            if otherList[1]!=otherList[2]:
                if otherList[2]!=otherList[0]:
                    return True
    if hand.count(card) ==3 and hand.count('J') == 0:
        return True
    elif OnePair(Card1, card) and hand.count('J') == 1:
        return True
    return False

def FullHousep2(Cards:Card, card1:str, card2:str):
    if Cards.OrigHand.count('J') >1:
        return False
    if Cards.OrigHand.count('J') == 1:
        if TwoPair(Cards, card1=card1, card2=card2):
            return True
    if (ThreeKind(Cards, card1) and OnePair(Cards, card2)) or (ThreeKind(Cards, card2) and OnePair(Cards, card1)):
        return True
    return False

def fourOfAKindP2(Card1:Card, card)->bool:
    hand = Card1.SortedHand
    if hand.count('J') == 0:
        if hand[0] == hand[3] or hand[1] == hand[4]:
            return True
    elif hand.count('J') == 1:
        if ThreeKind(Card1, card=card):
            return True
    elif hand.count('J') == 2:
        if card!='J':
            if OnePair(Card1, card):
                return True

    elif hand.count('J') == 3:
        othercard2= [i for i in hand if i !='J']
        if othercard2[0]!=othercard2[1]:
            return True
    return False

def FiveOfAKindP2(Card1:Card)->bool:
    hand = Card1.SortedHand
    if hand[0]==hand[-1]:
        return True
    if hand.count('J') == 1:
        if hand[0] == hand[3] or hand[1] == hand[4]:
            return True
    if hand.count('J') ==2:
        otherList = [i for i in hand if i !='J']
        if otherList[0] == otherList[1]==otherList[2]:
            return True
    if hand.count('J') ==3:
        otherList = [i for i in hand if i !='J']
        if otherList[0]==otherList[1]:
            return True
    if hand.count('J') == 4:
        return True
    return False



def HandStrengthP2(Card1 : Card):
    onePair  = False
    Thrips = False
    Two =False
    Full = False
    four= False
    hand = Card1.SortedHand
    if FiveOfAKindP2(Card1):
        return 7 #Five of a Kind
    
    for i in range(len(hand)):
        if not onePair:
            onePair = OnePairP2(Card1,hand[i])
        if not Thrips:
            Thrips = ThreeKindp2(Card1, hand[i])
        if not four:

            if fourOfAKindP2(Card1, hand[i]):
                four = True#Four of a Kind
        for j in range(i+1,len(hand)):
            if hand[i] != hand[j]:
                if not Full:
                    if FullHousep2(Card1, hand[i], hand[j]):
                        Full = True
                if not Two:
                    if TwoPairP2(Card1,hand[i], hand[j]):
                        Two = True
    if four:
        return 6  
    if Full:
        return 5
    if Thrips:
        return 4
    if Two:
        return 3
    if onePair:
        return 2       


    return 1
