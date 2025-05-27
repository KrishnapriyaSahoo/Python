class Student:
    college_name="nalanda"
    name="anonymous"#class attribute
    def __init__(self,name):
        self.name=name#object attribute
s1=Student("karan")
print(s1.name)
#object attribute has high precedence than class attribute

#Methods
#Methods are functions that belong to objects
#Class is a collection of objects and methods
class Teacher:
    def h(self):
        g="college"
        print("I study in ",g)
    def k(self):
        print("hello world!")
t=Teacher()
t.h()
t.k()
