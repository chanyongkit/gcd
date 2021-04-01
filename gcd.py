def gcd(a,b):
    #Error cases
    if(a is None or b is None):
        return -1

    try:
        int(a)
        int(b)
    except ValueError:
        return -1

    #Edge cases
    if(a == 0 or b == 0):
        return 0

    #Get lowest and highest num
    if(a>b):
        highest_num = a
        lowest_num = b
    else:
        lowest_num = a
        highest_num = b

    if(highest_num % lowest_num == 0):
        return lowest_num

    #Apply euclidean algorithm
    while(1):
        remainder = highest_num % lowest_num
        if(lowest_num % remainder == 0):
            return remainder
        else:
            highest_num = lowest_num
            lowest_num = remainder

