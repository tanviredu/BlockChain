## loop in range
for item in range(1,101):
    print(item,end=" ")
## loop in set
print()
my_set = set([1,2,3,4,5,6,7,8,9])
for item in my_set:
    print(item,end=" ")
## loop in list
print()
my_list = ["Bhootan","Nepal","France","Italy","Brazil","Germany","USA"]
for item in my_list:
    print(item,end=" ")

## loop in dictionary
my_dict = {
    "Fname":"Tanvir",
    "Lname": "Rahman",
    "Age" : "29",
    "School": "CUET",
    "City": "Chittagong"
}
print()
for i,j in my_dict.items():
    print(i+ "   ->   " + j )


for i in range(len(my_list)):
    print(my_list[i])
