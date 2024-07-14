# Property (decorator)
'''
We use property decorator on any method in the class to use method as property
'''
class Student:
    def __init__(self, Phy, Chem, Maths):
        self.Phy = Phy
        self.Chem = Chem
        self.Maths = Maths

    @property
    def percentage(self):
        return str((self.Phy + self.Chem + self.Maths) / 3) + "%"    

stu1 = Student(98, 97, 99)
print(stu1.percentage)
stu1.Phy = 88
print(stu1.percentage)