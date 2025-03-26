from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
 
root = Tk()
root.geometry("500x300")
root.title("MySQL CRUD Operations")

id = Label(root, text="Enter ID:", font=("verdana 15"))
id.place(x=50, y=30)
id_entry = Entry(root, font=("verdana 15"))
id_entry.place(x=150, y=30)
  
name = Label(root, text="Nombre:", font=("verdana 15"))
name.place(x=50, y=80)
name_entry = Entry(root, font=("verdana 15"))
name_entry.place(x=150, y=80)
  
email = Label(root, text="correo", font=("verdana 15"))
email.place(x=50, y=130)
email_entry= Entry(root, font=("verdana 15"))
email_entry.place(x=180, y=130)

carrera = Label(root, text="carrera", font=("verdana 15"))
carrera.place(x=50, y=150)
carrera_entry= Entry(root, font=("verdana 15"))
carrera_entry.place(x=150, y=130)


grupo = Label(root, text="grupo", font=("verdana 15"))
grupo.place(x=50, y=130)
grupo_entry= Entry(root, font=("verdana 15"))
grupo_entry.place(x=150, y=130)

  

  
def Insert():

   id = id_entry.get() 
   name = name_entry.get()
   email = email_entry.get()
   carrera=carrera_entry.get()
   grupo=grupo_entry.get()

  
   if(id == "" or name == "" or email == ""or carrera =="" or grupo==""):
       MessageBox.showinfo("ALERT", "Porfavor inserta  datos  completos")
   else:
       con = mysql.connect(host="localhost", user="root", password="", database="Your Database Name")
       cursor = con.cursor()
       cursor.execute("insert into TablaName values('" + id +"', '"+ name +"', '" +  +"' )")
       cursor.execute("commit")
  
       MessageBox.showinfo("Status", "Successfully Inserted")
       con.close();



def Update():
   id = id_entry.get()
   name = name_entry.get()
   phone = phone_entry.get()
  
   if(name == "" or phone == ""):
       MessageBox.showinfo("ALERT", "Please enter fiels you want to update!")
   else:
       con = mysql.connect(host="localhost", user="Database Username", password="Your Database Password", database="Your Database Name")
       cursor = con.cursor()
       cursor.execute("update Person set name = '"+ name +"', phone='"+ phone +"' where id ='"+ id +"'")
       cursor.execute("commit");
  
       MessageBox.showinfo("Status", "Successfully Updated")
       con.close();





  
btnInsert = Button(root, text="Insert", command = Insert,   font=("verdana 15")).place(x=100, y=190)
btnDelete = Button(root, text="Delete",  font=("verdana 15")).place(x=200, y=190)
btnUpdate = Button(root, text="Update",  font=("verdana 15")).place(x=320, y=190)
btnSelect= Button(root, text="Select",  font=("verdana 15")).place(x=200, y=240)
  
root.mainloop()