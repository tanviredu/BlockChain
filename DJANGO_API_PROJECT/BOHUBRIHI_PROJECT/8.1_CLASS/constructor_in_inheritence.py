class A:
    def __init__(self,name):
        self.name = name

    def hello(self):
        print("My Name is : {} ".format(self.name))


class B(A):
    def __init__(self,name,job):
        super().__init__(name)
        self.job = job

    def show_job(self):
        print("My Job is : {} ".format(self.job))

obj1 = B("Tanvir","Software Engineer")
obj1.hello();
obj1.show_job();
