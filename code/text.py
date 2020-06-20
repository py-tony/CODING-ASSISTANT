import tkinter as tk
from validate_email import validate_email

root = tk.Tk()

def _delete_window():
    print( "delete_window")
    try:
        root.destroy()
    except:
        pass



button = tk.Button(root, text="Destroy", command=root.destroy)
button.pack()


try:
    a = validate_email("tony@oceansofty.com", verify=True)
except Exception:
    tk.Label(root, text="this is an internet issue").pack()
    


root.mainloop()


