my_list = ["Bhootan","Nepal","France","Italy","Brazil","Germany","USA"]

## INDEX
print(my_list[0])  ## first
print(my_list[-1]) ## last
print(my_list[1])  ## second
print(my_list[-5]) ## fance

print("FIRST NATION IS {}".format(my_list[0]))
print("LAST NATION IS  {}".format(my_list[-1]))
print("NEPAL HAS INDEX POSITION :  {}".format(my_list.index("Nepal")))
print("FRANCE HAS INDEX POSITION : {}".format(my_list.index("France")))

### SLICING
newList = my_list[:]  ## this is the wild card it will return the whole list
print("MAIL LIST : {}".format(my_list))
print("LIST COPIED . NEW LIST IS {}".format(newList))

## PRINT FROM ITALY TO LAST

sliced_list1 = my_list[3:]
print("SLICED LIST 1 IS : {}".format(sliced_list1))
## difficult appeodach
print("SLICED LIST 1 IS : {}".format(my_list[my_list.index('Italy'):]))


## sliced list2
## task make up to Italy 
## from the beginning to Italy
sliced_list2 = my_list[:3]
print("SLICED LIST 1 IS : {}".format(sliced_list2))
## difficult appeodach
print("SLICED LIST 1 IS : {}".format(my_list[:my_list.index('Italy')]))

## task3 
## between nepal and germany
sliced_list3 = my_list[2:5]
print("SLICED LIST 1 IS : {}".format(sliced_list3))
## difficult appeodach
print("SLICED LIST 1 IS : {}".format(my_list[my_list.index('Nepal')+1:my_list.index('Germany')]))

### steps 
### 1) print everything but skip in the rate 1
### 2) print everything but skip in the rate 2 
print(my_list[::2]) ## skip 1 
print(my_list[::3]) ### skip 2

## take from nepal to bazil and skip 1

print(my_list[1:5:2]) ## ans will be nepal and italy
my_list = ["Bhootan","Nepal","France","Italy","Brazil","Germany","USA"]


## with the negative index print
## Germany to Nepal

new_list = my_list[-2:-7:-1]
print(new_list)
# or we can use this too

new_list2 = my_list[-7:-2]
print(new_list2)
