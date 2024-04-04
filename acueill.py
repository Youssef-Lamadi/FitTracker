from tkinter import *
from PIL import Image, ImageTk

def login(event):
    print("Connexion en cours...")

f = Tk()
f.geometry("1000x500")
f.title("Fitness")
f.configure(bg="white")

image_1 = Image.open("C:\\Users\\Mohamed Sabbar\\OneDrive\\Bureau\\fitnees.jpg")
image_user = Image.open("C:\\Users\\Mohamed Sabbar\\OneDrive\\Bureau\\user.jpg")
image_password = Image.open("C:\\Users\\Mohamed Sabbar\\OneDrive\\Bureau\\password.webp")

image_1 = image_1.resize((300, 500), Image.BICUBIC)
photo_1 = ImageTk.PhotoImage(image_1)

image_user = image_user.resize((40, 40), Image.BICUBIC)
photo_2 = ImageTk.PhotoImage(image_user)

image_password = image_password.resize((25, 25), Image.BICUBIC)
photo_3 = ImageTk.PhotoImage(image_password)

label = Label(f, image=photo_1)
label.pack(side=LEFT)

Label(f, text="Fitness Application", bg="white", font=("Courier", 20)).pack()

Label(f, image=photo_2, bg="white").place(x=350, y=60)
Label(f, text="Nom d'utilisateur", bg="white", font=("Courier", 15)).place(x=400, y=65)
user_champ = Entry(f, borderwidth=1, relief="flat", bg="lightblue", width=30).place(x=400, y=100)

Label(f, image=photo_3, bg="white").place(x=355, y=130)
Label(f, text="Mot de passe", bg="white", font=("Courier", 15)).place(x=405, y=130)
password_champ = Entry(f, borderwidth=1, relief="flat", bg="lightblue", width=30).place(x=400, y=160)

# Création d'un bouton personnalisé avec une image
rounded_button_image = Image.open("C:\\Users\\Mohamed Sabbar\\OneDrive\\Bureau\\button.png") 
rounded_button_image = rounded_button_image.resize((150, 70), Image.BICUBIC)
rounded_button_photo = ImageTk.PhotoImage(rounded_button_image)



button_1 = Button(f, image=rounded_button_photo, borderwidth=0, bg="white", command=login,relief="sunken")
button_1.place(x=420, y=200)
button_2=Label(f,text="password forget",font=("Courier",12),bg="white",fg="blue")
button_2.place(x=420, y=300)
button_2.bind("<Button-1>",login)
f.mainloop()



