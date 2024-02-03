from collections import defaultdict
class CardDictionary():
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def CardDict():
        cardDict = defaultdict(int)
        for i in range(2,10):
            cardDict[str(i)]=i

        cardDict['T'] = 10
        cardDict['J'] = 11
        cardDict['Q'] = 12
        cardDict['K'] = 13
        cardDict['A'] = 14

        return cardDict

    @staticmethod
    def p2Stack():
        cardDict = defaultdict(int)        
        cardDict['J'] = 1
        for i in range(2,10):
            cardDict[str(i)]=i

        cardDict['T'] = 10
        cardDict['Q'] = 11
        cardDict['K'] = 12
        cardDict['A'] = 13

        return cardDict