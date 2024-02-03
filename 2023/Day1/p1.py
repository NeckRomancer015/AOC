import re


dig = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
answer=0
def getN(n):    
    if dig.get(n):
        return str(dig[n])
    else:
        return str(n)

def p1(file):
    num =0
    for l in file:
        list = re.findall('\d',l)
        num+=int(list[0]+''+list[-1])
    return num


def p2(file):
    num=0
    for l in file:
        list = re.findall("one|\d|two|three|four|five|six|seven|eight|nine", l)

        list2 = [list[0],list[-1]]
        num+=int(getN(list2[0])+''+getN(list2[-1]))
        print(num)
    return num


def p2V2(file):
    num=0
    for line in file:
        list1 = re.findall("one", line)
        list2 = re.findall("two", line)
        list3 = re.findall("three", line)
        list4 = re.findall("four", line)
        list5 = re.findall("five", line)
        list6 = re.findall("six", line)
        list7 = re.findall("seven", line)
        list8 = re.findall("eight", line)
        listnum = re.findall("0|1|2|3|4|5|6|7|8|9", line)
        list9 = re.findall("nine", line)
        num+=int(getN(list1[0])  +""+ getN(list1[-1]))
        a = str(num)
        with open('outputs.txt',"a") as output:
            l = str(list1)+"  " +str(getN(list1[0])  +""+ getN(list1[-1]))+ "  "+str(int(getN(list1[0])  +""+ getN(list1[-1]))) + "answer: "+a+"\n"
            output.write(l)
    return num

def p2V3(file:str):
    num=0
    for line in file:
        list1  = re.findall('\d', line)
        list2 = re.findall("one|two|three|four|five|six|seven|eight|nine", line)
        list3=[]
        if len(list1) and len(list2):
            if line.find(list1[0]) < line.find(list2[0]):
                list3.append([list1[0]])
            else:
                list3.append([list2[0]])

            if line.find(list1[-1]) > line.find(list2[-1]):
                list3.append([list1[-1]])
            else:
                list3.append([list2[-1]])
            num+=int(getN(str(list3[0])) +""+ getN(str(list3[-1])))
    return num
            


def p2V4(file):
    num=0
    for line in file:
        list1 = re.findall("one", line)
        list2 = re.findall("two", line)
        list3 = re.findall("three", line)
        list4 = re.findall("four", line)
        list5 = re.findall("five", line)
        list6 = re.findall("six", line)
        list7 = re.findall("seven", line)
        list8 = re.findall("eight", line)
        list9 = re.findall("nine", line)
        min = 1000
        max = -1
        t1=''
        t2=''
        if len(list1):
            min = line.find("one")
            t1 = '1'
            t2 = '1'
            max = line.rfind("one")
        if len(list2):
            if line.find("two") < min:
                min = line.find("two")
                t1 = '2'
            if line.rfind("two")>max:
                max = line.rfind("two")
                t2 = '2'
        if len(list3):
            if line.find("three") < min:
                min = line.find("three")
                t1 = '3'
            if line.rfind("three")>max:
                t2= '3'
                max = line.rfind("three")
        if len(list4):
            if line.find("four") < min:
                t1='4'
                min = line.find("four")
            if line.rfind("four")>max:
                t2='4'
                max = line.rfind("four")
        if len(list5):
            if line.find("five") < min:
                min = line.find("five")
                t1='5'
            if line.rfind("five")>max:
                t2='5'
                max = line.rfind("five")
        if len(list6):
            if line.find("six") < min:
                min = line.find("six")
                t1='6'
            if line.rfind("six")>max:
                t2='6'
                max = line.rfind("six")
        if len(list7):
            if line.find("seven") < min:
                min = line.find("seven")
                t1='7'
            if line.rfind("seven")>max:
                t2='7'
                max = line.rfind("seven")
        if len(list8):
            if line.find("eight") < min:
                min = line.find("eight")
                t1='8'
            if line.rfind("eight")>max:
                t2='8'
                max = line.rfind("eight")
        if len(list9):
            if line.find("nine") < min:
                min = line.find("nine")
                t1='9'
            if line.rfind("nine")>max:
                t2='9'
                max = line.rfind("nine")
        if line.find('1') != -1:
            if line.find('1')<min:
                min = line.find('1')
                t1='1'
            if line.rfind('1') > max:
                max = line.rfind('1')
                t2='1'
        if line.find('2') != -1:
            if line.find('2')<min:
                min = line.find('2')
                t1='2'
            if line.rfind('2') > max:
                max = line.rfind('2')
                t2='2'
        if line.find('3') != -1:
            if line.find('3')<min:
                min = line.find('3')
                t1='3'
            if line.rfind('3') > max:
                max = line.rfind('3')
                t2='3'
        if line.find('4') != -1:
            if line.find('4')<min:
                min = line.find('4')
                t1='4'
            if line.rfind('4') > max:
                max = line.rfind('4')
                t2='4'
        if line.find('5') != -1:
            if line.find('5')<min:
                min = line.find('5')
                t1='5'
            if line.rfind('5') > max:
                max = line.rfind('5')
                t2='5'
        if line.find('6') != -1:
            if line.find('6')<min:
                min = line.find('6')
                t1='6'
            if line.rfind('6') > max:
                max = line.rfind('6')
                t2='6'
        if line.find('7') != -1:
            if line.find('7')<min:
                min = line.find('7')
                t1='7'
            if line.rfind('7') > max:
                max = line.rfind('7')
                t2='7'
        if line.find('8') != -1:
            if line.find('8')<min:
                min = line.find('8')
                t1='8'
            if line.rfind('8') > max:
                max = line.rfind('8')
                t2='8'
        if line.find('9') != -1:
            if line.find('9')<min:
                min = line.find('9')
                t1='9'
            if line.rfind('9') > max:
                max = line.rfind('9')
                t2='9'
        num+=int(str(t1)+str(t2))
        print(num)
    return num


            


print(sum)
with open(r'input.txt') as file:
    print(p2V4(file))
    