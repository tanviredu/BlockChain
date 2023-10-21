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
    def __init__(self,name,job):
        ## you have to manually give them the
        ## proper value
        A.__init__(self,name)
        B.__init__(self,job)

## question is how do you know which constructor data
## you will be fullfilling class A, or class B
## in this case class A because you called it first

c = C("Tanvir","Student")
c.show1()
c.show2()
