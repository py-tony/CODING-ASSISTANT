from tkinter import *

root = Tk()

def _delete_window():
    print( "delete_window")
    try:
        root.destroy()
    except:
        pass



root.protocol("WM_DELETE_WINDOW", _delete_window)
# root.bind("<Destroy>", _destroy)

button = Button(root, text="Destroy", command=root.destroy)
button.pack()

mainloop()