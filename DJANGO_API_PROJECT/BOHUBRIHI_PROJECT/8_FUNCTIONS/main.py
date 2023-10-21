## make a fibonacchi number
## function
from typing import List,Dict,Set,Tuple

def fib(limit: int) -> List[int]:
    if limit == 1:
        return [0]
    if limit == 2:
        return [0,1]
    fib = [];
    first  = 0;
    second = 1
    fib.append(first)
    fib.append(second)
    third = first + second
    fib.append(third)
    for item in range(3,limit):
        first = second
        second = third
        third = first+second
        fib.append(third)
    return fib
print(fib(10))




## taking *args to take variable arguments

def take_as_much_method(*args):
    print(args)

## it will take as much argument
## as possible
take_as_much_method("Tanvir","Rahman","orbob",23)
