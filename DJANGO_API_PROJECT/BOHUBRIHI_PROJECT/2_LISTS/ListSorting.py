my_list = ["Bhootan","Nepal","France","Italy","Brazil","Germany","USA"]
my_list.sort()
print(my_list)
## compare in lowercase

## suppose we want to add dubai (in small letter
my_list = ["Bhootan","Nepal","France","Italy","Brazil","Germany","USA","dubai"]
my_list.sort()
print(my_list)
## you will see that the dubai comes at last but it has to be after
## Bhootan and Brazil
## its because of ascii value
## to solve this problem we can use this
## when we compare we all convert into lower then we compare it
my_list = ["Bhootan","Nepal","France","Italy","Brazil","Germany","USA","dubai"]
my_list.sort(key=str.lower)
print(my_list)
# now its ok