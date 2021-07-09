import tkinter as tk
from tkinter import *
import random
import sqlite3

#importing functions

from functions import newreg, checkingtable


checkingtable()

#dbcreate()


#GUI

mainpage = tk.Tk()
mainpage.title('Serial APP')

canvas = tk.Canvas(mainpage, width=400, height=500, bg="#56a6a2")
canvas.pack()

frame = tk.Frame(mainpage, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

title = tk.Label(frame, text="Navigation Button", fg="black")
title.place(relx=0.15, rely=0.09)
title.config(font=("Courier", 22))

#nav buttons

navbtnreg = tk.Button(frame, text="ახალი ნომრის რეგისტრაცია",command=newreg)
navbtnreg.place(relwidth=0.6,relheight=0.06, relx=0.2, rely=0.2)

navbtnreg = tk.Button(frame, text="ნომრის მიხედვით ძებნა")
navbtnreg.place(relwidth=0.6,relheight=0.06, relx=0.2, rely=0.29)

navbtnreg = tk.Button(frame, text="სახელი და გვარის მიხედვით ძიება")
navbtnreg.place(relwidth=0.75,relheight=0.06, relx=0.12, rely=0.38)

navbtnreg = tk.Button(frame, text="ნომრების ნახვა")
navbtnreg.place(relwidth=0.6,relheight=0.06, relx=0.2, rely=0.47)

navbtnreg = tk.Button(frame, text="ნომრის გადაფორმება")
navbtnreg.place(relwidth=0.6,relheight=0.06, relx=0.2, rely=0.56)

mainpage.mainloop()