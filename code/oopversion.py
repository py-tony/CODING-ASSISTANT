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

        # self.user_label = Label(self.background, text="Username", pady=20)
        # self.user_label.grid(row=0, column=0, sticky=W)


        self.frame1 = Frame(self.master, bg="black", bd=10)
        self.frame1.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

        
        self.user_input = Entry(self.frame1, bg="white", font=40)
        self.user_input.place( relwidth=0.45, relheight=1)
        self.user_input.insert(0, 'username')

        self.pass_input = Entry(self.frame1, bg="white", font=40)
        self.pass_input.place(relx = 0.55, rely=0,relwidth=0.45, relheight=1)
        self.pass_input.insert(0, '***********')

# B = tk.Button(frame1, text ="Submit", font=40, command = lambda: helloCallBack(entry.get()) )
# B.place(relx = 0.7, rely=0, relwidth=0.3, relheight=1)

        self.frame2 = Frame(self.master, bg="black", bd=10)
        self.frame2.place(relx=0.5, rely=0.2, relwidth=0.9, relheight=0.1, anchor='n')


        self.btnlogin = Button(self.frame2, text="login")
        self.btnlogin.place(relwidth=0.7, relheight=1)

        self.btnreg = Button(self.frame2, text="register")
        self.btnreg.place(relx=0.75, rely=0.1, relwidth=0.25, relheight=1)



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