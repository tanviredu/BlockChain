## tradiational approach
## even number
## odd number
from typing import List,Set,Dict
def generate_even_number() -> List[int]:
    new_list = []
    for item in range(1,101):
        if item % 2 == 0:
            new_list.append(item)
    return new_list

def generate_odd_number() -> List[int]:
    new_list = []
    for item in range(1,100):
        if item % 2 != 0:
            new_list.append(item)
    return new_list


def COMPRENSION_ODD()-> List[int]:
    return [x for x in range(1,101) if x % 2 != 0]

def COMPRENSION_EVEN()-> List[int]:
    return [x for x in range(1,101) if x % 2 == 0]


print(generate_even_number());
print(generate_odd_number())
print(COMPRENSION_EVEN())
print(COMPRENSION_ODD())
##
