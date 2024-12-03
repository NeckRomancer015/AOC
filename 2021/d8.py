import sys
sys.path.append(r"C:\Users\user-pc\Documents\PythonProj\AOC")
import common_functions

correct_nums = {0:'abcefg',1:'cf', 2:'acdeg',3:'acdfg',4:'bcdf',5:'abdfg',6:'abdefg',7:'acf',8:'abcdefg',9:'abcdfg'}

def p1(f):
    unique_number_seg = 0
    for line in common_functions.read_file_line_by_line(f):
        _, second = line.strip().split('|')
        signals = second.strip().split(' ')
        for sig in signals:
            if len(sig.strip()) in (2,3,4,7):
                unique_number_seg+=1
    
    print(f"Part 1 :{unique_number_seg}")

def p2(f):
    ans =0
    for line in common_functions.read_file_line_by_line(f):
        first, second = line.strip().split('|')
        signals = second.strip().split(' ')
        first = first.strip().split(" ")
        
        for i in range(0,len(signals)):
            signals[i] = "".join(sorted(signals[i]))
        
        for i in range(0,len(first)):
            first[i] = "".join(sorted(first[i]))
        nums = {}
        first.sort(key =len)
        nums[1] = first[0]
        nums[7] = first[1]
        nums[4] = first[2]
        nums[8] = first[-1]
        
        while len(nums.keys()) !=10:
            for sig in first:
                if sig not in nums.values():
                    if len(sig) == 6:
                        if 6 not in nums.keys():
                            t= ''
                            t = nums[1]
                            in_six = False
                            for i in nums[1]:
                                if i not in sig:
                                    in_six = True
                                    break
                            if in_six:
                                nums[6] = sig
                                break
                        if 9 not in nums.keys():
                            in_sig = True
                            for i in nums[4]:
                                if i not in sig:
                                    in_sig = False
                                    break
                            if in_sig:
                                nums[9] = sig
                                break
                        else:
                            nums[0] = sig
                            break
                    elif len(sig) == 5:
                        if 3 not in nums.keys():
                            in_sig = True
                            for i in nums[1]:
                                if i not in sig:
                                    in_sig = False
                                    break
                            if in_sig:
                                nums[3] = sig
                                break
                        else:
                            if 5 not in nums.keys():
                                t = ''
                                t = nums[4]
                                for i in nums[1]:
                                    t= t.replace(i,"")

                                in_sig = True
                                for i in t:
                                    if i not in sig:
                                        in_sig = False
                                        break
                                if in_sig:
                                    nums[5] = sig
                            else:
                                nums[2] = sig
        
        val = {v:k for k,v in nums.items()}
        right = ''
        for sig in signals:
            right += str(val[sig])
        ans+=int(right)
    print(f"Part 2 :{ans}")









def main():
    f = r"C:\Users\user-pc\Documents\PythonProj\AOC\ex.txt"
    p1(f)
    p2(f)
if __name__ == '__main__':
    main()