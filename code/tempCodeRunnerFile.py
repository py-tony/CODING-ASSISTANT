home_label.config(bg=yellow)
    top_frame.config(bg=yellow)
    root.config(bg="gray17")

    
    for x in range(-300,0):
        nav_root.place(x=x, y=0)
        nav_root.update()

    #turning btn ON
    btn_state = True