from math import gcd
import re

def next_departure_time(earliest_timestamp, bus_id):
    return ((earliest_timestamp // bus_id) + 1) * bus_id if earliest_timestamp % bus_id != 0 else earliest_timestamp        


def p1(busID :list[int],tmStamp:int):
    earliestTmStamp=0
    earliestBus=0
    for bus in busID:
        if earliestTmStamp==0:
            earliestTmStamp=next_departure_time(tmStamp,bus_id=bus)
            earliestBus=bus
        else:
            if earliestTmStamp>next_departure_time(bus_id=bus,earliest_timestamp=tmStamp):
                earliestTmStamp = next_departure_time(bus_id=bus,earliest_timestamp=tmStamp)
                earliestBus=bus
    
    print("Part 1 answer is: ",earliestBus*(earliestTmStamp-tmStamp))

def getInput(FilePath):
    tmStamp = 0
    busID=[]
    AllBusses = ''
    with open(FilePath) as file:
        tmStamp=int(file.readline().strip())
        AllBusses = file.readline().strip()
        busID = re.findall(r'\d+',AllBusses)
        busID = [int(num) for num in busID]
    return busID,tmStamp,AllBusses
    
def p2(AllBusses):
    buses = [(int(bus), offset) for offset, bus in enumerate(AllBusses.split(',')) if bus != 'x']
    print(buses)
    t = 0
    step = 1
    
    for bus, offset in buses:
        while (t + offset) % bus != 0:
            t += step
        step *= bus     

    print(f"p2: {t}")



def main():
    busId,tmStamp, AllBusses = getInput(r"ex.txt")
    p1(busID=busId,tmStamp=tmStamp)
    p2(AllBusses)

if __name__ == '__main__':
    main()