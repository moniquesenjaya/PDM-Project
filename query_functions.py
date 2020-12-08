import sqlite3

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

conn = sqlite3.connect("Cool_School.db")
c = conn.cursor()
c.execute("SELECT * from students")
id_list = c.fetchall()
print(id_list)
conn.commit()
conn.close()