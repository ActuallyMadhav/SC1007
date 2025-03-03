# Class ==> basically a user defined variable type with specified attributes and methods

class Student:
    institution_name = "NTU"

    def __init__(self, name, age, cgpa):
        self.__name = name
        self.__age = age
        self.__cgpa = cgpa

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_cgpa(self):
        return self.__cgpa

class StudentList:
    def __init__(self):
        self.__SL = []

    def insert(self, name, age, cgpa):
        self.__SL.append(Student(name, age, cgpa))
    
    def delete(self):
        self.__SL.pop()
    
    def print(self):
        for x in self.__SL:
            print("Name: ", x.get_name(), "\t Age: ", x.get_age(), "\t CGPA: ", x.get_cgpa())

sl = StudentList()
sl.insert('Madhav', 10, 4.0)
sl.insert('Raghu', 20, 4.11)
sl.insert('Pranav', 30, 4.22)
sl.print()
sl.delete()
sl.print()