import sqlite3
import face_recognition

def add_new_data(studentid, firstname, lastname, gender, picturepath, present, absent):
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("INSERT INTO students (studentid, firstname, lastname, gender, picturepath, present, absent) VALUES (?, ?,?,?,?,?,?)", (studentid, firstname, lastname, gender, picturepath, present, absent))
    conn.commit()
    conn.close()

def delete_data(studentid):
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("DELETE FROM students where studentid=?", (studentid,))
    conn.commit()
    conn.close()
    

def check_valid_id(studentid):
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("SELECT studentid FROM students")
    id_list = []
    for item in c.fetchall():
        id_list.append(item[0])
    if studentid == "" or studentid not in id_list:
        return "Please enter a valid ID."
    conn.close()

def view_all_data():
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("SELECT * from students ORDER BY studentid")
    rows = c.fetchall()
    conn.close()
    return rows

def search_data(studentid = "", firstname = "", absent = ""):
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("SELECT * from students WHERE studentid=? OR firstname=? OR absent=? ORDER BY studentid", (studentid, firstname, absent))
    rows = c.fetchall()
    conn.close()
    return rows

def update_data(studentid, firstname, lastname, gender, picturepath, present, absent):
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("UPDATE students set firstname=?, lastname=?, gender=?, picturepath=?, present=?, absent=? WHERE studentid=?", (firstname, lastname, gender, picturepath, present, absent, studentid))
    conn.commit()
    conn.close()

def search_data_by(searchby, searchtxt):
    print(searchtxt)
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("SELECT * from students WHERE " + str(searchby) + " LIKE '%" + str(searchtxt) + "%' ORDER BY studentid")
    rows = c.fetchall()
    print(rows)
    conn.close()
    return rows

def add_attendance(filename):
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    picturepath_list = []
    id_list = []
    final_id_present = []
    final_id_absent =[]
    final_list = []
    check = 0
    all_data = c.fetchall()
    for item in all_data:
        file_directory = item[4]
        id_list.append(item[0])
        print(file_directory)
        # print(file_directory)
        picturepath_list.append(face_recognition.face_encodings(face_recognition.load_image_file(file_directory))[0])


    test_image = face_recognition.load_image_file(filename)

    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)

    for group_encoding in face_encodings:
        matches = face_recognition.compare_faces(picturepath_list, group_encoding)  
        ids = "Unknown Person"  

        if True in matches:
            first_match_index = matches.index(True)
            ids = id_list[first_match_index]
            
        final_list.append(ids) 
    for id_all in id_list:
        if id_all in final_list:
            current_present = int(all_data[id_list.index(id_all)][5]) +1
            c.execute("UPDATE students set present=? WHERE studentid=?", (str(current_present), id_all))
            conn.commit()
            final_id_present.append(id_all)
        else:
            current_absent = int(all_data[id_list.index(id_all)][6]) +1
            c.execute("UPDATE students set absent=? WHERE studentid=?", (str(current_absent), id_all))
            conn.commit()
            final_id_absent.append(id_all)
    conn.close()
    for unknown_check in final_list:
        if unknown_check == "Unknown Person":
            check += 1
    return f"There are {check} students in the picture that were not detected. The students present are {final_id_present}. The students absent are {final_id_absent}."

