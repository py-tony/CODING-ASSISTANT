import tkinter as tk

btn_state = False
nav_root = None

brand_label = None
home_label = None
top_frame = None
root = None

yellow = "#FFD43B"
yellow2 ="#FFE873"
blue = "#306998"

def close_nav():
    if btn_state == True:
    # creat animated Navbar closing
        for x in range(301):
            nav_root.place(x=-x, y=0)
            
            top_frame.update()

        #reseting widget colors:
        
        home_label.config(bg=yellow)
        top_frame.config(bg=yellow)
        root.config(bg="gray17")


# setting switch function

def switch():
    global btn_state
    global brand_label
    global nav_root
    global top_frame
    #navbar frame
    nav_root = tk.Frame(root, bg=yellow2, height=1000, width=300)
    nav_root.place(x=0, y=0)

    l = tk.Label(nav_root, font="bahnschrist 15", bg="gray17", fg="white", height=2, width=300, padx=20).place(x=0, y=0)


    # set y-coordinate of navbar widgets

    y = 80
    
    

    # option in the navbar

    options = [("Profile", "profile_f"), ("Setting", "setting_f"),
                ("About", "about_f"), ("Help", "help_f"), ("Feedback", "feedback_f"),
                ("Dial A Mentor", "mentor_f")]
    
    for i in options:
        tk.Button(nav_root, text=i[0], font="Bahnschrist 15", bg=yellow2,fg="black", 
        activebackground=yellow, activeforeground="green", bd=0).place(x=25, y=y)
        y+=40

    # close Navbar button
    close_btn = tk.Button(nav_root, text="X", font="Bahnscchrist 16 bold", bg="gray17",  activebackground="white",fg="grey", bd=0, command=close_nav)
    close_btn.place(x=250, y=10)

         
    home_label.config(bg=yellow)
    top_frame.config(bg=yellow)
    root.config(bg="gray17")

    
    for x in range(-300,0):
        nav_root.place(x=x, y=0)
        nav_root.update()

    #turning btn ON
    btn_state = True

def top_menu():
    nav_menu = tk.Menu(root)
    nav_menu.add_command(label="Files", command=None)
    root.config(menu=nav_menu)

def code_assistant():
    global yellow
    global yellow2
    global blue
    global home_label
    global nav_root
    global top_frame
    global root
    HEIGHT = 500
    WIDTH = 800
    yellow = "#FFD43B"
    yellow2 ="#FFE873"
    blue = "#306998"

    root = tk.Tk(className=' CODING ASSISTANT')
    root.title("CODING ASSISTANT")
    root.config(bg="gray17")
    root.wm_attributes("-alpha", 0.95)
    root.geometry("600x500")
    top_menu()

    #setting swich case state for navbar
    btn_state = False

    top_frame = tk.Frame(root, bg=yellow)
    top_frame.pack(side="top", fill=tk.X)


    # header label text for nav
    home_label = tk.Label(top_frame, text="CA", font="Bahnscchrist 15", bg=blue, fg=yellow, height=2, padx=20)
    home_label.pack(side="right")


    nav_bar_btn = tk.Button(top_frame, text="MENU", font="Bahnscchrist 10 bold", bg=yellow, fg=blue, activebackground=yellow2, bd=0, command=switch)
    nav_bar_btn.place(x=10, y=10)

    



    

    





    root.mainloop()
    

code_assistant()