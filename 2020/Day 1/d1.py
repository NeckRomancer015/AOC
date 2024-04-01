

def p1(listOfExpenses: list) -> int:
    for i in range(0, len(listOfExpenses)-1):
        for j in range(i+1, len(listOfExpenses)):
            if listOfExpenses[i]+listOfExpenses[j] == 2020:
                return listOfExpenses[i]*listOfExpenses[j]
    return 0

def p2(listOfExpenses: list) -> int:
    for i in range(0, len(listOfExpenses)-2):
        for j in range(i+1, len(listOfExpenses)-1):
            for k in range(j+1, len(listOfExpenses)):
                if listOfExpenses[i]+listOfExpenses[j] +listOfExpenses[k]== 2020:
                    return listOfExpenses[i]*listOfExpenses[j] *listOfExpenses[k]   

    return 0

def returnInput(pathToInput: str) -> list:
    listOfExpenses = []
    with open(pathToInput) as file:
        for line in file:
            listOfExpenses.append(int(line.strip()))
    file.close()
    return listOfExpenses


def main():
    ListOfExpenses = returnInput(r"2020\Day 1\input.txt")
    print("P1 anwer is : ", p1(listOfExpenses=ListOfExpenses))
    print("P2 answer is : ", p2(listOfExpenses=ListOfExpenses))


if __name__=="__main__":
    main()