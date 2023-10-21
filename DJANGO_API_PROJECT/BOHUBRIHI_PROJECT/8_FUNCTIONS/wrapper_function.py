def myfunction():
    '''THIS FUNCTION RETURN THE HELLO FUNCITON'''
    def hello():
        print("Hello World")
    return hello

f = myfunction();
f()


## up to this concept the wrapper function
## work

def mywrapper(fn):
    def f():
        print("i am first test function")
        fn()
        print("i am seond test function")
    return f

def greet():
    print("I am uder greet function and passed as fn")


g = mywrapper(greet) ## returns the function f()
g() ## executing the function

## like this method wrapper function add additional code
## in your existing code
## in a framework there is always some code you write
## and some code will be added by the framework(or injected)
## this is how this thing works

## to do the same thing we can use a decorator

@mywrapper
def greet():
    print("I am uder greet function and passed as fn")
## this deorator take this greet() method as  aparameter
## of the mywrapper function

greet()
