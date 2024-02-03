from cardDict import CardDictionary
cardDict = CardDictionary.CardDict()
import re 
from card import Card
from PokerRules import *
import functools
stackOfCards = list()
HighCardsList = list()
OnePairList = list()
TwoPairList = list()
ThreeKindList = list()
FullHouseList = list()
FourKindList = list()
FiveOfKindList = list()



def HandStrength(Card1 : Card):
    onePair  = False
    Thrips = False
    hand = Card1.SortedHand
    if hand[0] == hand[-1]:
        return 7 #Five of a Kind
    elif hand[0] == hand[3] or hand[1] == hand[4]:
        return 6#Four of a Kind
    
    for i in range(len(hand)):
        if not onePair:
            onePair = OnePair(Card1,hand[i])
        if not Thrips:
            Thrips = ThreeKind(Card1, hand[i])
        for j in range(i+1,len(hand)):
            if hand[i] != hand[j]:
                if FullHouse(Card1, hand[i], hand[j]):
                    return 5
                if TwoPair(Card1,hand[i], hand[j]):
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
        bet.replace(" ","")
        Card1 = Card(hand, bet)
        Card1.score = HandStrength(Card1)
        stackOfCards.append(Card1)

def compare_lists(Card1:Card, Card2:Card):
    list1= Card1.OrigHand
    list2=Card2.OrigHand
    for i in range(len(list1)):
        if cardDict[list1[i]]<cardDict[list2[i]]:
            return -1
        elif cardDict[list1[i]]> cardDict[list2[i]]:
            return 1
    return 0
stackOfCards.sort(key = lambda kv: (kv.score))
print(stackOfCards)
HighCardsList = [i for i in stackOfCards if i.score == 1]
OnePairList = [i for i in stackOfCards if i.score == 2]
TwoPairList = [i for i in stackOfCards if i.score == 3]
ThreeKindList = [i for i in stackOfCards if i.score == 4]
FullHouseList = [i for i in stackOfCards if i.score==5]
FourKindList = [i for i in stackOfCards if i.score == 6]
FiveOfKindList = [i for i in stackOfCards if i.score == 7]

HighCardsList.sort(key =functools.cmp_to_key(compare_lists))
OnePairList.sort(key=functools.cmp_to_key(compare_lists))
TwoPairList.sort(key =functools.cmp_to_key(compare_lists))
ThreeKindList.sort(key=functools.cmp_to_key(compare_lists))
FullHouseList.sort(key=functools.cmp_to_key(compare_lists))
FourKindList.sort(key =functools.cmp_to_key(compare_lists))
FiveOfKindList.sort(key=functools.cmp_to_key(compare_lists))
# print("\n HighCardList: ")
# print(HighCardsList)
# print("\n OnePairList: ")
# print(OnePairList)
# print("\n TwoPairList: ")
# print(TwoPairList)
# print("\n ThreeKindList: ")
# print(ThreeKindList)
# print("\n FullHouseList: ")
# print(FullHouseList)
# print("\n FourKindList: ")
# print(FourKindList)
# print("\n FiveOfKindList: ")
# print(FiveOfKindList)
ans =0
rank = 1
for i in HighCardsList:
    ans +=(i.bet * rank)
    rank+=1
for i in OnePairList:
    ans +=(i.bet * rank)
    rank+=1
for i in TwoPairList:
    ans +=(i.bet * rank)
    rank+=1
for i in ThreeKindList:
    ans +=(i.bet * rank)
    rank+=1
for i in FullHouseList:
    ans +=(i.bet * rank)
    rank+=1
for i in FourKindList:
    ans +=(i.bet * rank)
    rank+=1
for i in FiveOfKindList:
    ans +=(i.bet * rank)
    rank+=1
print(rank)
print("ans: ", ans)
print()
# newStack = []
# for i in range(0, len(stackOfCards)):
#     if newStack.count(stackOfCards[i])==0:
#         newStack.append(stackOfCards[i])
#     for j in range(i+1, len(stackOfCards)):
#         if newStack.count(stackOfCards[j])>0:
#             continue
#         elif stackOfCards[i].score == stackOfCards[j].score:
#             breakLoop = False
#             temp = newStack.pop()
#             for k in range(len(stackOfCards[i].OrigHand)):
#                 if cardDict[stackOfCards[i].OrigHand[k]]==cardDict[stackOfCards[j].OrigHand[k]]:
#                     continue
#                 elif cardDict[stackOfCards[i].OrigHand[k]]>cardDict[stackOfCards[j].OrigHand[k]]:
#                     newStack.append(stackOfCards[j])
#                     newStack.append(temp)
#                     breakLoop= True
#                 elif cardDict[stackOfCards[i].OrigHand[k]]<cardDict[stackOfCards[j].OrigHand[k]]:
#                     newStack.append(temp)
#                     breakLoop = True
#                 if breakLoop:
#                     break
