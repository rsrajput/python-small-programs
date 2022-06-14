num = int(input("Enter a number to check for convergence: "))

def sortAsc(num):
    str_num = str(num)
    num_list = list(str_num)
    sorted_num = sorted(num_list)
    sorted_num = "".join(sorted_num)
    sorted_num = int(sorted_num)
    return(sorted_num)



def sortDesc(num):
    str_num = str(num)
    num_list = list(str_num)
    sorted_num = sorted(num_list, reverse = True)
    sorted_num = "".join(sorted_num)
    sorted_num = int(sorted_num)
    return(sorted_num)

num1 = sortAsc(num)
num2 = sortDesc(num)

result0 = 0
while(True):
    if num1 >= num2:
        bigNum = num1
        smallNum = num2
    else:
        bigNum = num2
        smallNum = num1

    result1 = bigNum - smallNum
    num = result1
    if result1 != result0:
        print("a", num)
        if num == 6174 or num == 495:
            break

    num1 = sortAsc(num)
    num2 = sortDesc(num)
    if num1 == num2:
        print("c", num1)
        break
    else:
        result1 = result0
        continue
