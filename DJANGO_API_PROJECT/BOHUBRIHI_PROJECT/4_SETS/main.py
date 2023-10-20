## what is the main properties of the set
## in the set dta stucture there will be no 
## duplicate value
my_set = set([1,2,3,4,5,6,7,8,9])
print("THE SET VALUE IS  : {} ".format(my_set))
## and there is no sorting in set
my_set = set([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9])
print("THE SET VALUE IS  : {} ".format(my_set))

## find the intersection

myset1 = set([1,2,3,4,5,'a','b','c','d','e'])
myset2 = set([4,5,6,7,8,'a','b','z','t'])

## intersection
print(myset1 & myset2)

## find the union
print(myset1 | myset2)

