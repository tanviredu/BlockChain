class A:
    def __init__(self,name):
        self.name = name

    def show(self):
        print("CLASS A METHOD BASE, VALUE: {}".format(self.name))


class B(A):

    ## this is a override function
    def show(self):
        print("HELLO FROM TEE CLASS B");

obj1 = A("Tanvir")
obj1.show();

obj2 = B("Tanvir")
obj2.show();
