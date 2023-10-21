class A:
    def __init__(self,name):
        self.name = name
    def show1(self):
        print("NAME IS : {}".format(self.name))

class B:
    def __init__(self,job):
        self.job = job

    def show2(self):
        print("JOB IS : {}".format(self.job))

class C(A,B):
    pass

## question is how do you know which constructor data
## you will be fullfilling class A, or class B
## in this case class A because you called it first

c = C("Tanvir")
c.show1()
c.show2()
