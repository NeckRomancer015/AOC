from collections import defaultdict

Boxes = defaultdict(list)

def hashWord(word:str):
    currentValue= 0
    for c in word:
        currentValue+=ord(c)
        currentValue*=17
        currentValue=currentValue%256

    return currentValue

print(hashWord('qp'))

def p1():
    with open('input.txt') as input:
        for line in input:
            line = line.strip().strip('\n')
            words = line.split(',')
            total=0
            for word in words:
                total+=(hashWord(word))
            print(total)


p1()

def p2():
    with open('input.txt') as input:
        for line in input:
            line = line.strip().strip('\n')
            words = line.split(',')
            for word in words:
                if word.count('=')>0:
                    label,focalLength = word.split('=')
                    hashValue = hashWord(label)
                    if len(Boxes[hashValue])==0:
                        Boxes[hashValue].append([label,focalLength])
                    else:
                        box = Boxes[hashValue]
                        replaced = False
                        for b,_ in box:
                            if b == label:
                                index = Boxes[hashValue].index([b,_])
                                Boxes[hashValue].remove([b,_])
                                Boxes[hashValue].insert(index , [label, focalLength])
                                replaced= True
                        if not replaced:
                            Boxes[hashValue].append([label,focalLength])
                elif word.count('-')>0:
                    label,focalLength = word.split('-')
                    hashValue = hashWord(label)
                    removed=False
                    for k,v in Boxes.items():
                        for i in range(len(v)):
                            l,_ = v[i]
                            if l == str(label):
                                Boxes[hashValue].remove(v[i])
                                removed=True
                                break
                        if removed:
                            break


p2()
print(Boxes)

count = 0
ans=0
for k,v in Boxes.items():
    for i in range(len(v)):
        _,focalLength = v[i]
        ans+=((int(k)+1)*(i+1)*(int(focalLength)))

print(ans)
            