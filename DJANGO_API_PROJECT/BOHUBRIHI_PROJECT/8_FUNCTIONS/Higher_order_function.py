### if one function is taking
### anoter funciton as a parameter
### in that sence usnig map and filter in a function
### is an example of higher order function
### similarly if any function return another function that
### also is a higher order function

def hi(fn):
    fn();

def greet():
    print("Hello")

def hello():
    print("Greet")

hi(hello)
hi(greet)
