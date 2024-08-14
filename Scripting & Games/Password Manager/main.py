from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Find Data in JSON

def search_data():
    website = website_entry.get()
    file = open("data.json", "r")
    data = json.load(file)
    email = data[website]["email"]
    password = data[website]["password"]
    messagebox.showinfo("Account details", f"Email: {email}\nPassword: {password}")



#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_to_list():
    password = password_entry.get()
    website = website_entry.get()
    email = email_entry.get()

    new_data = {
        website : {
            "email": email,
            "password": password
        }
    }

    ok = messagebox.askokcancel(title=website, message=f"Following are the details entered:\nemail = {email} \npassword = {password}"
                                + "\nClick Ok to confirm.")

    if ok:

        with open("data.json", "r+") as jsonFile:
            data = json.load(jsonFile)
            data.update(new_data)
            jsonFile.seek(0)
            json.dump(data, jsonFile, indent = 4)

        password_entry.delete(0, END)
        website_entry.delete(0, END)
        email_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=0, columnspan=3)

website = Label(text="Website:", font=("Arial", 10, "bold"))
website.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=1)

email_data = Label(text="Email/Username:", font=("Arial", 10, "bold"))
email_data.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.insert(END, "abc@xyz.com")
email_entry.grid(row=2, column=1, columnspan=2)

password = Label(text="Password:", font=("Arial", 10, "bold"))
password.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, columnspan=1, sticky=W)

button = Button(text="Generate", font=("Arial", 7, "italic"), width=15, command=generate_password)
button.grid(row=3, column=1, columnspan=2, sticky=E)

search_button = Button(text="Search", font=("Arial", 7, "italic"), width=15, command=search_data)
search_button.grid(row=1, column=2)

button = Button(text="Add", font=("Arial", 7, "italic"), width=41, command=add_to_list)
button.grid(row=4, column=1, columnspan=2)


window.mainloop()