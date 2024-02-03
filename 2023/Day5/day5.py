import re
seedArray = []
with open('input.txt') as input:
    seeds = re.findall('\d+',input.readline())
    print(seeds)
    
        