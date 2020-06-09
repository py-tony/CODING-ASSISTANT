import tkinter as tk

def helloCallBack(entry):
    label["text"] = f"This  is {entry}"
    
    


HEIGHT = 500
WIDTH = 800

root = tk.Tk(className=' CODING ASSISTANT')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bg_img = tk.PhotoImage(file="bg.png")
background = tk.Label(root, image=bg_img)
background.place(relheight=1, relwidth=1)







frame = tk.Frame(root, bg="black", bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

entry = tk.Entry(frame, bg="white", font=40)
entry.place(relwidth=0.6, relheight=1)

B = tk.Button(frame, text ="Submit", font=40, command = lambda: helloCallBack(entry.get()) )
B.place(relx = 0.7, rely=0, relwidth=0.3, relheight=1)







lower_frame = tk.Frame(root, bg="black", bd=10 )
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, bg="white", anchor="nw",text="WELCOME TO", justify="left")
label.place(relwidth=1, relheight=1)








root.mainloop()