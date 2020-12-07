import sqlite3

def add_new_data(studentid, firstname, lastname, gender, picturepath, present, absent):
    conn = sqlite3.connect("Cool_School.db")
    c = conn.cursor()
    c.execute("INSERT INTO students (studentid, firstname, lastname, gender, picturepath, present, absent) VALUES (?, ?,?,?,?,?,?)", (studentid, firstname, lastname, gender, picturepath, present, absent))
    conn.commit()
    conn.close()

conn = sqlite3.connect("Cool_School.db")
c = conn.cursor()
c.execute("SELECT * from students")
id_list = c.fetchall()
print(id_list)
conn.commit()
conn.close()