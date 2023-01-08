def getInput():
    bin_dict = {}
    for char in ['x','y','z']:
        num = int(input(f"Enter {char}1: "))
        pos = int(input(f"Enter {char}2: "))
        bin_dict[f"{char}"] = [num,pos]
    return bin_dict

def decimal2binary(val,lst):
    if val >= 1:
        decimal2binary(int(val/2),lst)
        lst.append(val%2)
    return lst

def eval_bin(val_lst,pos):
    rev_lst = val_lst[::-1]
    return rev_lst[pos]

def main():
    bin_dict = getInput()
    final_lst = []
    has_zero = False
    for num in bin_dict.values():
        lst = []
        # turned decimal value into binary number
        bin = decimal2binary(num[0], lst)
        #evaluate the binary and checked the number at the given position
        final_lst.append(eval_bin(bin, num[1]))

    #check if every value in final_lst is 1.. or if there is a 0 in it
    for i in final_lst:
        if i == 0:
            has_zero = True
    #final check in final_lst if 0 is present or not
    if has_zero == True:
        print('0')
    else:
        print('1')
    

main()