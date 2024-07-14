# Class Method 

'''@classmethod is a decorator'''


class Person:
    name = "Anonymous"

    @classmethod
    def ChangeName(cls, name):

        cls.name = name
p1 = Person()        
p1.ChangeName("Shaban Saleem")
print(p1.name)
print(Person.name)