import os 
import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

import subprocess
def check_user():
    exist = False
    if connection.is_connected:
        cursor = connection.cursor()
        cursor.execute("SELECT username,password FROM personne1")
        rows = cursor.fetchall()
        for row in rows:
            if (user_champ.get(), password_champ.get()) == row:
                exist = True
                break
        
        if exist:
            cursor.execute("SELECT * FROM personne1 WHERE username=%s", (user_champ.get(),))
            
            row = cursor.fetchone()
            
            if row:
                L=list(row)
                print(L)
                f.destroy()
                subprocess.run(["python",os.path.join(os.path.dirname(__file__),'page_principale.py'),str(L[1]),str(L[2]),str(L[3]),str(L[4]),str(L[5]),str(L[6]),str(L[7]),str(L[8]),str(L[9])])

           
            
            
            
        else:
            messagebox.showerror("Error", "This user doesn't exist or the password is wrong!!")
            user_champ.delete(0, END)
            password_champ.delete(0, END)

def forget_password(e):
    password_window = Tk()
    password_window.geometry("500x500")
    password_window.title("Forget Password")
    # Ajoutez les widgets pour la réinitialisation du mot de passe ici
    password_window.mainloop()

def entry_in_user(e):
    if user_champ.get() == 'Username':   
        user_champ.delete(0, 'end')

def on_leave_user(e):
    if user_champ.get() == '':
        user_champ.insert(0, 'Username')

def entry_in_password(e):
    if password_champ.get() == 'Password':   
        password_champ.delete(0, 'end')

def on_leave_password(e):
    if password_champ.get() == '':
        password_champ.insert(0, 'Password')

def login():
    print("Connexion en cours...")

# Connexion à la base de données
connection = mysql.connector.connect(host="localhost", user="root", password="", database="client")

f = Tk()
f.geometry("1000x500")
f.title("Fitness")
f.configure(bg="white")

# Chargement des images
image_1 = Image.open(os.path.join(os.path.dirname(__file__), "images\\fitnees.jpg"))
image_user = Image.open(os.path.join(os.path.dirname(__file__), "images\\user.jpg"))
image_password = Image.open(os.path.join(os.path.dirname(__file__), "images\\password.webp"))

image_1 = image_1.resize((300, 500), Image.BICUBIC)
photo_1 = ImageTk.PhotoImage(image_1)

image_user = image_user.resize((40, 40), Image.BICUBIC)
photo_2 = ImageTk.PhotoImage(image_user)

image_password = image_password.resize((25, 25), Image.BICUBIC)
photo_3 = ImageTk.PhotoImage(image_password)

label = Label(f, image=photo_1)
label.pack(side=LEFT)

Label(f, text="Sign in", bg="white", font=("Arial", 20)).pack()

Label(f, image=photo_2, bg="white").place(x=450, y=108)

user_champ = Entry(f, borderwidth=1, relief="flat", font=("Arial", 18))
user_champ.insert(0, "Username")
user_champ.bind("<FocusIn>", entry_in_user)
user_champ.bind("<FocusOut>", on_leave_user)

user_champ.place(x=530, y=115)
Frame(f, bg="black", width=250, height=2).place(x=530, y=150)
Label(f, image=photo_3, bg="white").place(x=460, y=180)

password_champ = Entry(f, borderwidth=1, relief="flat", font=("Arial", 18))
password_champ.insert(0, "Password")
password_champ.bind("<FocusIn>", entry_in_password)
password_champ.bind("<FocusOut>", on_leave_password)
password_champ.place(x=530, y=180)
Frame(f, bg="black", width=250, height=2).place(x=530, y=215)

# Bouton de connexion
rounded_button_image = Image.open(os.path.join(os.path.dirname(__file__), "images\\button.png"))
rounded_button_image = rounded_button_image.resize((150, 70), Image.BICUBIC)
rounded_button_photo = ImageTk.PhotoImage(rounded_button_image)

button_1 = Button(f, image=rounded_button_photo, borderwidth=0, bg="white", relief="sunken", command=check_user)
button_1.place(x=530, y=250)

# Lien pour oublier le mot de passe


    
f.mainloop()
