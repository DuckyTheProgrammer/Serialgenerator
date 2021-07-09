#imports
from sqlite3.dbapi2 import Cursor
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import sqlite3

# vars
conn = sqlite3.connect('serialdata.db')
c = conn.cursor()
randnum = random.randint(101,999)


govermentjobs = ['MP', 'PD', 'OC', 'HS','GP']
citylist = ['TB', 'KU', 'BA', 'KH', 'RU']


# functions

def warningmsg(wtitle, werror):
    messagebox.showwarning(wtitle, werror)

def checkingtable():
    '''
    c.execute("CREATE TABLE tables(existen text)")
    conn.commit()
    c.execute("""
    INSERT INTO tables VALUES("")
    """)
    conn.commit()
    '''

    c.execute("""
    SELECT * FROM tables
    """)
    
    tabledatas = c.fetchone()
    print(tabledatas)

    if tabledatas[0] == "serialdatas":
        print('True')

    else:
        c.execute("""
        DELETE FROM tables WHERE rowid=1
        """)
        conn.commit()
        c.execute("""
        INSERT INTO tables VALUES("serialdatas")
        """)
        conn.commit()

        c.execute("""CREATE TABLE serialdatas(
        govermentjob text,
        city text,
        privatenum integer,
        name text,
        lastname text
        )""")
        conn.commit()
        c.execute("SELECT * FROM tables")

        print('Creating table in database')
        print(c.fetchall())



    
    
def newreg():
    regroot = tk.Tk()
    canvas = tk.Canvas(regroot, bg="#263D42", width=650, height=500)
    canvas.pack()

    cframe = tk.Frame(regroot, bg='white')
    cframe.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    # ----- ----- ------ Texts ----- ----- ------ #

    goventlbl = tk.Label(cframe, text="სახელმწიფო დაწესებულება: ")
    goventlbl.place(relx=0.07, rely=0.11)  
    goventlbl.config(font=("Courier", 15))

    cityentlbl = tk.Label(cframe, text="ქალაქი: ")
    cityentlbl.place(relx=0.36, rely=0.21)  
    cityentlbl.config(font=("Courier", 15))

    pnventlbl = tk.Label(cframe, text="პირადი ნომერი: ")
    pnventlbl.place(relx=0.24, rely=0.31)
    pnventlbl.config(font=("Courier", 15))

    nameentlbl = tk.Label(cframe, text="სახელი: ")
    nameentlbl.place(relx=0.36, rely=0.41)
    nameentlbl.config(font=("Courier", 15))

    lnameentlbl = tk.Label(cframe, text="გვარი: ")
    lnameentlbl.place(relx=0.38, rely=0.51)
    lnameentlbl.config(font=("Courier", 15))

    # ----- ----- ------ ENTRIES ----- ----- ------ #

    govent = tk.Entry(cframe)
    govent.place(relwidth=0.43, relx=0.5, rely=0.1)
    
    cityent = tk.Entry(cframe)
    cityent.place(relwidth=0.43, relx=0.5, rely=0.2)

    pnvent = tk.Entry(cframe)
    pnvent.place(relwidth=0.43, relx=0.5, rely=0.3)

    nameent = tk.Entry(cframe)
    nameent.place(relwidth=0.43, relx=0.5, rely=0.4)

    lnameent = tk.Entry(cframe)
    lnameent.place(relwidth=0.43, relx=0.5, rely=0.5)
    

    def insertdata():

        #getting datas from inputs

        govdata = govent.get().upper()
        citydata = cityent.get().upper()
        privatenumdata = pnvent.get()
        namedata = nameent.get()
        lnamedata = lnameent.get()

        #checking if input fields was empty

        if len(govdata) < 1:
            warningmsg("Empty fields", "Empty fields")
        else: pass

        if len(citydata) < 1:
            warningmsg("Empty fields", "Empty fields")
        else: pass

        if len(privatenumdata) < 1:
            warningmsg("Empty fields", "Empty fields")
        else: pass

        if len(namedata) < 1:
            warningmsg("Empty fields", "Empty fields")
        else: pass

        if len(lnamedata) < 1:
            warningmsg("Empty fields", "Empty fields")
        else: pass

        #clearing input fields

        datains = [govdata, citydata, privatenumdata, namedata, lnamedata]
        c.executemany('INSERT INTO serialdatas VALUES (?,?,?,?,?)', [datains])
        c.execute("SELECT * FROM serialdatas")
        conn.commit()
        print("Successfully entered your data")
        fa = c.fetchall()
        for t in fa:
            print(t)
        print("Generating serial number")
        

        #Checking gov job

        if govdata == govermentjobs[0]:
            print("Got goverment job " + govermentjobs[0])
            suffix = govermentjobs[0]
        else:
            pass
        if govdata == govermentjobs[1]:
            print("Got goverment job " + govermentjobs[1])
            suffix = govermentjobs[1]
        else:
            pass
        if govdata == govermentjobs[2]:
            print("Got goverment job " + govermentjobs[2])
            suffix = govermentjobs[2]
        else:
            pass
        if govdata == govermentjobs[3]:
            print("Got goverment job " + govermentjobs[3])
            suffix = govermentjobs[3]
        else:
            pass
        if govdata == govermentjobs[4]:
            print("Got goverment job " + govermentjobs[4])
            suffix = govermentjobs[4]
        else:
            pass

        #Cheking city

        if citydata[0:2] == citylist[0][0:2]:
            serialnumb = citylist[0] + "-" + str(randnum) + "-" + suffix
            print(serialnumb)
        else: pass

        if citydata[0:2] == citylist[1][0:2]:
            serialnumb = citylist[1] + "-" + str(randnum) + "-" + suffix
            print(serialnumb)
        else: pass

        if citydata[0:2] == citylist[2][0:2]:
            serialnumb = citylist[2] + "-" + str(randnum) + "-" + suffix
            print(serialnumb)
        else: pass

        if citydata[0:2] == citylist[3][0:2]:
            serialnumb = citylist[3] + "-" + str(randnum) + "-" + suffix
            print(serialnumb)
        else: pass

        if citydata[0:2] == citylist[4][0:2]:
            serialnumb = citylist[4] + "-" + str(randnum) + "-" + suffix
            print(serialnumb)
        else: pass
        
        #generating result serial number
 
        numberlbl = tk.Label(cframe, text=serialnumb)
        numberlbl.place(relx=0.36, rely=0.7)
        numberlbl.config(font=("Courier", 20))

        #clearing input fields

        govent.delete(0, END)
        cityent.delete(0, END)
        pnvent.delete(0, END)
        nameent.delete(0, END)
        lnameent.delete(0, END)
        

    insertbtn = tk.Button(cframe, text="ENTER", command=insertdata)
    insertbtn.place(relwidth=0.3, relx=0.56, rely=0.6)

    regroot.mainloop()