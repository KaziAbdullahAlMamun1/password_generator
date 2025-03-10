from tkinter import *
from tkinter import messagebox
import pyperclip
from random import choice,randint,shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def new_password():
    password_entry.delete(0,END)
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list+=[choice(symbols) for _ in range(randint(2, 4))]
    password_list+=[choice(numbers) for _ in range(randint(2, 4)) ]

    shuffle(password_list)

    password="".join(password_list)
    
   
    password_entry.insert(0,password)
    pyperclip.copy(password)
    print(password)
  



# ---------------------------- SAVE PASSWORD ------------------------------- #

window = Tk()

def added():
    
    website = website_entry.get()
    email =email_entry.get()
    password =password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }
    if (website=="" or email=="" or password == ""):
        messagebox.showinfo(message="please don't leave any field empty",title= "website")
       
    else:
        try:
            with open("data.json","r") as data_file:
                
                content = json.load(data_file)
                
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            content.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(content,data_file,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)


def search():
    website = website_entry.get()
    try:
        with open("data.json","r") as data_file:
            content = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="error",message="No data file found")
    else:
    
        
        try:
            messagebox.showinfo(title=website,message=f"email: {content[website]["email"]}\npassword: {content[website]["password"]}")
        except KeyError:
            messagebox.showerror(title="error",message="No details for the website exits")
# ---------------------------- UI SETUP ------------------------------- #


window.title("Password Manager")
window.config(padx=20,pady=20)
canvas = Canvas(height=200,width=200)

lock_photo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_photo)
canvas.grid(row=0,column=1)

website_label = Label(text= "Website",font=('calibre',10, 'bold'))
website_entry = Entry(width=35)
website_entry.focus()

email_label = Label(text="Email/Username",font=('calibre',10, 'bold'))
email_entry = Entry(width=30)
email_entry.insert(0,"hellomello@gmail.com")

password_label = Label(text="Password",font=('calibre',10, 'bold'))
password_entry = Entry(width= 27)

search_btn = Button(text="Search",font=('calibre',10, 'bold'),command=search)
pass_btn = Button(text="Generate Password",font=('calibre',10, 'bold'),command=new_password)

add_btn = Button(text="Add",width=36,font=('calibre',10, 'bold'),command=added)

website_label.grid(row=1,column=0)
website_entry.grid(row=1,column=1,columnspan=2)
search_btn.grid(row=1,column=2)
email_label.grid(row=2,column=0)
email_entry.grid(row=2,column=1,columnspan=2)
password_label.grid(row=3,column=0)
password_entry.grid(row=3,column=1,columnspan=1)
pass_btn.grid(row=3,column=2)
add_btn.grid(row=4,column=1,columnspan=2)



window.mainloop()
