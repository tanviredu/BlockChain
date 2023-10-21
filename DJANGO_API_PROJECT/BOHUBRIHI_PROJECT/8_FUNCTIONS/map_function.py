### suppose you have a sequence
### and you want to apply a function in every element
### you can do it with a for loop and a function
### or you can use a map() function
### map function
## make square traditional
my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = []
for item in my_list:
    new_list.append(item*item)
print(new_list)
## make square with  list comprehension
print([item * item for item in my_list])
## make it with map function
def func(i):
    return i*i
new_list = list(map(func,my_list))
print(new_list)
## doing with lambda function
new_list = list(map(lambda x:x*x,my_list))
print(new_list)
