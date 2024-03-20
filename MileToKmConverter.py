from tkinter import *
from tkinter.ttk import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to KM converter")
window.minsize(width=230, height=100)

#Entries
entry = Entry(width=10)

#Gets text in entry
print(entry.get())
entry.place(x=80, y=20)

#Labels
label = Label(text="Miles")
label.place(x=150, y=20)

km = 0


label1 = Label(text=f"is equal to\t{km}\tKm")
label1.place(x=10, y=60)

#Buttons
def action():
    km = float(entry.get()) * 1.60934
    label1.config(text=f"is equal to\t{km}\tKm")

#calls action() when pressed
button = Button(text="Calculate", command=action)
button.place(x=75, y=100)




window.mainloop()

