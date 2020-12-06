#Making a student class with id, fname, lname and gender as their attributes
class Student:

    def __init__(self, studentid, firstname, lastname, gender, picturepath, present, absent):
        self.__studentid = studentid
        self.__firstname = firstname
        self.__lastname = lastname
        self.__gender = gender
        self.__picturepath = picturepath
        self.__present = present
        self.__absent = absent
    

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

    #picturepath getter setter
    @property
    def picturepath(self): return self.__picturepath
    @picturepath.setter
    def picture(self, value): self.__picturepath = value

    #present getter setter
    @property
    def present(self): return self.__present
    @present.setter
    def present(self, value): self.__present = value

     #absent getter setter
    @property
    def absent(self): return self.__absent
    @absent.setter
    def absent(self, value): self.__absent = value

            