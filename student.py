import sqlite3
from PIL import Image  
import PIL 

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


    def get_full_name(self): return f"{self.__firstname} {self.__lastname}"

    #Validation
    
    def validate_empty(self, list_of_textbox):
        for boxes in list_of_textbox:
            if boxes == "":
                return "Please Fill In All The Required Fields."

    def validate_studentid(self):
        conn = sqlite3.connect("Cool_School.db")
        c = conn.cursor()
        c.execute("SELECT studentid FROM students")
        id_list = []
        for item in c.fetchall():
            id_list.append(item[0])
        conn.close()

        # Check if the student id is "SXXXX" where X is int and if it is unique
        if self.__studentid[0] != "S" or len(self.__studentid) != 5 or self.__studentid in id_list:
            return "Invalid StudentID."
        try:
            int(self.__studentid[1:])
        except:
            return "Invalid StudentID."

    def validate_name(self):
        # Check if the student name is string
        if type(self.__firstname) != str or type(self.__lastname) != str:
            return "Name must be all characters."

    def validate_new_number(self):
        # Check if the initial present and absent numbers are 0
        if self.__absent != "0" or self.__present !="0":
            return "Initial absent and present value should be 0."

    def validate_number(self):
        # Check if the present and absent numbers are integers
        num = ["0","1","2","3",'4',"5","6","7","8","9"]
        for i in self.__absent+self.__present:
            if i not in num:
                return "Number of absent and present should be integer."


    # Saving the picture in the known file whenever it is uploaded as student data
    def picture_saving(self):
        path = self.__picturepath
        img1 = Image.open(path)
        name = self.get_full_name()
        newpath = r".\known\{}.jpg".format(name)
        img1 = img1.save(newpath)
        self.__picturepath = newpath

    
            