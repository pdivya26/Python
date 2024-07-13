from tkinter import *
import tkinter.messagebox
import random
import mysql.connector

c = mysql.connector.connect(host="localhost", database="Python", user="root", password="root")
cursor = c.cursor()

gselvar = None
nmtb = None
emtb = None
untb = None
pstb = None
pntb = None
usidtb = None

def submit():
    global nmtb, emtb, untb, pstb, pntb, gselvar, uid, root1
    
    n = nmtb.get()
    e = emtb.get()
    un = untb.get()
    ps = pstb.get()
    pn = pntb.get()
    if gselvar.get() == 1:
        g = "Male"
    else:
        g = "Female"

    if not pn.isdigit() or n.isdigit():
        tkinter.messagebox.showerror("Error", "Enter valid inputs!")

    try:
        ins = "insert into UserData(UserID, Name, Gender, Email, Username, Password, Phone)values(%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(ins,(uid, n, g, e, un, ps, pn))
        
        c.commit()
        c.close()
        
        nmtb.delete(0, END)
        emtb.delete(0, END)
        untb.delete(0, END)
        pstb.delete(0, END)
        pntb.delete(0, END)

        tkinter.messagebox.showinfo("Registration","Registration Successfull!")

    except Exception as e:
        print(e)
        tkinter.messagebox.showerror("Error", "Failed to Register User.")

    root1.destroy()

def delete():
    global usidtb, root2
    usid = str(usidtb.get())
    
    dlt = "delete from UserData where UserID = %s"

    try:
        cursor.execute(dlt,(usid,))
    
        usidtb.delete(0, END)
        tkinter.messagebox.showinfo("Deleting Existing Data","Records Deleted Successfull!")

        c.commit()
        
    except Exception as e:
        print(e)
        tkinter.messagebox.showerror("Error", "Failed to Delete Records.")

def modify():
    global ntb, etb, utb, pwtb, ptb, gselvar, usidtb, root3
    usid = usidtb.get()
    n = ntb.get()
    e = etb.get()
    un = utb.get()
    ps = pwtb.get()
    pn = ptb.get()
    if gselvar.get() == 1:
        g = "Male"
    else:
        g = "Female"

    try:
        upd = "update UserData set Name = %s, Gender = %s, Email = %s, Username = %s, Password = %s, Phone = %s where UserID = %s"
        cursor.execute(upd, (n, g, e, un, ps, pn, usid))
        
        ntb.delete(0, END)
        etb.delete(0, END)
        utb.delete(0, END)
        pwtb.delete(0, END)
        ptb.delete(0, END)
        tkinter.messagebox.showinfo("Modify Existing Records","Records Updated Successfully!")

        c.commit()
    except Exception as e:
        print(e)
        tkinter.messagebox.showerror("Error", "Failed to Update Records.")

def insert_data():
    global nmtb, emtb, untb, pstb, pntb, gselvar, uid, root1

    root1 = Tk()
    root1.title("New Registration")
    root1.geometry("450x350")

    f1 = Frame(root1, height = 350, width = 450)
    f1.propagate(0)
    f1.pack()

    label=Label(f1, text = "Registration Form", font = 'arial 20 bold')
    label.pack()

    uid = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=5))
    
    uidl = Label(f1, text = "User-ID :", font = "Arial 12")
    uidd = Label(f1, text = uid, font = "Arial 12")
    uidl.place(x = 280, y = 40)
    uidd.place(x = 350,y = 40)

    nml = Label(f1, text = "Name", font = "Arial 12")
    nml.place(x = 10, y = 85)
    nmtb = tkinter.Entry(f1, width = 35)
    nmtb.place(x = 120, y = 85)

    gselvar = IntVar()
    gl = Label(f1, text = "Gender", font = "Arial 12")
    gl.place(x = 10, y = 115)
    rm=Radiobutton(f1, font = ("arial",12), text = "Male",variable = gselvar, value = 1)
    rf=Radiobutton(f1, font = ("arial",12), text = "Female",variable = gselvar, value = 2)
    rm.place(x = 115, y = 113)
    rf.place(x = 260, y = 113)

    eml = Label(f1, text = "Email", font = "Arial 12")
    eml.place(x = 10, y = 145)
    emtb = tkinter.Entry(f1, width = 35)
    emtb.place(x = 120, y = 145)

    unl = Label(f1, text = "Username", font = "Arial 12")
    unl.place(x = 10, y = 175)
    untb = tkinter.Entry(f1, width = 35)
    untb.place(x = 120, y = 175)

    psl = Label(f1, text = "Password", font = "Arial 12")
    psl.place(x = 10, y = 205)
    pstb = tkinter.Entry(f1, width = 35, show = "*")
    pstb.place(x = 120, y = 205)

    pnl = Label(f1, text = "Phone No.",font = "Arial 12")
    pnl.place(x = 10, y = 235)
    pntb = tkinter.Entry(f1, width = 35)
    pntb.place(x = 120, y = 235)

    subbt = Button(f1, text = "Submit", font = 'arial 10 bold', width = 20, height = 1, bg = "white", command = submit)
    subbt.place(x = 150, y = 280)

    root1.resizable(False, False)
    root1.mainloop()

def delete_data():
    global usidtb, root2
    
    root2 = Tk()
    root2.title("Delete Existing Data")
    root2.geometry("300x200")

    f2 = Frame(root2, height = 200, width = 300)
    f2.propagate(0)
    f2.pack()

    label=Label(f2, text = "Delete Existing Records", font = 'arial 18 bold')
    label.pack()

    usid = Label(f2, text = "Enter your User-ID here ", font = "Arial 12 bold")
    usid.place(x = 38, y = 65)
    usidtb = tkinter.Entry(f2, width = 35)
    usidtb.place(x = 40, y = 95)

    subbt = Button(f2, text = "Delete", font = 'arial 10 bold', width = 0, height = 1, bg = "white", command = delete)
    subbt.place(x = 120, y = 140)
    
    root2.resizable(False, False)
    root2.mainloop()

def modify_data():
    global ntb, etb, utb, pwtb, ptb, gselvar, usidtb, root3

    root3 = Tk()
    root3.title("Modify Existing Records")
    root3.geometry("450x350")

    f3 = Frame(root3, height = 300, width = 450)
    f3.propagate(0)
    f3.pack()
    
    label=Label(f3, text = "Modify Existing Records", font = 'arial 20 bold')
    label.pack()
    
    usidl = Label(f3, text = "User-ID :", font = "Arial 12")
    usidl.place(x = 250, y = 40)
    usidtb = tkinter.Entry(f3)
    usidtb.place(x = 320,y = 40)

    nl = Label(f3, text = "Name", font = "Arial 12")
    nl.place(x = 10, y = 85)
    ntb = tkinter.Entry(f3, width = 35)
    ntb.place(x = 120, y = 85)

    gselvar = IntVar()
    gl = Label(f3, text = "Gender", font = "Arial 12")
    gl.place(x = 10, y = 115)
    rm=Radiobutton(f3, font = ("arial",12), text = "Male",variable = gselvar, value = 1)
    rf=Radiobutton(f3, font = ("arial",12), text = "Female",variable = gselvar, value = 2)
    rm.place(x = 115, y = 113)
    rf.place(x = 260, y = 113)

    el = Label(f3, text = "Email", font = "Arial 12")
    el.place(x = 10, y = 145)
    etb = tkinter.Entry(f3, width = 35)
    etb.place(x = 120, y = 145)

    ul = Label(f3, text = "Username", font = "Arial 12")
    ul.place(x = 10, y = 175)
    utb = tkinter.Entry(f3, width = 35)
    utb.place(x = 120, y = 175)

    pwl = Label(f3, text = "Password", font = "Arial 12")
    pwl.place(x = 10, y = 205)
    pwtb = tkinter.Entry(f3, width = 35, show = "*")
    pwtb.place(x = 120, y = 205)

    pl = Label(f3, text = "Phone No.",font = "Arial 12")
    pl.place(x = 10, y = 235)
    ptb = tkinter.Entry(f3, width = 35)
    ptb.place(x = 120, y = 235)

    subbt = Button(f3, text = "Modify", font = 'arial 10 bold', width = 20, height = 1, bg = "white", command = modify)
    subbt.place(x = 150, y = 280)
    
    root3.resizable(False, False)
    root3.mainloop()

def exit():
    root.destroy()

root = Tk()
root.title("Registration Form")
root.geometry("300x300")

f = Frame(root, height = 300, width = 300)
f.propagate(0)
f.pack()

label=Label(f, text = "What action do you want\nto perform ?", font = 'arial 15 bold')
label.pack()

insbt = Button(text = "New Registration", font = 'arial 10 bold', width = 20, height = 1, bg = "white", command = insert_data)
insbt.place(x = 65, y = 70)

modbt = Button(text = "Modify Existing Records", font = 'arial 10 bold', width = 20, height = 1, bg = "white", command = modify_data)
modbt.place(x = 65, y = 130)

delbt = Button(text = "Delete Existing Records", font = 'arial 10 bold', width = 20, height = 1, bg = "white", command = delete_data)
delbt.place(x = 65, y = 190)

delbt = Button(text = "Exit", font = 'arial 10 bold', width = 20, height = 1, bg = "white", command = exit)
delbt.place(x = 65, y = 250)

root.resizable(False, False)
root.mainloop()