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

