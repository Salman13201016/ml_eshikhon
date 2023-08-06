class Person:
    # name ="salman"

    def __init__(self,name,age,year):
        self.firstname = name
        self.age = age
        self.year = year
    def information(self): 
        return [self.firstname,self.age]


class Student(Person):
    def __init__(self,name,age,year):
        super().__init__(name,age,year)
        self.grad_year = year
    def welcome (self):
        print("welcome", self.firstname,self.age, "to this university")

x = Student("salman",30,2017)
result = x.information()
x.welcome()

