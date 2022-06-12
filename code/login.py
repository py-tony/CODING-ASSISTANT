#this is the necessary files and modules that we will use this file 

import tkinter as tk
from urllib.request import urlopen
from validate_email import validate_email
from tkinter import messagebox
from tkinter import ttk
import random
import time
import datetime
import yagmail
#local classes==============
from db import Database as db
import codeAssistant as ca

title = "CODING ASSISTANT"

screen = None
login_screen = None
register_screen = None

email_entry = None
user_entry = None
pass_entry = None
screen = None
email = None
username = None
password = None
error  = None
user_info = None
pass_info = None
email_info = None




def confirmation_email(receiver):

    sender = "codeassistantconfirm@gmail.com"      
    receiver = "tony@oceansofty.com"
    password = "0990525794"
    

    msg = f"""
    Subject: CODE ASSISTANT CONFIRMATION EMAIL

    Username: {user_info}
    Password: {pass_info}
    Email: {email_info}
    
    Please click the link below to confirm your email
    https://py-tony.netlify.app/emailConfirm/




    If you do not recognize this please report at
    https://py-tony.netlify.app/repportSpam/


    """

    print("sending")
    try:
        
        
        yag = yagmail.SMTP(sender, password)
        yag.send(receiver, "CODE ASSISTANT CONFIRMATION", msg)
        print("success")
    except Exception as e:
        print(e)



def error_button():
    
    error.destroy()


def error_screen(reason, msg):
    
    resp = tk.messagebox.askretrycancel(reason, msg)

    if resp:
        register_screen.destroy()
        return register()
    else:
        _click_cancel()
        
    
   

   

def check_empty(entry_var) :
     if entry_var.get():
         pass     #your function where you want to jump
     else:
        print(' input required') 

def connection_test():
    
    try :
        stri = "https://www.google.co.in"
        urlopen(stri)
        return [True, "Internet Connection detected"]
    except Exception as e:
        return [False, "No internet connection detected\n make sure you have a working internet"]

def error_handler(info, msg, reason):

    connection_t = connection_test()
    tk.Label(register_screen, text=connection_t[1], bg="black", fg="red").pack()
    try:
        conn = validate_email(info) 
    except:
        pass
    error = True
    while error:
        if reason == "Invalid Username" and len(list(info)) < 2:
            error = False
            error_screen(reason, msg)

        elif reason == "Invalid Password" and len(list(info)) < 8:
            error = False
            error_screen(reason, msg)

        elif reason == "Invalid Email" and conn == False:
            error = False
            error_screen(reason, msg)

        else:
            return True




def register_user(*args):
    
    global user_info
    global email_info
    global pass_info

    user_info = username.get()
    email_info = email.get()
    pass_info = password.get()

    

    emaiL_error_msg = "Oooops Invalid email or email address already taken \nPlease try with a valid Email address"
    username_error_msg = "Ooops already taken or invalid Username \nPlease try using a valid Username"
    pass_error_msg = "Invalid Password Please enter a secure password lenght at least 8"
    
    valid = False
    for info,msg,reason in zip([user_info, email_info, pass_info], [username_error_msg, emaiL_error_msg, pass_error_msg], ["Invalid Username", "Invalid Email", "Invalid Password"]):

        valid = error_handler(info, msg, reason)
        if valid:
            pass
        else:
            break

    if valid:
        data = db("code_assistant.db")
        
        result = data.insert(user_info, email_info, pass_info)

        if result:
            tk.messagebox.showerror("User Credential Exist", result)
            register_screen.destroy()
            return register()
        else:
            confirmation_email()
            

            
        user_entry.delete(0, tk.END)
        email_entry.delete(0,tk.END)
        pass_entry.delete(0, tk.END)
        register_screen.destroy()
        tk.messagebox.showinfo("CODE ASSISTANT", f"Successfully registered {user_info} please check your emails to confirm your registration (you might have to check your spam box as well if email not received)")



def register(*args):
    global email_entry
    global user_entry
    global pass_entry
    global register_screen
    global email
    global username 
    global password 

    try:
        register_screen.destroy()
    except:
        pass

    register_screen = tk.Toplevel(screen)
    register_screen.title(title)
    register_screen.resizable(False,False)
    register_screen.geometry("380x350")
    
    
    register_screen.configure(background="black",  pady=10)
    register_screen.wm_attributes("-alpha", 1)
    
    
    
    username = tk.StringVar()
    email = tk.StringVar()
    password = tk.StringVar()

    tk.Label(register_screen, text = "Please enter details below", width=100, height= 2, bg =  "grey", font = ("Calibri", 14, "bold")).pack()
    tk.Label(register_screen, text="", bg="black", fg="green").pack()
    tk.Label(register_screen, text="Username", bg="black", fg="green").pack()
    tk.Label(register_screen, text="", bg="black", fg="green")
    user_entry = tk.Entry(register_screen, textvariable = username, width=35, highlightbackground="green", highlightthickness=2)
    user_entry.pack()

    tk.Label(register_screen, text="Email", bg="black", fg="green").pack()
    tk.Label(register_screen, text="", bg="black", fg="green")
    email_entry = tk.Entry(register_screen, textvariable = email, width=35, highlightbackground="green", highlightthickness=2)
    email_entry.pack()

    tk.Label(register_screen, text="", bg="black", fg="green")
    tk.Label(register_screen, text="Password", bg="black", fg="green").pack()
    tk.Label(register_screen, text="", bg="black", fg="green")
    pass_entry = tk.Entry(register_screen, width=35, textvariable = password, show="*", highlightbackground="green", highlightthickness=2)
    pass_entry.pack()
    tk.Label(register_screen, text="", bg="black", fg="green").pack()
    tk.Button(register_screen, text = "Register", command = register_user, width = 10, bg="black", fg="green", activebackground="grey").pack()


def login_authenti(*args):
    user_info = username.get()
    pass_info = password.get()
    data = db("code_assistant.db")
    records = data.fetch()
    for i in records:
        if user_info and pass_info in i:
            user_entry.delete(0, tk.END)
            pass_entry.delete(00, tk.END)
            login_screen.destroy()
            screen.destroy()

            data = db("code_assistant.db") # db is the database
            data.insert_hist(user_info)
            print(data.fetch_hist())

            ca.code_assistant() #ca here refers to codeAssistant.py imported as ca
            
            return

    else:
        tk.messagebox.showinfo("Login Fail", f"Username or Password incorect\ncheck your connection and try again\n if the problem persist please contact tony@oceansofty.com")
        login_screen.destroy()
        login()


def login():
    
    global email_entry
    global user_entry
    global pass_entry
    global login_screen
    global email
    global username 
    global password 
    global screen


    try:
        login_screen.destroy()
    except:
        pass

    login_screen = tk.Toplevel(screen)
    login_screen.title(title)
    login_screen.resizable(False,False)
    login_screen.geometry("300x250")
    login_screen.attributes('-topmost', True)
    login_screen.configure(background="black",  pady=10)

    username = tk.StringVar()
    email = tk.StringVar()
    password = tk.StringVar()
    
    tk.Label(login_screen, text = "Please enter login details", width=100, height= 2, bg =  "grey", font = ("Calibri", 14, "bold")).pack()

    tk.Label(login_screen, text="", bg="black", fg="green").pack()

    tk.Label(login_screen, text="Username or Email", bg="black", fg="green").pack()
    tk.Label(login_screen, text="", bg="black", fg="green")
    user_entry = tk.Entry(login_screen, textvariable = username, width=35, highlightbackground="green", highlightthickness=2)
    user_entry.pack()

    # tk.Label(login_screen, text="Email", bg="black", fg="green").pack()
    # tk.Label(login_screen, text="", bg="black", fg="green")
    # email_entry = tk.Entry(login_screen, textvariable = email, width=35, highlightbackground="green", highlightthickness=2)
    # email_entry.pack()

    tk.Label(login_screen, text="", bg="black", fg="green")

    tk.Label(login_screen, text="Password", bg="black", fg="green").pack()
    tk.Label(login_screen, text="", bg="black", fg="green")
    pass_entry = tk.Entry(login_screen, width=35, textvariable = password, show="*", highlightbackground="green", highlightthickness=2)
    pass_entry.pack()

    tk.Label(login_screen, text="", bg="black", fg="green").pack()

    tk.Button(login_screen, text = "Login", command = login_authenti, width = 10, bg="black", fg="green", activebackground="grey").pack()



def _click_cancel():
    
    ask = messagebox.askquestion("EXIT CODE ASSISTANT", "Unsaved data maybe lost\nExit anyway?")
    print(ask)
    if ask ==  "yes":
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
        return 


def next_widget(event):
    event.Button.tk_focusNext().focus()
    return "break"


def main():
    import os

    os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "python" to true' ''')
    global screen
    screen = tk.Tk()
    screen.geometry("350x280")
    screen.resizable(False, False)
    screen.title(" CODE ASSISTANT")
    screen.protocol("WM_DELETE_WINDOW", _click_cancel)

    bg_img = tk.PhotoImage(file=r"C:\Users\byamu\OneDrive\Desktop\codeAssitant\code\bg.gif")
    screen.configure(background="black",  pady=10)
    screen.bind("<Return>", register)
    screen.bind_class("Up", "<Down>", next_widget)



    tk.Label(text = "CODE ASSISTANT Version 1.0", width=100, height= 2, bg =  "grey", font = ("Calibri", 14, "bold")).pack()
    tk.Label(text = "", bg="black").pack()

    login_btn = tk.Button(text = "Login",command = login, width = 30, height= 2)
    login_btn.pack()
    login_btn

    tk.Label(text = "", bg="black").pack()

    reg_btn = tk.Button(text = "Register", command = register, width = 30, height= 2)
    reg_btn.pack()
    reg_btn.focus()

    screen.mainloop()

main()


