import re
import itertools
def makeProducts(row:str):
    listOfStuff = ['.', '#']
    return set(itertools.product(listOfStuff, repeat = len(row)))


def removeFromList(row:str, prod:set):
    for i in range(len(row)):
        if (str(row[i]) == '.' or str(row[i]) == '#') and str(row[i])!=str(prod[i]):
            return True
    return False

prods = []
ans =0
with open('input.txt') as input:
    for line in input:
        row, numbers = line.split(' ')
        row= row.strip()
        numbers = numbers.strip()
        numbers= numbers.replace('\n', '')
        numbers= re.findall('\d+', numbers)
        prods = makeProducts(row)

        copyOfProd = prods.copy()
        for p in copyOfProd:
            temp = ''.join(str(e) for e in p)
            num = re.findall('#+', temp)
            if removeFromList(row,p):
                prods.remove(p)
        ans+= len(prods)

print(ans)