my_list = ["Bhootan","Nepal","France","Italy","Brazil","Germany","USA"]

## adding string
my_list.append("Bangladesh")
print(my_list)

## adding integer
my_list.append(2)
print(my_list)

### adding list

my_list.append(['arab','palestain','Iraq'])
print(my_list)

## addind just the values
my_list = ["Bhootan","Nepal","France","Italy","Brazil","Germany","USA"]

my_list.extend(['arab','palestain','Iraq'])
print(my_list)

## insert "Bangladesh" in the 3 index

my_list.insert(3,"Bangladesh")
print(my_list)

my_list.remove("Bangladesh")
print(my_list)

## remove last
my_list.pop()
print(my_list)


## remove italy
my_list.pop(3)
print(my_list)
data_removed = my_list.pop()
print(data_removed)


mylist = ["Tanvir","hasib","Ornob","Tonmoy"]
print("Ornik" not in mylist)  ## true
print("Tanvir" not in mylist) ## false


## yuple packing and unpacking
a = ["Tanvir","Rahman","CDA23"]

fname,lname,address = a
print(fname)
print(lname)
print(address)

## remember item number and variable number should be same
## otherwise it will through en error

a = ["Tanvir","Rahman",["CDA23 Agrabad","Chittaging","Bangladesh"]]

fname,lname,address = a
print(address)
fname,lname,[address,city,country] = a
print(address)
print(city)
print(country)