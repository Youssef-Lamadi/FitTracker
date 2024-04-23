from tkinter import *
from PIL import Image, ImageTk
import os
import subprocess
import sys
root = Tk()
root.geometry("1000x700")
root.title("profile")
root.config(bg="light blue")

# Load profile image
image1 = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\profile.png")).resize((200, 200)))
Label(root, image=image1, bg="light blue").place(x=800, y=0)

# Separator line
Frame(root, height=1000, width=5, bg="Black").place(x=200)

# Load icons
photos = [
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "images\\user.png")).resize((45, 45))),
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "images\\id.png")).resize((55, 55))),
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "images\\age.png")).resize((45, 45))),
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "images\\gender.png")).resize((45, 45))),
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "images\\weight.png")).resize((40, 40))),
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "images\\height .png")).resize((40, 40))),
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "images\\email.png")).resize((40, 40))),
]

# Place icons
Label(root, text="Your", bg="light blue", font=("Arial", 50, "bold")).place(x=0, y=100)
Label(root, text="Profil", bg="light blue", font=("Arial", 50, "bold")).place(x=0, y=250)

for i, j in zip(range(0, 2), range(50, 600, 70)):
    Label(root, image=photos[i], bg="light blue").place(x=300, y=j)

for i, j in zip(range(1, len(photos)), range(200, 700, 72)):
    Label(root, image=photos[i], bg="light blue").place(x=300, y=j)

# Labels for information
L = ["Username:", "First name:", "Last name:", "Age:", "Gender:", "Weight:", "Height:", "Gmail:"]
for i, j in zip(range(0, len(L)), range(50, 700, 73)):
    Label(root, text=L[i], bg="light blue",font=("Arial",23,"bold")).place(x=390, y=j)
#Label(text=sys.argv[2]).pack()
Label(root,text=sys.argv[2],bg="light blue",font=("Arial", 23, "bold")).place(x=560,y=51)
Label(root,text=sys.argv[3],bg="light blue",font=("Arial", 23, "bold")).place(x=560,y=124)
Label(root,text=sys.argv[4],bg="light blue",font=("Arial", 23, "bold")).place(x=560,y=197)
Label(root,text=sys.argv[5],bg="light blue",font=("Arial", 23, "bold")).place(x=470,y=270)
Label(root,text=sys.argv[6],bg="light blue",font=("Arial", 23, "bold")).place(x=515,y=343)
Label(root,text=sys.argv[7],bg="light blue",font=("Arial", 23, "bold")).place(x=515,y=416)
Label(root,text=sys.argv[8],bg="light blue",font=("Arial", 23, "bold")).place(x=515,y=489)
Label(root,text=sys.argv[9],bg="light blue",font=("Arial", 23, "bold")).place(x=510,y=562)
root.mainloop()
