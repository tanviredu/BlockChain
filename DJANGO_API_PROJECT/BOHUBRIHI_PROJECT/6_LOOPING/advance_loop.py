## print the value with its index

my_list1 = ["Bhootan","Nepal","France","Italy","Brazil","Germany","USA"]
for i,j in enumerate(my_list1):
    print("INDEX : {} ---> VALUE : {}".format(i,j))
my_list2 = [1,2,3,4,5,6,7]


## print two same length list in 1 for loop
for i,j in zip(my_list1,my_list2):
    print("FROM LIST1 : {}  ---- FROM LIST2 :{}".format(i,j))

for item in reversed(my_list2):
    print(item,end=" ")

print()

for item in sorted(reversed(my_list2)):
    print(item,end=" ")