import re
class PasswordRule():
    def __init__(self, min: int, max: int, char : str) -> None:
        self.min = int(min)
        self.max = int(max)
        self.char = char

    def __str__(self) -> str:
        return """
        Min : {min}
        Max : {max}
        char : {char}
        """.format(char = self.char, min = self.min, max= self.max)
    
    def __repr__(self) -> str:
        return "{char} {min} {max}".format(char = self.char, min = self.min, max= self.max)


def ValidP1(rule : PasswordRule, pw:str) ->bool:
    count = len(re.findall(rule.char, pw))
    if rule.min <=count<=rule.max:
        return True
    return False



def createRule(rule:str)->PasswordRule:    
    nums= re.findall('\d+', rule)
    min,max= nums[0],nums[1]
    char = rule[-1]
    return PasswordRule(min=min, max=max, char=char)

def returnInput(pathToInput: str) -> list:
    listOfPwAndRule = []
    with open(pathToInput) as file:
        for line in file:
            r, pw = line.strip().split(": ")
            rule = createRule(r)
            listOfPwAndRule.append([rule,pw])
    file.close()
    return listOfPwAndRule

def p1(p1Input:list) -> None:
    validPw = 0
    for rule,pw in p1Input:
        if ValidP1(rule=rule, pw=pw):
            validPw+=1
    print("Part 1 Total : ", validPw)

def ValidP2(pw:str, rule:PasswordRule)->bool:
    if pw[rule.min-1] == rule.char==pw[rule.max-1]:
        return False
    if pw[rule.max-1] == rule.char:
        if rule.char != pw[rule.min-1]:
            return True
    if pw[rule.min-1] == rule.char:
        if rule.char != pw[rule.max-1]:
            return True
        
    return False
def p2(p2Input: list)->None:
    validPw = 0
    for rule,pw in p2Input:
        if ValidP2(pw,rule):
            validPw+=1
    print("Part 2 Total : ", validPw)
    
        

def main():
    Input = returnInput(r"2020\Day 2\input.txt")
    p1(p1Input=Input)
    p2(p2Input = Input)



if __name__=="__main__":
    main()

