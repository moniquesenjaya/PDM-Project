from tkinter import *
from tkinter import messagebox, ttk, filedialog
from PIL import ImageTk, Image
import os
import sqlite3

class Menu():

    
    def __init__(self, root):
        self.__root = root
        self.__root.title('Cool School Attendance Application')
        self.__root.geometry("1350x700+0+0")
        self.__root.config(bg="sky blue")

        #open file dialog
        def open():
            root.filename = filedialog.askopenfilename(initialdir="/desktop", title="Select the picture", filetypes=(("png files", "*.png"),("jpeg files", "*.jpeg"),("jpg files", "*.jpg")))
            picturepath_text.insert(END, root.filename)

        def open_first():
            root.filename = filedialog.askopenfilename(initialdir="/desktop", title="Select the picture", filetypes=(("png files", "*.png"),("jpeg files", "*.jpeg"),("jpg files", "*.jpg")))
            picturepath_text.insert(END, root.filename)
            
            

        titlelbl = Label(self.__root, font=("Helvetica", 40, "bold"), bd =3, text = "Cool School Attendance System", relief=GROOVE, bg = "sky blue")
        titlelbl.pack(side=TOP, fill=X)

        #Entry Form for the program

        entry_frame = Frame(self.__root, bd=3, relief=RIDGE, bg="light gray")
        entry_frame.place(x=20, y=100, width=450, height=560)

        entry_title = Label(entry_frame, text="Student Information",bg="light gray", font=("Helvetica", 20, "bold"))
        entry_title.grid(row=0, columnspan=2, pady=20, padx=10, sticky="w")

        studentid_label = Label(entry_frame, text = "Student ID:",bg="light gray", font=("Helvetica", 16, "bold"))
        studentid_label.grid(row=1, column=0, pady=5, padx=20, sticky="w")
        studentid_text = Entry(entry_frame, font=("Helvetica", 16), bd=3, relief=GROOVE)
        studentid_text.grid(row=1, column=1, padx=8, pady=5, sticky = "w",columnspan=2)

        firstname_label = Label(entry_frame, text = "First Name:",bg="light gray", font=("Helvetica", 16, "bold"))
        firstname_label.grid(row=2, column=0, pady=5, padx=20, sticky="w")
        firstname_text = Entry(entry_frame, font=("Helvetica", 16), bd=3, relief=GROOVE)
        firstname_text.grid(row=2, column=1, padx=8, pady=5, sticky = "w",columnspan=2)

        lastname_label = Label(entry_frame, text = "Last Name:",bg="light gray", font=("Helvetica", 16, "bold"))
        lastname_label.grid(row=3, column=0, pady=5, padx=20, sticky="w")
        lastname_text = Entry(entry_frame, font=("Helvetica", 16), bd=3, relief=GROOVE)
        lastname_text.grid(row=3, column=1, padx=8, pady=5, sticky = "w",columnspan=2)

        gender_label = Label(entry_frame, text = "Gender:",bg="light gray", font=("Helvetica", 16, "bold"))
        gender_label.grid(row=4, column=0, pady=5, padx=20, sticky="w")
        gender_combobox = ttk.Combobox(entry_frame, font=("Helvetica", 15), state="readonly")
        gender_combobox['values'] = ("Male", "Female", "Others")
        gender_combobox.grid(row=4, column=1, pady=5,columnspan=2)

        picturepath_label = Label(entry_frame, text = "Picture:",bg="light gray", font=("Helvetica", 16, "bold"))
        picturepath_label.grid(row=5, column=0, pady=5, padx=20, sticky="w")
        picturepath_text = Entry(entry_frame, font=("Helvetica", 12), bd=3, relief=GROOVE)
        picturepath_text.grid(row=5, column=1, padx=8, pady=5, sticky = "w")
        picturepath_button = Button(entry_frame, text="Choose", command=open_first)
        picturepath_button.grid(row=5, column=2, pady=5)

        present_label = Label(entry_frame, text = "Present:",bg="light gray", font=("Helvetica", 16, "bold"))
        present_label.grid(row=6, column=0, pady=5, padx=20, sticky="w")
        present_text = Entry(entry_frame, font=("Helvetica", 16), bd=3, relief=GROOVE)
        present_text.grid(row=6, column=1, padx=8, pady=5, sticky = "w",columnspan=2)
        present_text.insert(END, 0)

        absent_label = Label(entry_frame, text = "Absent:",bg="light gray", font=("Helvetica", 16, "bold"))
        absent_label.grid(row=7, column=0, pady=5, padx=20, sticky="w")
        absent_text = Entry(entry_frame, font=("Helvetica", 16), bd=3, relief=GROOVE)
        absent_text.grid(row=7, column=1, padx=8, pady=5, sticky = "w",columnspan=2)
        absent_text.insert(END, 0)
        

        lastname_label = Label(entry_frame, text = "Last Name:",bg="light gray", font=("Helvetica", 16, "bold"))
        lastname_label.grid(row=3, column=0, pady=5, padx=20, sticky="w")
        lastname_text = Entry(entry_frame, font=("Helvetica", 16), bd=3, relief=GROOVE)
        lastname_text.grid(row=3, column=1, padx=8, pady=5, sticky = "w",columnspan=2)
        

        #Button Frame
        button_frame = Frame(entry_frame, bd=0, relief=RIDGE, bg="light gray")
        button_frame.place(x=10, y=500, width=420)

        add_button = Button(button_frame, text="Add", bd=4, width =10)
        add_button.grid(row=0, column=0, padx=10)

        update_button = Button(button_frame, text="Update", bd=4, width =10)
        update_button.grid(row=0, column=1, padx=10)

        delete_button = Button(button_frame, text="Delete", bd=4, width =10)
        delete_button.grid(row=0, column=2, padx=10)

        clear_button = Button(button_frame, text="Clear", bd=4, width =10)
        clear_button.grid(row=0, column=3, padx=10)

        #Database frame
        table_frame = Frame(self.__root, bd=3, relief=RIDGE, bg="light gray")
        table_frame.place(x=500, y=100, width=800, height=560)

        search_by_label = Label(table_frame, text = "Search by:",bg="light gray", font=("Helvetica", 13, "bold"))
        search_by_label.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        search_by_combobox = ttk.Combobox(table_frame, font=("Helvetica", 10), state="readonly", width=10)
        search_by_combobox['values'] = ("StudentID", "First Name", "Last Name")
        search_by_combobox.grid(row=0, column=1, pady=10)

        search_text = Entry(table_frame, font=("Helvetica", 13), bd=3, relief=GROOVE)
        search_text.grid(row=0, column=2, padx=5, pady=10, sticky = "w")

        search_button = Button(table_frame, text="Search", bd=4, width =10)
        search_button.grid(row=0, column=3, padx=10)

        cancel_button = Button(table_frame, text="Cancel", bd=4, width =10)
        cancel_button.grid(row=0, column=4, padx=10)

        attendance_button = Button(table_frame, text="Attendance", command=open, width=15, bd=4)
        attendance_button.grid(row=0, column=5, padx=10)

        #List frame
        list_frame = Frame(table_frame, bd=4, relief=RIDGE, bg="light gray")
        list_frame.place(x=10, y=70, width=760, height=470)

        scroll_x = Scrollbar(list_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(list_frame, orient=VERTICAL)
        student_table = ttk.Treeview(list_frame, columns=("studentid, firstname, lastname, gender, picture, present, absent"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=student_table.xview)
        scroll_y.config(command=student_table.yview)
        student_table.heading(0, text="Student ID")
        student_table.heading(1, text="Fisrt Name")
        student_table.heading(2, text="Last Name")
        student_table.heading(3, text="Gender")
        student_table.heading(4, text="Picture")
        student_table.heading(5, text="Present")
        student_table.heading(6, text="Absent")
        student_table["show"] = 'headings'
        student_table.column(0, width=100)
        student_table.column(1, width=150)
        student_table.column(2, width=150)
        student_table.column(3, width=100)
        student_table.column(4, width=200)
        student_table.column(5, width=50)
        student_table.column(6, width=50)
        student_table.pack(fill=BOTH,expand=1)

'''
    #Database

    #Creating the database
    conn = sqlite3.connect('Cool_School.db')

    #Creating cursor
    c = conn.cursor()

    #Creating table

    c.execute("""CREATE TABLE students(
        studentid text,
        firstname text,
        lastname text,
        gender text,
        picturepath text,
        present int,
        absent int
        )""")

'''

if __name__ =='__main__':
    root = Tk()
    application = Menu(root)
    root.mainloop()