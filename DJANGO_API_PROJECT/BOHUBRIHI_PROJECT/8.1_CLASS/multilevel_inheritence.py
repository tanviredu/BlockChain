### multiple inheritence

class A:
    def __init__(self,name):
        self.name = name

    def show(self):
        print("NAME : {} ".format(self.name))


class B(A):
    def __init__(self,name,job):
        super().__init__(name)
        self.job = job

    ## when the derived class call this METHOD
    ## base class wont be called
    ## this is the override function
    ## this will be called
    def show(self):
        print("JOB : {} ".format(self.job))


class C(B):
    pass


c=C("Tanvir","Student")
c.show()
#c.show2()
