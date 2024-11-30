import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
import common_functions


def p1(f):
    gamma= 0
    epsilon = 0
    start = 0
    length = []
    for line in common_functions.read_file_line_by_line(f):
        if start ==0:
            length= [0 for i in range(len(line))]
            start = 1
        
        for l in range(0,len(line)):
            if line[l] == '1':
                length[l]+=1
            else:
                length[l]-=1
    
    binary = ['1' if b>0 else '0' for b in length]
    print(length)
    gamma = "".join(binary)
    epsilon = "".join(['1' if bit == '0' else '0' for bit in gamma])
    
    print(int(gamma,2)*int(epsilon,2))



def find_rating(candidates, criteria):
    bit_length = len(candidates[0])

    for i in range(bit_length):
        if len(candidates) == 1:
            break

        ones = sum(1 for num in candidates if num[i] == '1')
        zeros = len(candidates) - ones

        if criteria == "most_common":
            bit_to_keep = '1' if ones >= zeros else '0'
        elif criteria == "least_common":
            bit_to_keep = '0' if zeros <= ones else '1'

        candidates = [num for num in candidates if num[i] == bit_to_keep]

    return int(candidates[0], 2)  


def calculate_life_support_rating(numbers):
    """Calculate the life support rating."""
    oxygen_rating = find_rating(numbers, "most_common")
    co2_rating = find_rating(numbers, "least_common")
    return oxygen_rating * co2_rating


def p2(f):
    numbers = []
    for line in common_functions.read_file_line_by_line(f):
        numbers.append(line)
    
    print(calculate_life_support_rating(numbers=numbers))

def main():
    f= r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt"
    p1(f)
    p2(f)



if __name__ == '__main__':
    main()