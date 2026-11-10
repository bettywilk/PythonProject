class Student:
    name = ''

    def __init__(self):
        self.name = ""

    def __repr__(self):  # representation (python rep)
        return self.name


class Classroom:
    list_of_students = [] # the danger

    def __str__(self):
        return str(self.list_of_students[:])


s1 = Student()
s1.name = 'Alice'
s2 = Student()
s2.name = 'Bob'
print(s2)
print(s1)

c1 = Classroom() # created a classroom
c1.list_of_students = [] # c1 now has its own copy of list_of_students
c2 = Classroom() # created another classroom
c2.list_of_students = [] # c2 now has its own copy of list_of_students

c1.list_of_students.append(s1) # added Alice to class 1
c2.list_of_students.append(s2) # added Bob to class 2
c2.list_of_students.append(s1)

print(c1) # prints [‘Alice’] Problem solved
print(c2.list_of_students) # prints [‘Bob’] Problem solved

