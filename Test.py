import sqlite3

def createtable():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(id INTEGER , name TEXT , date TEXT , amount REAL)")
    conn.commit()
    conn.close()

def check_table():
    try:
        conn = sqlite3.connect("lite.db")
        cur=conn.cursor()
        print("Database Connection and creation is successfully created")
        cur.close()

    except sqlite3.Error as error:
        print("Error in creating Database")
    finally:
        if(conn):
            conn.close()
            print("Sqlite connection is closed")

def insert(id,name,date,amount):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUES(?,?,?,?)",(id,name,date,amount))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,amount,date,Email):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE data SET amount=? , date=? , Email=? WHERE id=?",(amount,date,Email,id))
    conn.commit()
    conn.close()

def add_column():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("ALTER TABLE data ADD Email VARCHAR(100);")
    conn.commit()
    conn.close()

#sqlite does not support DROP COLUMN in ALTER TABLE. You can only rename tables and add columns.
#If you need to remove columns, create a new table, copy the data there, drop the old table and rename the table to its intented name.

def remove_col():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("ALTER TABLE data DROP Email;")
    conn.commit()
    conn.close()

def rename_table():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("ALTER TABLE new_name RENAME TO data;")
    conn.commit()
    conn.close()
