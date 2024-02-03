import re

def combo1(row, numbers):
    i=0
    hash = []
    for r in row:
        if r =='.':
            if i>0:
                hash.append(i)
            i=0
        elif r=='#':
            i+=1
        else:
            assert False
    if i>0:
        hash.append(i)
    if numbers== hash:
        return True
    else:
        return False

def part1(row, numbers, index):
    if index == len(row):
        if combo1(row, numbers):
            return 1
        else: 
            return 0
    if str(row[index]) == '?':
        temp1= row.copy()
        temp1[index] = '#'
        temp2 = row.copy()
        temp2[index] = '.'
        return (part1(temp1, numbers, index+1) + part1(temp2, numbers, index+1))
    else:
        return (part1(row, numbers, index+1))


total=0
with open('input.txt') as input:
    for line in input:
        row, numbers = line.split(' ')
        row= list(row.strip())
        numbers = numbers.strip()
        numbers= numbers.replace('\n', '')
        numbers= re.findall('\d+', numbers)
        digits = [int(n) for n in numbers]
        score = part1(row , digits,0)
        total+=score

print(total)