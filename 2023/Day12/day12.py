import itertools
import re

def combop1(row:str, numbers):
    rowSplit = re.findall('#+',row)
    if len(rowSplit) != len(numbers):
        return False
    else:
        for i in range(len(rowSplit)):
            if len(rowSplit[i]) != int(numbers[i]):
                return False
    return True


def subCombos(row:str, ListOfCombos:list, index:int, numbers):
    numOfSubs = len(ListOfCombos)
    ques ='?'
    temp = row
    ans=0
    i=index
    b = False
    while True:
        combos = ListOfCombos[i]
        for c in combos:
            ques = '?'*len(c)
            sub=''.join(str(e) for e in c)
            temp =temp.replace(ques,sub,1)
            print(temp)
            if temp.count('?')>=1:
                ans +=subCombos(temp,ListOfCombos, i+1,numbers=numbers)
            else:
                if combop1(temp,numbers=numbers):
                    ans+=1
            temp=row
        return ans



def makeCombo(row:str):
    listOfStuff = ['.', '#']
    count = 0
    copyOfRow = row
    ListOfCombos = []
    combinations = []
    for i in range(len(row)+1):
        if i== len(row):
            if count>0:
                combinations = list(itertools.product(listOfStuff, repeat = count))            
                ListOfCombos.append(combinations)
                count=0
                break
        if str(row[i])=='?':
            count+=1
        if str(row[i])!='?' and count>0:
            combinations = list(itertools.product(listOfStuff, repeat = count))

            count=0
            
    if count>0:
        ListOfCombos.append(combinations)
    return ListOfCombos

total=0
with open('input.txt') as input:
    for line in input:
        row, numbers = line.split(' ')
        row= row.strip()
        numbers = numbers.strip()
        numbers= numbers.replace('\n', '')
        numbers= re.findall('\d+', numbers)
        print(row)
        print(numbers)
        total+=subCombos(row ,makeCombo(row),0, numbers)

print(total)