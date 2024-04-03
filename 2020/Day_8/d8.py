from typing import List
import random
import copy

class Instruction():
    def __init__(self, operation:str ,argument:int  ,uniqueID:int) -> None:
        self.operation = operation
        self.argument = argument
        self.uniqueID = uniqueID

    def __str__(self) -> str:
        return "{operation} {argument} {uniqueID}".format(operation = self.operation, argument=self.argument, uniqueID = self.uniqueID)
    
    def __repr__(self) -> str:
        return self.__str__()

# Global Variables#
listOfInstructions : List[Instruction] = []
accumulator = 0
changed = set()


#Helper functions#
def createUniqueInstructions(InputPath:str)->None:
    with open(InputPath) as file:
        count=0
        for instruction in file:            
            instruction = instruction.strip()
            operation,argument = instruction.split(" ")
            newInstruction = Instruction(operation=operation,argument=int(argument), uniqueID=count)
            listOfInstructions.append(newInstruction)
            count+=1
    file.close()

def proccesInstruction(instruction : Instruction) -> Instruction:
    global accumulator
    nextIns = 1
    if instruction.operation == 'nop':
        pass
    elif instruction.operation == 'acc':
        accumulator+=instruction.argument
    elif instruction.operation == 'jmp':
        nextIns=instruction.argument
    
    return listOfInstructions[instruction.uniqueID+nextIns]

def proccesInstructionWithMutation(instruction : Instruction, copyOfInstructions : list[Instruction]) -> Instruction:
    global accumulator
    nextIns = 1
    if instruction.operation == 'nop':
        pass
    elif instruction.operation == 'acc':
        accumulator+=instruction.argument
    elif instruction.operation == 'jmp':
        nextIns=instruction.argument
    
    return copyOfInstructions[instruction.uniqueID+nextIns]

def MutateRandomArgument() -> list[Instruction]:
    changedInstructions = copy.deepcopy(listOfInstructions)
    
    while True:
        element = random.choice(changedInstructions)
        if element in changed:
            continue
        if element.operation == 'nop':            
            element.operation = 'jmp'
            changed.add(element)
            return changedInstructions
        elif element.operation == 'jmp':
            element.operation = 'nop'
            changed.add(element)
            return changedInstructions

#Part 1 and 2       
def p1()->None:
    global accumulator
    currentInstruction = listOfInstructions[0]
    seen = set()
    while True:
        if currentInstruction in seen:
            break
        seen.add(currentInstruction)
        currentInstruction = proccesInstruction(currentInstruction)

    print("Part 1 Answer is:", accumulator)

def p2()->None:
    global accumulator
    accumulator=0 if accumulator>0 else accumulator # because of p1
    changedInstructions = MutateRandomArgument()
    possibleChanges = sum(1 for x in listOfInstructions if x in ['nop','jmp'])

    currentInstruction = changedInstructions[0]   
    seen = set()    
    while True:
        if currentInstruction in seen:
            accumulator=0
            changedInstructions = MutateRandomArgument() 
            currentInstruction = changedInstructions[0]
            seen = set()
            continue
        
        seen.add(currentInstruction)

        if currentInstruction.uniqueID == len(listOfInstructions)-1: # last instruction
            if currentInstruction.operation == 'acc': # in case it is acc and accumulsator changes
                accumulator+=currentInstruction.argument
            break

        currentInstruction = proccesInstructionWithMutation(currentInstruction, changedInstructions)

        if len(changed) == possibleChanges:
            print("Part 2 failed")
            return
    
    print("Number of mutations: ", len(changed))
    print("Part 2 Answer is: ", accumulator)



# Main Function
def main():
    createUniqueInstructions(r"2020\Day 8\input.txt")
    p1()
    p2()


if __name__ == '__main__':
    main()