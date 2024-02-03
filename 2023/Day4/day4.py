import re
from collections import defaultdict


CardsSeen = defaultdict(int)
def p1(winningCards :list, yourCards: list):
    count=0
    for card in yourCards:
        if winningCards.count(card)>0:
            if count ==0:
                count+=1
            else:
                count = count*2
    return count

def p2(winningCards :list, yourCards: list):
    count=0
    for card in yourCards:
        if winningCards.count(card)>0:
            count+=1
    return count

PoppedCard = []
leftOver = dict()
count=1
with open('input.txt') as input:
    p1Ans = 0
    CopiedCards = []
    for line in input:
        line = line.strip()
        repl = "Card "+str(count)+":"
        line = line.replace(repl,"")
        Cards = line.split("|")
        WinningCards= re.split(" ",Cards[0].strip())
        WinningCards = list(filter(None,WinningCards))
        YourCards = re.split(" ", Cards[1].strip())
        YourCards = list(filter(None,YourCards))

        matchingCards = p1(winningCards=WinningCards, yourCards=YourCards)
        if matchingCards>0:
            p1Ans+= matchingCards
        
        matchedCards = p2(WinningCards,YourCards)
        if count in leftOver.keys():
            leftOver[count] += 1
        else:
            leftOver[count] = 1
        
        for c in range(1,matchedCards+1):
            key = c+count
            if key in leftOver.keys():
                leftOver[key]+=leftOver[count]
            else:
                leftOver[key]=leftOver[count]
        
        count+=1
    print(p1Ans)
    print(sum(leftOver.values()))
        
    

    # while(len(CopiedCards)>0):
    #     num = CopiedCards.pop(0)                    
    #     PoppedCard.append(num)
    #     card = CardsSeen[num]
    #     w = card[0]
    #     y = card[1]
    #     matchedCards = p2(w,y)
    #     if(matchedCards > 0):
    #         for i in range(num,matchedCards+num):
    #             CopiedCards.append(i + 1)
    #     if len(CopiedCards) == 0:
    #         break
    
    # ans = 0
    # for i,v in leftOver.items():
    #     ans +=v
    # #print(CopiedCards)
    # print(leftOver)

    # for c in CopiedCards:
    #     ans +=leftOver[c]
    # print(ans +count-1)
    #print(total)
    #print(len(PoppedCard) + count-1)