from tkinter import *
from PIL import Image, ImageTk
import subprocess
import os 
root = Tk()
root.config(bg="White")
root.title("Animation de texte")
root.geometry("1000x700")
def on_enter(button):
    if button == button_signup:
        button.config(image=photo_2)
    else:
        button_signin.config(image=photo_4)

def on_leave(button):
    if button == button_signup:
        button.config(image=photo_1)
    else:
        button_signin.config(image=photo_3)
def translation(button):
    root.destroy()
    
    if(button==button_signup):
        subprocess.run(["python",os.path.join(os.path.dirname(__file__),'signup.py')])
    else:
        subprocess.run(["python",os.path.join(os.path.dirname(__file__),'signin.py')])
signup_leave = Image.open(os.path.join(os.path.dirname(__file__),"images\\button_signup_leave - Copie (2).png")).resize((200,150))
signup_enter = Image.open(os.path.join(os.path.dirname(__file__),"images\\button_signup_enter - Copie.png")).resize((200,150))
signin_leave = Image.open(os.path.join(os.path.dirname(__file__),"images\\button_signin_leave - Copie.png")).resize((200,150))
signin_enter = Image.open(os.path.join(os.path.dirname(__file__),"images\\button_signin_enter - Copie.png")).resize((200,150))

button_signup = Button(root, image=None, borderwidth=0, highlightthickness=0, padx=10, pady=10,command=lambda:translation(button_signup))
button_signup.place(x=650, y=420)
photo_1 = ImageTk.PhotoImage(signup_leave)
photo_2 = ImageTk.PhotoImage(signup_enter)
button_signup.config(image=photo_1)

button_signin = Button(root, image=None, borderwidth=0, highlightthickness=0, padx=10, pady=10,command=lambda:translation(button_signin))
button_signin.place(x=650, y=550)
photo_3 = ImageTk.PhotoImage(signin_leave)
photo_4 = ImageTk.PhotoImage(signin_enter)
button_signin.config(image=photo_3)

button_signup.bind("<Enter>", lambda event, button=button_signup: on_enter(button))
button_signup.bind("<Leave>", lambda event, button=button_signup: on_leave(button))
button_signin.bind("<Enter>", lambda event, button=button_signin: on_enter(button))
button_signin.bind("<Leave>", lambda event, button=button_signin: on_leave(button))
frame_label = Frame(root, bg="#008DDA", width=500, height=700)
frame_label.place(x=0, y=0)

frame_gif = Frame(root, bg="#008DDA", width=700, height=420)
frame_gif.place(x=500, y=0)

def animate_gif(frame_index=0):
    label_gif.config(image=frames[frame_index])
    frame_index += 1
    if frame_index == len(frames):
        frame_index = 0
    root.after(10, animate_gif, frame_index)

def animate_text(words, index=0):
    if index < len(words):
        if words[index] == 'create':
            root.after(1000, lambda: label_text.config(text="Welcome\nto\nour\napplication\n\nCreated by:\n \n"))
            root.after(2000, lambda: display_names(['Mohamed Sabbar', 'Youssef Lamadi'], 0))
        else:
            label_text.config(text='\n'.join(words[:index+1]))
            root.after(200, animate_text, words, index + 1)

def display_names(names, index):
    if index < len(names):
        label_text.config(text=label_text.cget("text") + names[index] + "\n")
        root.after(1000, lambda: display_names(names, index + 1))
    else:
        root.after(1000, lambda: animate_text([], 0))

def separate_text():
    words = 'Welcome to our application create by '.split()
    animate_text(words)

label_text = Label(frame_label, text="", font=("Arial", 30), bg="#008DDA", fg="white")
label_text.place(x=20, y=40)
separate_text()

label_gif = Label(frame_gif)
label_gif.place(x=0, y=0)

gif = Image.open("C:\\Users\\Mohamed Sabbar\\OneDrive\\Bureau\\health.gif")

frames = []
try:
    while True:
        frames.append(ImageTk.PhotoImage(gif.copy().convert('RGBA')))
        gif.seek(gif.tell() + 1)
except EOFError:
    pass

animate_gif()
root.mainloop()
