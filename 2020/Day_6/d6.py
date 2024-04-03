

def p1(InputFile:str)->None:
    YesPeople = list()
    with open(InputFile) as file:
        group=set()
        for line in file:
            if line == '\n':
                YesPeople.append(len(group))
                group=set()
            else:
                line = line.strip()
                for question in line:
                    group.add(question)
        else:
            YesPeople.append(len(group))
    file.close()

    print("Part 1 answer: ",sum(YesPeople))

def countAll(questions:list, seen:set)->int:
    maxValue = 0

    for answer in seen:
        inAllQuestions = True
        for question in questions:
            if answer not in question:
                inAllQuestions = False
        if inAllQuestions:
            maxValue+=1               

    return maxValue

def p2(InputFile:str)->None:
    AllYes = list()
    total = 0
    with open(InputFile) as file:
        group = list()
        seen = set()
        for line in file:
            if line== '\n':
                total += countAll(questions=group, seen=seen)
                group=list()
                seen = set()
            else:
                line=line.strip()
                for i in line:
                    seen.add(i)
                group.append(line)
        else:
            total+=countAll(questions=group, seen=seen)
    
    print("Part 2 answer: ",total)


def main():
    p1(InputFile=r"2020\Day 6\input.txt")
    p2(InputFile=r"2020\Day 6\input.txt")




if __name__=='__main__':
    main()
        