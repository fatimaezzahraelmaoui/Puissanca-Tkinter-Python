import tkinter as Tk
from tkinter import *

def puissance():
    puissance = entry_int.get()
    numbre_output = puissance**2
    output_var.set(numbre_output)
    
pro = Tk()
pro.title("my home")
pro.geometry("200x100")

mylabel = Label(pro, text="Browser", font="Tahoma 30 bold")
mylabel.pack(pady=30)

frome = Frame(pro)

mytext = Entry(pro, width=50, hieght=10)
mytext.pack(pady=15)

mybutton = Button(pro, text="Envoyer", fg="black", bg="yellow", font="helvatice 10 bold")
mybutton.pack()

output_var = Tk.gettvar()
pro.mainloop()