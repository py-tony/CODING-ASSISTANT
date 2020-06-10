from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime


    

class login:
    def __init__(self, master):
        self.master = master
        self.master.title("CODE ASSISTANT LOGIN")
        self.master.geometry('400x400')
        self.bg_img = PhotoImage(file="bg.png")
        self.background = Label(self.master, image=self.bg_img)
        self.background.place(relheight=1, relwidth=1) 

        



        self.frame1 = Frame(self.master, bg="black")
        self.frame1.pack(padx=20, pady=15, anchor='w')
        
        Label(self.frame1, text="Username: ").grid(row=0, column=0, sticky='w')
        
        self.user_input = Entry(self.frame1, bg="white", width=24)
        self.user_input.grid( row=0, column=1, sticky='w')
        self.user_input.focus_set()


        Label(self.frame1, text="Password: ").grid(row=1, column=0, sticky='w')
        
        self.pass_input = Entry(self.frame1, bg="white", width=24, show="*")
        self.pass_input.grid(row=1, column=1)
        

# B = tk.Button(frame1, text ="Submit", font=40, command = lambda: helloCallBack(entry.get()) )
# B.place(relx = 0.7, rely=0, relwidth=0.3, relheight=1)

        

        # self.btnlogin = Button(self.frame2, text="login")
        # self.btnlogin.place(relwidth=0.7, relheight=1)

        # self.btnreg = Button(self.frame2, text="register")
        # self.btnreg.place(relx=0.75, rely=0.1, relwidth=0.25, relheight=1)



    def registration(self):
        pass

    def  admin(self):
        pass     

    def  student(self):
        pass

    def  hypestudent(self):
        pass

root = Tk()
app = login(root)
root.mainloop()