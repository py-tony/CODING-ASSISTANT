import tkinter as tk


def error_button():
    
    error.destroy()

def register_user():
    user_info = username.get()
    email_info = email.get()
    pass_info = password.get()

    global error

    with open("users.txt", "a+") as f:
        data = f.read()

    while True:
        if len(list(user_info)) < 2:
            print(len(list(user_info)), user_info)            

            error = tk.Tk()
            error.title("ERROR")
            tk.Label(text="")
            tk.Label(error, text="name characters cannot be less than 2", fg = "red").pack()
            tk.Button(error, text = "OK", command = error_button, width = 10, default="active").pack()
            login.destroy()
            return register()

        else:
            break
    
    data.write(user_info+", "+email_info+", "+pass_info+"\n")

    user_entry.delete(0, tk.END)
    email_entry.delete(0,tk.END)
    pass_entry.delete(0, tk.END)

    tk.Label(text="").pack()
    tk.Label(screen, text=f"Successfully registered {user_info} \nplease check your emails", fg = "green", font = ("Calibri", 14)).pack()
    login.destroy()

def register():
    global login

    login = tk.Toplevel(screen)
    login.title("Login")
    login.resizable(False,False)
    login.geometry("320x250")
    
    global email_entry
    global user_entry
    global pass_entry

    global email
    global username
    global password

    username = tk.StringVar()
    email = tk.StringVar()
    password = tk.StringVar()

    tk.Label(login, text = "Please enter details below", width = 300).pack()
    tk.Label(login, text="").pack()
    tk.Label(login, text="Username").pack()
    tk.Label(login, text="")
    user_entry = tk.Entry(login, textvariable = username, width=35)
    user_entry.pack()

    tk.Label(login, text="Email").pack()
    tk.Label(login, text="")
    email_entry = tk.Entry(login, textvariable = email, width=35)
    email_entry.pack()

    tk.Label(login, text="")
    tk.Label(login, text="Password").pack()
    tk.Label(login, text="")
    pass_entry = tk.Entry(login, width=35, textvariable = password, show="*")
    pass_entry.pack()
    tk.Label(login, text="").pack()
    tk.Button(login, text = "register", command = register_user, width = 10).pack()
    
    


def login():
    print("logging in")

def main():
    global screen
    screen = tk.Tk()
    screen.geometry("320x250")
    screen.resizable(False, False)
    screen.title(" CODE ASSISTANT")
    screen.protocol("VM_DELETE_WINDOW", click_cancel)
    screen.bind("<Return>". click_ok)
    


    tk.Label(text = "CODE ASSISTANT Version 0.1", width=100, height= 2, bg =  "grey", font = ("Calibri", 14)).pack()
    tk.Label(text = "").pack()
    tk.Button(text = "Login", width = 30, height= 2).pack()
    tk.Label(text = "").pack()
    tk.Button(text = "Register", command = register, width = 30, height= 2).pack()

    screen.mainloop()

main()

