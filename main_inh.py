#Concept Of Inheritance

'''
When one class (child) derives the properties and method of another class (parent/base)
'''
'''
There three types of Inheritance are given below
'''
#Single Inheritance


class Car:
    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def stop():
        print("Car Stopped")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

Car1 = ToyotaCar ("Fortuner")        
Car2 = ToyotaCar("Prius")
print(Car1.start())



#Note @staticmethod is used in this example



#Multi_Level Inheritance
class FirstYear:
    def __init__(self, student_marks):
        self.Student_Marks = student_marks        
        self.Total_Students = list(student_marks.keys())

class Overall_Result(FirstYear):
    def __init__(self, student_marks, max_mark_per_student):
        super().__init__(student_marks)
        self.max_mark_per_student = max_mark_per_student

    def calculate_overall_percentage(self):
        total_marks_obtained = sum(self.Student_Marks.values())
        total_students = len(self.Student_Marks)
        total_possible_marks = total_students * self.max_mark_per_student
        overall_percentage = (total_marks_obtained / total_possible_marks) * 100
        return overall_percentage


s1 = Overall_Result({"Ali": 78, "Ahmed": 91, "Rafy": 70}, 100)
print(s1.Total_Students) 
print(s1.Student_Marks) 
print(s1.calculate_overall_percentage())  # Output: 79.666


          #Multiple Inheritance

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)  
print(c1.varB)  
print(c1.varA)  
