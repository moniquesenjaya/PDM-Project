#Making a student class with id, fname, lname and gender as their attributes
class Student:

    def __init__(self, studentid, firstname, lastname, gender, picture):
        self.__studentid = studentid
        self.__firstname = firstname
        self.__lastname = lastname
        self.__gender = gender
        self.__picture = picture

    #Using property decorator as getter and setter of the class attributes

    #Student ID getter setter
    @property
    def studentid(self): return self.__studentid
    @studentid.setter
    def studentid(self, value): self.__studentid = value

    #fname getter setter
    @property
    def firstname(self): return self.__firstname
    @firstname.setter
    def firstname(self, value): self.__firstname = value

    #lname getter setter
    @property
    def lastname(self): return self.__lastname
    @lastname.setter
    def lastname(self, value): self.__lastname = value

    #gender getter setter
    @property
    def gender(self): return self.__gender
    @gender.setter
    def gender(self, value): self.__gender = value

    #picture getter setter
    @property
    def picture(self): return self.__picture
    @picture.setter
    def picture(self, value): self.__picture = value

    