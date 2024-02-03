from cardDict import CardDictionary
p2 = CardDictionary.p2Stack()
import re 
from card import Card
from PokerRules import *
import functools

def compare_lists(Card1:Card, Card2:Card):
    list1= Card1.OrigHand
    list2=Card2.OrigHand
    for i in range(len(list1)):
        if p2[list1[i]]<p2[list2[i]]:
            return -1
        elif p2[list1[i]]> p2[list2[i]]:
            return 1
    return 0

stackOfCards = list()
HighCardsList = list()
OnePairList = list()
TwoPairList = list()
ThreeKindList = list()
FullHouseList = list()
FourKindList = list()
FiveOfKindList = list()

with open('input.txt') as input:
     for line in input:
        line = line.strip()
        hand,bet = re.split(' ',line)
        hand.replace(" ",'')
        hand = list(hand)
        bet.replace(" ","")
        Card1 = Card(hand, bet)
        Card1.score = HandStrengthP2(Card1)
        stackOfCards.append(Card1)

print("Length: " , len(stackOfCards))
stackOfCards.sort(key = lambda kv: (kv.score))

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
size = len(HighCardsList)+len(OnePairList)+len(TwoPairList)+len(ThreeKindList)+len(FourKindList)+len(FullHouseList)+len(FiveOfKindList)
if size == len(stackOfCards):
    print("Equal")


# with open('output.txt', mode="a") as output:
#     for i in HighCardsList:
#         output.write(i.__str__())
#     for i in OnePairList:
#         output.write(i.__str__())
#     for i in TwoPairList:
#         output.write(i.__str__())
#     for i in ThreeKindList:
#         output.write(i.__str__())
#     for i in FullHouseList:
#         output.write(i.__str__())
#     for i in FourKindList:
#         output.write(i.__str__())
#     for i in FiveOfKindList:
#         output.write(i.__str__())

ans =0
rank = 1
for i in HighCardsList:
    ans +=(i.bet * rank)
    rank+=1
print("Rank1: ", rank,"\n")
for i in OnePairList:
    ans +=(i.bet * rank)
    rank+=1
print("Rank1: ", rank,"\n")
for i in TwoPairList:
    ans +=(i.bet * rank)
    rank+=1
print("Rank1: ", rank,"\n")
for i in ThreeKindList:
    ans +=(i.bet * rank)
    rank+=1
print("Rank1: ", rank,"\n")
for i in FullHouseList:
    ans +=(i.bet * rank)
    rank+=1
print("Rank1: ", rank,"\n")
for i in FourKindList:
    ans +=(i.bet * rank)
    rank+=1
print("Rank1: ", rank,"\n")
for i in FiveOfKindList:
    ans +=(i.bet * rank)
    rank+=1
print("Rank1: ", rank,"\n")
print(rank)
print("ans: ", ans)