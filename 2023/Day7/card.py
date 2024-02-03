from cardDict import CardDictionary
cardDic = CardDictionary.p2Stack()

def HandSort(card:str):
    return cardDic[card]
class Card():
    
    def __init__(self, OrigHand : list, bet : int) :
        self.OrigHand = OrigHand
        self.SortedHand = OrigHand.copy()
        self.SortedHand.sort(reverse=True, key = HandSort)
        self.bet = int(bet)
        self.score = 0
    
    def __str__(self) -> str:
        string = """{OrigHand} {bet}\n"""
        return string.format(OrigHand = self.OrigHand, bet = self.bet, score= self.score)


    def __repr__(self) -> str:
        return self.__str__()
    
    