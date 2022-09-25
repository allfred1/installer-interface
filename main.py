from platform import win32_edition
from tkinter import *
import os




window = Tk()

# visiual
logo = PhotoImage(file='logo.png') 
window.iconphoto(False, logo)
# Text Color = #E5DFDF
# BackGround = #284754
window.title('ETC')
window.geometry('400x400+25+35')
window.resizable(True, False)
window.config(bg='#284754')
name = Label(window, text="Starting", bg=('#284754'), fg=('#E5DFDF'), font=("Roboto",16), justify=RIGHT) # NOperation name
operator = Label(window, text="59 Secound",bg=('#284754'), fg=('#E5DFDF'), font=("Roboto",16), justify=RIGHT) # Duration 
Status = Label(window, text="OK",bg=('#284754'), fg=('#E5DFDF'), font=("Roboto",16), justify=RIGHT) # Status Completed or not

name.grid(
    row=0, column=0,
    columnspan=2,
    sticky='we',
    ipady=4
)
operator.grid(
    row=0, column=2, ipadx=34
)
Status.grid(
    row=0, column=3, rowspan=4, sticky='ns', ipadx=14
)
window.grid_columnconfigure(0, minsize=25),

def executor():
    Status = Label(window, text="OK",bg=('#284754'), fg=('#3CFF1E'), font=("Roboto",16), justify=RIGHT)

# You need to duplicate this code according to your needs. you can use this as
#  an installer for your software and use along with c# for a quick install


window.mainloop()