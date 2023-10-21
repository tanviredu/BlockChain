## annonymus functions
## is same as  lambda function
## Effie function
##

## normal function
def concat_names(fname : str,lname : str) -> str:
    return fname + " " + lname

print(concat_names("Tanvir","Rahman"))

## doing this in lambda / annonymous function

c = lambda x,y : x + " " + y

print(c("Tanvir","Rahman"))


## Efie -> immediate execution

print((lambda x,y : x+ ' '+y)("Tanvir","Rahman"))
