from tkinter import *
win=Tk()
width=300
height=500
sys_width=win.winfo_screenwidth()
sys_height=win.winfo_screenheight()
c_x=int(sys_width/2-width/2)
c_y=int(sys_height/2-height/2)
win.geometry(f"{width}x{height}+{c_x}+{c_y}")
win.mainloop()