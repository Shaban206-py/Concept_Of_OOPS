# Constructer
'''
__init__ funtion is called constructor.This function is executed During object creation.All class have this funtion(__init__).As a programer rather you use or not it is always be executed automatically
'''

#Syntax

class Student:
    def __init__(self, name):
     self.name = name  
    print("Adding new Student")

S1 = Student("Ali")
print(S1.name)
