from typing import List,Dict,Tuple,Set

## define a list
## i functions . functions will be discussed in detail
## in next chapter
my_list = [1,2,3,4,5,6,7,8,9,10]

def list_comprehension() -> List[int]:
    return [x for x in my_list]


def ditionary_comprehension() -> Dict[int,int]:
    return {i:i*i for i in my_list}


def tuple_comprehension() -> Tuple[int]:
    return tuple(i**4 for i in my_list)


def tuple_under_list_comprehension() -> List[Tuple]:
    return [(i*3,) for i in my_list]

print(list_comprehension())
print(ditionary_comprehension())
print(tuple_comprehension())
print(tuple_under_list_comprehension())

## make comprehension and extract it as a tuple
## from a dictionary

my_dict = {
    "Fname":"Tanvir",
    "Lname": "Rahman",
    "Age" : "29",
    "School": "CUET",
    "City": "Chittagong"
}

def extract(data : Dict) -> List[Tuple]:
    ll = [(i,j) for i,j in data.items()]
    return ll

print(extract(my_dict))
