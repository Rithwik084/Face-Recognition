import mysql.connector
import os

def View():
    con = mysql.connector.connect(host="localhost", user="root", passwd="Admin")
    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS Images")
    cur.execute("USE Images")
    cur.execute("CREATE TABLE IF NOT EXISTS Imgs(ImageName VARCHAR(40))")
    cur.execute("SELECT * FROM Imgs")
    data = cur.fetchall()
    for i in data:
        print(i)

def Delete(Name):
    con = mysql.connector.connect(host="localhost", user="root", passwd="Admin")
    cur = con.cursor()
    sql = "DELETE FROM Imgs WHERE ImageName='%s'"%(Name)
    cur.execute("CREATE DATABASE IF NOT EXISTS Images")
    cur.execute("USE Images")
    cur.execute("CREATE TABLE IF NOT EXISTS Imgs(ImageName VARCHAR(40))")
    cur.execute(sql)
    con.commit()

while True:
    print("1. View the records")
    print("2. Delete a record")
    print("3. Exit")
    choice = int(input("ENTER YOUR CHOICE(the respective number) : "))
    if choice == 1:
        View()
    elif choice == 2:
        name = input("ENTER THE RECORD NAME: ")
        if os.path.exists("images" + "\\" + name + ".jpg"):
            os.remove("images" + "\\" + name + ".jpg")
            Delete(name)
            print("Deleted the record " + name)
        else:
            print("There is no record that matches your entry. Please try again!")
    
            
    elif choice == 3:
        os.system("TASKKILL /F /IM python.exe")
        break
    else:
        print("There is no choice that matches your entry. Please try again!")
    
