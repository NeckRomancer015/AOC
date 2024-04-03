# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
from collections import defaultdict
requiredN = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
required = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
required.sort()


def ValidatePassPort(mapOfFields : defaultdict):
    if 'byr' in mapOfFields:
        if not 1920<=int(mapOfFields['byr'])<=2002:
             return False
    else:
        return False
    
    if 'iyr' in mapOfFields:
        if not 2010<=int(mapOfFields['iyr'])<=2020:
             return False
    else:
        return False    
    
    if 'eyr' in mapOfFields:
        if not 2020<=int(mapOfFields['eyr'])<=2030:
             return False
    else:
        return False

    if 'hgt' in mapOfFields:
        hgt = mapOfFields['hgt']
        if 'in' in hgt:
            hgt=hgt[:-2]
            if not 59<=int(hgt)<=76:
                return False
        elif 'cm' in hgt:            
            hgt=hgt[:-2]
            if not 150<=int(hgt)<=193:
                return False
        else:
            return False
    else:
        return False
    
    if 'hcl' in mapOfFields:
        hcl = mapOfFields['hcl']
        if '#' not in hcl:
            return False
        for i in range(1,len(hcl)):
            if not hcl[i].isdigit():
                if not ord('a')<=ord(hcl[i])<=ord('f'):
                    return False
    else:
        return False
    
    if 'ecl' in mapOfFields:
        if mapOfFields['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']:
            return False
    else:
        return False

    if 'pid' in mapOfFields:
        if len(mapOfFields['pid']) != 9:
            return False
        if mapOfFields['pid'].isdigit() == False and len(mapOfFields['pid']) == 9:
            return False
    else:
        return False
    
    return True

def getPassportsP2(InputPath)->list:
    listOfPassPorts = []
    with open(InputPath) as file:
        pp = defaultdict()
        for line in file:
            if line == "\n":
                listOfPassPorts.append(pp)
                pp = defaultdict()
                continue
            else:
                line = line.strip()
                fields = line.split(" ")
                for field in fields:
                    if "cid" in field:
                        continue
                    row = field.split(":")                    
                    pp[row[0]] = row[1]
    listOfPassPorts.append(pp)
    file.close()
    return listOfPassPorts


def getPassportsP1(InputPath) ->list:
    listOfPassPorts = []
    with open(InputPath) as file:
        pp = []
        for line in file:
            if line == "\n":
                listOfPassPorts.append(pp)
                pp = []
                continue
            else:
                line = line.strip()
                fields = line.split(" ")
                for field in fields:
                    pp.append(field.split(":")[0])
    listOfPassPorts.append(pp)
    file.close()
    return listOfPassPorts

def p1(listOfPassPorts) -> None:
    validPP = 0
    for pp in listOfPassPorts:
        pp.sort()
        if pp == required:
            validPP +=1
        elif pp == requiredN:
            validPP+=1
        
    print("Part 1 Valid passports: ", validPP)


def p2(listOfPassports)->None:
    validPP = 0

    for pp in listOfPassports:
        if ValidatePassPort(pp):
            validPP+=1

    print("Part 2 Valid passports: ", validPP)


def main():
    p1(getPassportsP1(r"2020\Day 4\input.txt"))
    p2(getPassportsP2(r"2020\Day 4\input.txt"))


if __name__ == "__main__":
    main()