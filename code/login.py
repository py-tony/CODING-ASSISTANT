import tkinter as tk
from validate_email import validate_email
from tkinter import messagebox
from tkinter import ttk
import random
import time
import datetime

title = "CODING ASSISTANT"

register_screen = None
email_entry = None
user_entry = None
pass_entry =None
screen = None
email = None
username = None
password = None
error  = None



def error_button():
    
    error.destroy()


def error_screen(reason, msg):
    
    resp = tk.messagebox.askretrycancel(reason, msg)

    print(resp)
    
    if resp:
        register_screen.destroy()
        screen.destroy()
        main()
    else:
        pass
    
   

   

def check_empty(entry_var) :
     if entry_var.get():
         pass     #your function where you want to jump
     else:
        print(' input required') 

def error_handler(info, msg, reason):


    a = True
    while a:
        if reason == "Username" and len(list(info)) < 2:
            print(len(list(info)), info)            

            a = False
            error_screen(reason, msg)
            
        elif reason == "Email" and validate_email(info, verify=True) == False:
            a = False
            error_screen(reason, msg)
        else:
            break




def register_user():
    
    user_info = username.get()
    email_info = email.get()
    pass_info = password.get()

    

    emaiL_error_msg = "Oooops Invalid email or email address already taken \nPlease try with a valid Email address"
    username_error_msg = "Ooops already taken or invalid Username \nPlease try using a valid Username"
    
    for info,msg,reason in zip([user_info, email_info], [username_error_msg, emaiL_error_msg], ["Username", "Email"]):

        error_handler(info, msg, reason)


    with open("users.txt", "a+") as f:
        
        f.write(user_info+", "+email_info+", "+pass_info+"\n")

    user_entry.delete(0, tk.END)
    email_entry.delete(0,tk.END)
    pass_entry.delete(0, tk.END)
    
    tk.messagebox.showinfo("CODE ASSISTANT", f"Successfully registered {user_info} \nplease check your emails")

    register_screen.destroy()


    

def register(*args):
    global email_entry
    global user_entry
    global pass_entry
    global register_screen
    global email
    global username 
    global password 

    

    register_screen = tk.Toplevel(screen)
    register_screen.title(title)
    register_screen.resizable(False,False)
    register_screen.geometry("320x250")
    screen.protocol("WM_DELETE_WINDOW", _click_cancel)
    screen.bind("<Return>", register)
    
    
    username = tk.StringVar()
    email = tk.StringVar()
    password = tk.StringVar()

    tk.Label(register_screen, text = "Please enter details below", width = 300).pack()
    tk.Label(register_screen, text="").pack()
    tk.Label(register_screen, text="Username").pack()
    tk.Label(register_screen, text="")
    user_entry = tk.Entry(register_screen, textvariable = username, width=35)
    user_entry.pack()

    tk.Label(register_screen, text="Email").pack()
    tk.Label(register_screen, text="")
    email_entry = tk.Entry(register_screen, textvariable = email, width=35)
    email_entry.pack()

    tk.Label(register_screen, text="")
    tk.Label(register_screen, text="Password").pack()
    tk.Label(register_screen, text="")
    pass_entry = tk.Entry(register_screen, width=35, textvariable = password, show="*")
    pass_entry.pack()
    tk.Label(register_screen, text="").pack()
    tk.Button(register_screen, text = "register", command = register_user, width = 10).pack()
    
    


def register_screen():
    print("logging in")

def _click_cancel():
    print("hi there")
    ask = messagebox.askquestion("EXIT CODE ASSISTANT", "Unsaved data maybe lost\nAre you sure you want to exit?")

    if ask:
        try:
        
            screen.destroy()
        except:
            pass
        try:
            
            register_screen.destroy()
        except:
            pass

        exit()
    else:
        return screen


def next_widget(event):
    event.Button.tk_focusNext().focus()
    return "break"


def main():
    global screen
    screen = tk.Tk()
    screen.geometry("350x280")
    screen.resizable(False, False)
    screen.title(" CODE ASSISTANT")
    screen.protocol("WM_DELETE_WINDOW", _click_cancel)

    bg_img = tk.PhotoImage(file="bg.png")
    screen.configure(background=bg_img,  pady=2)
    screen.bind("<Return>", register)
    screen.bind_class("Up", "<Down>", next_widget)



    tk.Label(text = "CODE ASSISTANT Version 0.1", width=100, height= 2, bg =  "grey", font = ("Calibri", 14)).pack()
    tk.Label(text = "", bg="black").pack()

    login_btn = tk.Button(text = "Login", width = 30, height= 2)
    login_btn.pack()
    login_btn.focus()

    tk.Label(text = "", bg="black").pack()

    reg_btn = tk.Button(text = "Register", command = register, width = 30, height= 2)
    reg_btn.pack()

    screen.mainloop()

main()


