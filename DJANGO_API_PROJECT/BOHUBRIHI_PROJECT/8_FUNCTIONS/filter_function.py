## filter function
## supose you have a list of numbers
## and you want to find the even numberrs from the list
## you can use the filter function like
## you write a function that take a parameter and checks if it is
## even or not . if it is even then return True and if not return False
## then you pass the function name in the filter method and with the list
## it will give you a even number list
## remember the filter function only takes a function that return true or false
## thats the difference between map and filter method

## find the even number between 1 to 20

## regular process with a for lopp

from typing import List

def loop_method() -> List[int]:
    evenlist = []
    for item in range(1,21):
        if item%2 == 0:
            evenlist.append(item)
    return evenlist

def isEven(number : int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False
