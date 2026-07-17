
class Person:
    number_of_people=0

    def __init__(self, name):
        self.name= name

    @classmethod
    def number_of_people(cls):
        return cls.number_of_people()




p1=Person("Tim")
print(Person.number_of_people)
p2=Person("Jill")
print(Person.number_of_people)

