def variable_kwargs(**kwargs):
    print(kwargs)

variable_kwargs(name="Tanvir",age=29,profession = "student")

def doing_both(*args,**kwargs):
    print(args,kwargs)

doing_both("Tanvir","Rahman","ornob",name="Ornik",alias="aaaron",age=23)

## args will take the value without the key value and
## stored it in a tuple

## kwargs will take the key value pair and stored in a dictionary
