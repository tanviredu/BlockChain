
def BIG_O_1():
    array = [0,1,2,3,4]
    print(array[3])


def BIG_O_N():
    array = [0,1,2,3,4,5,6,7,8,9,10]
    for item in array:
        if item == 5:
            print("five is here")


def BIG_LOG_N():
    ## FIND 5 IN THAT LIST
    ARRAY = [1,2,3,4,5,6,7,8,9,10]
    print("ARRAY:")
    print(ARRAY)

    ## find the mid point
    midpoint = int(len(ARRAY)/2)
    print("Mid point is {}".format(ARRAY[midpoint]))
    ## mid point is 6 so we take the left half because
    ## 5<6

    ARRAY = ARRAY[:midpoint]
    print("new array")
    print(ARRAY)

    ## devide it further

    midpoint = int(len(ARRAY)/2)
    print("new midpoint {}".format(ARRAY[midpoint]))

    ## mid point is 3 which is less than 5 so we no longer
    ## go to the left side we go to the right side

    ARRAY = ARRAY[midpoint:]
    print(ARRAY)

    midpoint = int(len(ARRAY)/2)
    print("new midpoint {}".format(ARRAY[midpoint]))
    print(midpoint)
    ## midpoint is 4 which is less than 5 so we go right
    ## but in the right there is only 5
    ## so the answer if 5
    ## it takes less than full iteration 
    ## but it is greater than O(1)




def BIG_N_2():
    ARRAY = [0,1,2,3,4,5]
    for i in range(len(ARRAY)):
        for j in range(len(ARRAY)):
            print(i*j)

BIG_N_2();    

