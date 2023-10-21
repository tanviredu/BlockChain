## LIST COMPRENSION
## DICTIONARY COPREHENSION
## SET COMPREHENSION


## -----------------------------------
# traditional approach
mylist = [1,2,3,45,6,7,88,33,100]
new_list = []

for item in mylist:
    new_list.append(item*item)

print("TRADITIONAL APPROACH   : {}".format(new_list))

## --------------------------------

## COMPREHENSION approach

new_list2 = [item*item for item in mylist]
print("COMPREHENSION APPROACH : {}".format(new_list2))
