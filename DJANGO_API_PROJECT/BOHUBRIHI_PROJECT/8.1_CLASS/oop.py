class A:
    def __init__(self,name):
        self.name = name

    def show(self)->str:
        return "MY NAME IS  : {} ".format(self.name)

class B(A):
    pass

obj1 = A("Tanvir")
print(obj1.show())
obj2 = A("Rahim")
print(obj2.show())
