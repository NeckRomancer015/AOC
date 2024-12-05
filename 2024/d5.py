import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
import common_functions
from collections import defaultdict
import math
from copy import deepcopy

def p1(before :defaultdict(list[int]), updates :list[int]):
    ans=0    
    
    for order_update_index in range(0,len(updates)): #goes through each list
        current_list:list = updates[order_update_index]
        isValid = True
        for update_index in range(0,len(current_list)):#goes through the current list
            if not isValid:
                break
            if current_list[update_index] in before.keys():
                for before_index in before[current_list[update_index]]: # checks each page that it must be before
                    if before_index in current_list: # checks if that page is in the updates
                        if update_index<current_list.index(before_index) : # compares the indexes
                            isValid = False
                            break
        if isValid:
            mid = math.ceil((len(current_list)-1)/2)
            ans+=current_list[mid]
    
    print(f"Part 1: {ans}")

def p2(before :defaultdict(list[int]), updates :list[int]):
    ans=0
    
    for order_update_index in range(0,len(updates)): #goes through each list
        current_list:list = deepcopy(updates[order_update_index])
        isChanged = False
        while True:            
            isValid = True
            for update_index in range(0,len(current_list)):#goes through the current list                
                if current_list[update_index] in before.keys(): #safety
                    before_list = before[current_list[update_index]]
                    for before_index in range(0,len(before_list)): # checks each page that it must be before
                        if before_list[before_index] in current_list: # checks if that page is in the updatess                           
                            index2 = current_list.index(before_list[before_index]) # keep index as variable, makes program faster
                            if update_index<index2 :# compares the indexes
                                current_list[update_index],current_list[index2] = current_list[index2],current_list[update_index]
                                isValid = False
                                isChanged=True # This makes sure we check this list further down
                                break
            if isValid:
                    break
        if isChanged:
            mid = math.ceil((len(current_list)-1)/2)
            ans+=current_list[mid]
    
    print(f"Part 2: {ans}")




def main():
    f = r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt"
    before = defaultdict(list[int])
    updates = []
    for line in common_functions.read_file_line_by_line(f):
        if '|' in line:
            first,second = line.split('|')
            before[int(second)].append(int(first))
        elif line:
            updates.append(common_functions.retrieve_numbers.get_numbers_as_int_in_list(line))
    p1(before=before,updates=updates)
    p2(before=before,updates=updates)

if __name__ == '__main__':
    main()