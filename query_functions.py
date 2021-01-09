import sqlite3
import face_recognition

# Adding data to the database after validation
def add_new_data(studentid, firstname, lastname, gender, picturepath, present, absent):
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("INSERT INTO students (studentid, firstname, lastname, gender, picturepath, present, absent) VALUES (?, ?,?,?,?,?,?)", (studentid, firstname, lastname, gender, picturepath, present, absent))
    conn.commit()
    conn.close()

# Deleting data in the database
def delete_data(studentid):
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("DELETE FROM students where studentid=?", (studentid,))
    conn.commit()
    conn.close()
    
# Checking if the id exist (for searching)
def check_valid_id(studentid):
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("SELECT studentid FROM students")
    id_list = []
    # Fetching all data that is in the database with that id
    for item in c.fetchall():
        id_list.append(item[0])
    if studentid == "" or studentid not in id_list:
        return "Please enter a valid ID."
    conn.close()

# Function to view all the data in the database without filter (used after search button is clicked)
def view_all_data():
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("SELECT * from students ORDER BY studentid")
    rows = c.fetchall()
    conn.close()
    return rows

# Updating data in the database after validation
def update_data(studentid, firstname, lastname, gender, picturepath, present, absent):
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("UPDATE students set firstname=?, lastname=?, gender=?, picturepath=?, present=?, absent=? WHERE studentid=?", (firstname, lastname, gender, picturepath, present, absent, studentid))
    conn.commit()
    conn.close()

# Searching function that uses category filtering
def search_data_by(searchby, searchtxt):
    print(searchtxt)
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("SELECT * from students WHERE " + str(searchby) + " LIKE '%" + str(searchtxt) + "%' ORDER BY studentid")
    rows = c.fetchall()
    conn.close()
    return rows

# Attendance function that implements the face_recognition library
def add_attendance(filename):
    # Create connection
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students")

    # Declaring the variables needed
    picturepath_list = []
    id_list = []
    final_id_present = []
    final_id_absent =[]
    final_list = []
    check = 0

    # Fetch all the data from the database
    all_data = c.fetchall()

    # Reading all the picture path in the database and storing in a list
    for item in all_data:
        file_directory = item[4]
        id_list.append(item[0])
        picturepath_list.append(face_recognition.face_encodings(face_recognition.load_image_file(file_directory))[0])

    # Loading the image uploaded to the system
    test_image = face_recognition.load_image_file(filename)

    # Using the functions in face_recognition to find the locations and encoding of the faces
    face_locations = face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image, face_locations)

    # Check every face detected if it matches the faces in the picture path lists
    for group_encoding in face_encodings:
        matches = face_recognition.compare_faces(picturepath_list, group_encoding)  
        ids = "Unknown Person"  

        # If it does, the first index is stored in the final_list
        if True in matches:
            first_match_index = matches.index(True)
            ids = id_list[first_match_index]
            
        final_list.append(ids) 

    # Loop to check the difference in all the ids to see who is present and absent
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

    # Loop to check how many people are undetected to try to fix errors
    for unknown_check in final_list:
        if unknown_check == "Unknown Person":
            check += 1
    return f"There are {check} students in the picture that were not detected. The students present are {final_id_present}. The students absent are {final_id_absent}."

