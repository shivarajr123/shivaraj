import sqlite3
#backend

def StudentData():
    con=sqlite3.connect("student.db")
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text, Firstname text, Surname text, DoB text,Age text,Gender text,Address text,Mobile text)")
    con.commet()
    con.close()

def addStdRec(StdID , Firstname, Surname,DoB,Age,Gender ,Address, Mobile):
    con=sqlite3.connect("student.db")
    cur = con.cursor(*)
    cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?,?)",StdID , Firstname, Surname,DoB,Age,Gender ,Address, Mobile)
    con.commet()
    con.close()

def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor(*)
    cur.execute("SELECT * FROM student ")
    rows = cur.fetchall()
    con.close()
    return rows

def DeleteRec():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=? ", (id,))
    con.commet()
    con.close()

def searchData(StdID"", Firstname="", Surname="",DoB="",Age="",Gender="" ,Address="", Mobile=""):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=?",StdID , Firstname, Surname,DoB,Age,Gender ,Address, Mobile)
    rows= cur.fetchall()
    con.close()
    return rows

def dataUpdate(StdID"", Firstname="", Surname="",DoB="",Age="",Gender="" ,Address="", Mobile=""):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("UPDATE student set  StdID=?, Firstname=?, Surname=?,DoB=?, Age=?, Gender=?,Address=?, Mobile=?,WHERE id=?",StdID , Firstname, Surname,DoB,Age,Gender ,Address, Mobile,id)
    con.commet()
    con.close()

