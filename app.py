from tkinter import *
from tkinter import messagebox, ttk, filedialog
from PIL import ImageTk, Image
import os
import query_functions
from student import Student
import os

class Menu():

    
    def __init__(self, root):
        self.__root = root
        self.__root.title('Cool School Attendance Application')
        self.__root.geometry("1350x700+0+0")
        self.__root.config(bg="sky blue")

        #open file dialog
        def open():
            root.filename = filedialog.askopenfilename(initialdir="/desktop", title="Select the picture", filetypes=(("jpeg files", "*.jpeg"),("jpg files", "*.jpg")))


        def open_first():
            root.filename = filedialog.askopenfilename(initialdir="/desktop", title="Select the picture", filetypes=(("jpeg files", "*.jpeg"),("jpg files", "*.jpg")))
            picturepath_text.delete(0,END)
            picturepath_text.insert(END, root.filename)


        #Variables
        self.__studentid = StringVar()
        self.__firstname = StringVar()
        self.__lastname = StringVar()
        self.__gender = StringVar()
        self.__picturepath = StringVar()
        self.__present = StringVar()
        self.__absent = StringVar()     

        self.__search_by = StringVar()
        self.__search_text = StringVar()

        #Title of the app
        titlelbl = Label(self.__root, font=("Helvetica", 40, "bold"), bd =3, text = "Cool School Attendance System", relief=GROOVE, bg = "sky blue")
        titlelbl.pack(side=TOP, fill=X)

        #Entry Form for the program

        entry_frame = Frame(self.__root, bd=3, relief=RIDGE, bg="light gray")
        entry_frame.place(x=20, y=100, width=450, height=560)

        entry_title = Label(entry_frame, text="Student Information",bg="light gray", font=("Helvetica", 20, "bold"))
        entry_title.grid(row=0, columnspan=2, pady=20, padx=10, sticky="w")

        studentid_label = Label(entry_frame, text = "Student ID:",bg="light gray", font=("Helvetica", 16, "bold"))
        studentid_label.grid(row=1, column=0, pady=5, padx=20, sticky="w")
        studentid_text = Entry(entry_frame, font=("Helvetica", 16), bd=3, relief=GROOVE, textvariable = self.__studentid)
        studentid_text.grid(row=1, column=1, padx=8, pady=5, sticky = "w",columnspan=2)

        firstname_label = Label(entry_frame, text = "First Name:",bg="light gray", font=("Helvetica", 16, "bold"))
        firstname_label.grid(row=2, column=0, pady=5, padx=20, sticky="w")
        firstname_text = Entry(entry_frame, font=("Helvetica", 16), bd=3, relief=GROOVE, textvariable = self.__firstname)
        firstname_text.grid(row=2, column=1, padx=8, pady=5, sticky = "w",columnspan=2)

        lastname_label = Label(entry_frame, text = "Last Name:",bg="light gray", font=("Helvetica", 16, "bold"))
        lastname_label.grid(row=3, column=0, pady=5, padx=20, sticky="w")
        lastname_text = Entry(entry_frame, font=("Helvetica", 16), bd=3, relief=GROOVE, textvariable = self.__lastname)
        lastname_text.grid(row=3, column=1, padx=8, pady=5, sticky = "w",columnspan=2)

        gender_label = Label(entry_frame, text = "Gender:",bg="light gray", font=("Helvetica", 16, "bold"))
        gender_label.grid(row=4, column=0, pady=5, padx=20, sticky="w")
        gender_combobox = ttk.Combobox(entry_frame, font=("Helvetica", 15), state="readonly", textvariable = self.__gender)
        gender_combobox['values'] = ("Male", "Female", "Others")
        gender_combobox.grid(row=4, column=1, pady=5,columnspan=2)

        picturepath_label = Label(entry_frame, text = "Picture:",bg="light gray", font=("Helvetica", 16, "bold"))
        picturepath_label.grid(row=5, column=0, pady=5, padx=20, sticky="w")
        picturepath_text = Entry(entry_frame, font=("Helvetica", 12), bd=3, relief=GROOVE, textvariable = self.__picturepath)
        picturepath_text.grid(row=5, column=1, padx=8, pady=5, sticky = "w")
        picturepath_button = Button(entry_frame, text="Choose", command=open_first)
        picturepath_button.grid(row=5, column=2, pady=5)

        present_label = Label(entry_frame, text = "Present:",bg="light gray", font=("Helvetica", 16, "bold"))
        present_label.grid(row=6, column=0, pady=5, padx=20, sticky="w")
        present_text = Entry(entry_frame, font=("Helvetica", 16), bd=3, relief=GROOVE, textvariable = self.__present)
        present_text.grid(row=6, column=1, padx=8, pady=5, sticky = "w",columnspan=2)
        

        absent_label = Label(entry_frame, text = "Absent:",bg="light gray", font=("Helvetica", 16, "bold"))
        absent_label.grid(row=7, column=0, pady=5, padx=20, sticky="w")
        absent_text = Entry(entry_frame, font=("Helvetica", 16), bd=3, relief=GROOVE, textvariable = self.__absent)
        absent_text.grid(row=7, column=1, padx=8, pady=5, sticky = "w",columnspan=2)
        
        

        #Button Frame
        button_frame = Frame(entry_frame, bd=0, relief=RIDGE, bg="light gray")
        button_frame.place(x=10, y=500, width=420)

        add_button = Button(button_frame, text="Add", bd=4, width =10, command = self.add_new)
        add_button.grid(row=0, column=0, padx=10)

        update_button = Button(button_frame, text="Update", bd=4, width =10, command = self.update_entry)
        update_button.grid(row=0, column=1, padx=10)

        delete_button = Button(button_frame, text="Delete", bd=4, width =10, command = self.delete_entry)
        delete_button.grid(row=0, column=2, padx=10)

        clear_button = Button(button_frame, text="Clear", bd=4, width =10, command = self.clear_data)
        clear_button.grid(row=0, column=3, padx=10)

        #Database frame
        table_frame = Frame(self.__root, bd=3, relief=RIDGE, bg="light gray")
        table_frame.place(x=500, y=100, width=800, height=560)

        search_by_label = Label(table_frame, text = "Search by:",bg="light gray", font=("Helvetica", 13, "bold"))
        search_by_label.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        search_by_combobox = ttk.Combobox(table_frame, textvariable=self.__search_by, font=("Helvetica", 10), state="readonly", width=10)
        search_by_combobox['values'] = ("studentid", "firstname", "absent")
        search_by_combobox.grid(row=0, column=1, pady=10)

        search_text = Entry(table_frame, font=("Helvetica", 13), textvariable=self.__search_text, bd=3, relief=GROOVE)
        search_text.grid(row=0, column=2, padx=5, pady=10, sticky = "w")

        search_button = Button(table_frame, text="Search", bd=4, width =10, command = self.search)
        search_button.grid(row=0, column=3, padx=10)

        cancel_button = Button(table_frame, text="Cancel", bd=4, width =10, command = self.fetch_data)
        cancel_button.grid(row=0, column=4, padx=10)

        attendance_button = Button(table_frame, text="Attendance", command=open, width=15, bd=4)
        attendance_button.grid(row=0, column=5, padx=10)

        #List frame
        list_frame = Frame(table_frame, bd=4, relief=RIDGE, bg="light gray")
        list_frame.place(x=10, y=70, width=760, height=470)

        scroll_x = Scrollbar(list_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(list_frame, orient=VERTICAL)
        self.__student_table = ttk.Treeview(list_frame, columns=("studentid, firstname, lastname, gender, picture, present, absent"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.__student_table.xview)
        scroll_y.config(command=self.__student_table.yview)
        self.__student_table.heading(0, text="Student ID")
        self.__student_table.heading(1, text="Fisrt Name")
        self.__student_table.heading(2, text="Last Name")
        self.__student_table.heading(3, text="Gender")
        self.__student_table.heading(4, text="Picture")
        self.__student_table.heading(5, text="Present")
        self.__student_table.heading(6, text="Absent")
        self.__student_table["show"] = 'headings'
        self.__student_table.column(0, width=100)
        self.__student_table.column(1, width=150)
        self.__student_table.column(2, width=150)
        self.__student_table.column(3, width=100)
        self.__student_table.column(4, width=200)
        self.__student_table.column(5, width=50)
        self.__student_table.column(6, width=50)
        self.__student_table.pack(fill=BOTH,expand=1)
        self.__student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def clear_data(self):
        self.__studentid.set("")
        self.__firstname.set("")
        self.__lastname.set("")
        self.__gender.set("")
        self.__picturepath.set("")
        self.__present.set("0")
        self.__absent.set("0")

    def add_new(self):
        new_student = Student(self.__studentid.get(), self.__firstname.get(), self.__lastname.get(), self.__gender.get(), self.__picturepath.get(), self.__present.get(), self.__absent.get())
        check = new_student.validate_empty([self.__studentid.get(), self.__firstname.get(), self.__lastname.get(), self.__gender.get(), self.__picturepath.get(), self.__present.get(), self.__absent.get()])
        if check != None:
            messagebox.showerror(title="Error", message=check)
            return
        check = new_student.validate_studentid()
        if check != None:
            messagebox.showerror(title="Error", message=check)
            return
        # check = new_student.validate_name()
        # if check != None:
        #     messagebox.showerror(title="Error", message=check)
        #     return
        check = new_student.validate_number()
        if check != None:
            messagebox.showerror(title="Error", message=check)
            return
        check = new_student.validate_new_number()
        if check != None:
            messagebox.showerror(title="Error", message=check)
            return
        new_student.picture_saving()
        query_functions.add_new_data(new_student.studentid, new_student.firstname, new_student.lastname, new_student.gender, new_student.picturepath, new_student.present, new_student.absent)
        messagebox.showinfo(title="Successfully saved!", message=f"Data of {new_student.get_full_name()} has been successfully saved!")
        self.clear_data()
        self.fetch_data()
        
    def delete_entry(self):
        check = query_functions.check_valid_id(self.__studentid.get())
        if check != None:
            messagebox.showerror(title="Error", message=check)
            return
        else:
            answer = messagebox.askyesno("Deleting data", f"Are you sure you want to delete {self.__studentid.get()}'s data?'")
            if answer == True:
                os.remove(self.__picturepath.get())
                query_functions.delete_data(self.__studentid.get())
                messagebox.showinfo(title="Successfully deleted!", message=f"Data of {self.__studentid.get()} has been successfully deleted!")
                self.clear_data()
                self.fetch_data()
            else:
                return

    def update_entry(self):
        updated_student = Student(self.__studentid.get(), self.__firstname.get(), self.__lastname.get(), self.__gender.get(), self.__picturepath.get(), self.__present.get(), self.__absent.get())
        check = updated_student.validate_empty([self.__studentid.get(), self.__firstname.get(), self.__lastname.get(), self.__gender.get(), self.__picturepath.get(), self.__present.get(), self.__absent.get()])
        if check != None:
            messagebox.showerror(title="Error", message=check)
            return
        check = query_functions.check_valid_id(updated_student.studentid)
        if check != None:
            messagebox.showerror(title="Error", message=check)
            return
        # check = updated_student.validate_name()
        # if check != None:
        #     messagebox.showerror(title="Error", message=check)
        #     return
        check = updated_student.validate_number()
        if check != None:
            messagebox.showerror(title="Error", message=check)
            return
        query_functions.update_data(updated_student.studentid, updated_student.firstname, updated_student.lastname, updated_student.gender, updated_student.picturepath, updated_student.present, updated_student.absent)
        messagebox.showinfo(title="Successfully updated!", message=f"Data of {updated_student.get_full_name()} has been successfully updated!")
        self.clear_data()
        self.fetch_data()
        

    
    def fetch_data(self):
        if len(query_functions.view_all_data()) != 0:
            self.__student_table.delete(*self.__student_table.get_children())
            for row in query_functions.view_all_data():
                self.__student_table.insert("", END, values=row)


    def get_cursor(self,ev):
        cursor_row = self.__student_table.focus()
        contents = self.__student_table.item(cursor_row)
        row = contents['values']
        self.__studentid.set(row[0])
        self.__firstname.set(row[1])
        self.__lastname.set(row[2])
        self.__gender.set(row[3])
        self.__picturepath.set(row[4])
        self.__present.set(row[5])
        self.__absent.set(row[6])

    def search(self):
        if len(query_functions.search_data_by(self.__search_by.get(), self.__search_text.get())) != 0:
            self.__student_table.delete(*self.__student_table.get_children())
            for row in query_functions.search_data_by(self.__search_by.get(), self.__search_text.get()):
                self.__student_table.insert("", END, values=row)



if __name__ =='__main__':
    root = Tk()
    application = Menu(root)
    root.mainloop()