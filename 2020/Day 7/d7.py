from collections import defaultdict
import re

mapOfBags = defaultdict(list)
def returnCountOfBags(targetBag:str)->int:
    count =1
    if mapOfBags[targetBag] == [[0,0]]:
        return 1
    for num,bag in mapOfBags[targetBag]:
        count+= (num * returnCountOfBags(bag))
    return count

def p2()->None:
    count=0
    for num,bag in mapOfBags['shiny gold']:
         count+= (num * returnCountOfBags(bag))
    print("Part 2 Answer is: ", count)



def reachesBag(currentBag)->bool:
    if currentBag == 'shiny gold':
        return True
    else:
        for bags in mapOfBags[currentBag]:
            if bags == [0,0]:
                continue
            if reachesBag(bags[1]):
                return True
        return False

def p1()->bool:
    count=0
    for k,v in mapOfBags.items():
        if k =='shiny gold':
            continue
        if reachesBag(k):
            count+=1
    
    print("Part 1 Answer: ",count)

def getBags(InputPath:str)->None:    
    seenBags = set()
    with open(InputPath) as file:
        for line in file:
            line = line.strip()

            bags = line.split("bags contain")
            bag, Innerbag = bags[0].strip(),bags[1]
            seenBags.add(bag)
            Innerbag= Innerbag.replace('bags', "").replace('bag',"").replace('.','')
            Innerbag=Innerbag.strip()            
            if Innerbag == 'no other':
                mapOfBags[bag].append([0,0])
            else:
                ListOfInnerBags = Innerbag.split(',')
                for r in ListOfInnerBags:
                    num="".join(re.findall('\d+',r))
                    r=r.replace(num,"").strip()
                    mapOfBags[bag].append((int(num),r))





def main():
    getBags(r"2020\Day 7\input.txt")
    p1()
    p2()

if __name__=='__main__':
    main()