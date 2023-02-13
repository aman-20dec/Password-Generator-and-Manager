
from os import path
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


EMAIL = "abc@email.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    #Password Generator Project
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = random.choices(letters, k= nr_letters)
   
    
    
    password_list.extend( [random.choice(symbols) for _ in  range(nr_symbols)])

    
    password_list.extend([ random.choice(numbers) for _ in range(nr_numbers )])

    random.shuffle(password_list)

    # "".join converts the list as a string
    password = "".join(password_list)
   

    pass_txt.delete(0, END)
    pass_txt.insert(0,password)

    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = web_txt.get()
    password = pass_txt.get()
    email = user_txt.get()

    if len(website) > 0 and len(password) > 0 and len(email) > 0:

        pass_string = f"{website} | {email} | {password}\n"

        message_to_save = f"These are the details entered.\n Email: {email}\nPassword: {password}\n Is it ok to save?"
        confirm = messagebox.askokcancel(title= website, message= message_to_save)
        if confirm:
            with open("Password_Manager.txt", "a") as file:
                file.write(pass_string)
            
            web_txt.delete(0, END)
            pass_txt.delete(0,END)
    elif len(website) == 0:
        messagebox.showwarning(title="Warning", message="Website is missing.")
    elif len(password) == 0:
        messagebox.showwarning(title="Warning", message="Password is missing.")
    elif len(email) == 0:
        messagebox.showwarning(title="Warning", message="Email is missing.")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
# window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

###########Row 0###############
canvas = Canvas(width= 200, height= 200)
canvas.grid(column=1, row=0)
lock_image = PhotoImage(file="logo.png")

canvas.create_image(100,100,  image=lock_image)

###########Row 1###############
web_lbl = Label(text="Website:")
web_lbl.grid(column=0, row=1)

web_txt = Entry(width=38)
web_txt.grid(column=1, row=1, columnspan=2)
web_txt.focus()
###########Row 2###############
user_lbl = Label(text="Email/Username:")
user_lbl.grid(column=0, row=2)

user_txt = Entry(width=38)
user_txt.grid(column=1, row=2, columnspan=2)
user_txt.insert(0, EMAIL)


###########Row 3###############
pass_lbl = Label(text="Password:")
pass_lbl.grid(column=0, row=3)

pass_txt = Entry(width=21)
pass_txt.grid(column=1, row=3 )

generate_pass_btn = Button(text="Generate Password", width=13, command= generate_password)
generate_pass_btn.grid(column=2, row=3)



add_btn = Button(text="Add", width=36, command=save_password)
add_btn.grid(column=1, row=4, columnspan= 2)


window.mainloop()