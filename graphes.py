from tkinter import *
from PIL import Image, ImageTk
import subprocess
import os

root = Tk()

def staticts(word):
    root.destroy()
    if word == "sleep":
        subprocess.run(["python", os.path.join(os.path.dirname(__file__), 'sleep', 'gui.py')])
    else:
        subprocess.run(["python", os.path.join(os.path.dirname(__file__), 'steps', 'build', 'gui.py')])

def num(word, i=0):
    if word == "heure":
        if i < 8:
            heure_steps.config(text=f"{str(i)}h")
            i += 1
            if i < 4:
                root.after(50, lambda: num(word, i))
            else:
                root.after(200, lambda: num(word, i))
    elif word == "minute":
        if i < 23:
            minutes_steps.config(text=f"{str(i)} minute")
            i += 1
            if i < 17:
                root.after(50, lambda: num(word, i))
            else:
                root.after(200, lambda: num(word, i)) 
    elif word == "steps":                               
        if i < 470:
            step_steps.config(text=f"{str(i)}")
            i += 1
            if i < 400:
                root.after(10, lambda: num(word, i))
            else:
                root.after(100, lambda: num(word, i)) 

root.config(bg="#008DDA")
root.geometry("1000x1280")

Label(root, text="Choose one to show your statistics:", bg="#008DDA", font=("Arial", 30, "bold")).place(x=180, y=70)

image_sleep = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "images", "sleep.png")).resize((90, 90)))
image_steps = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), "images", "foot.png")).resize((90, 90)))

Label(root, text="Sleep Statistics", bg="#008DDA", font=("Arial", 25, "bold")).place(x=120, y=330)
Label(root, text="Steps Statistics", bg="#008DDA", font=("Arial", 25, "bold")).place(x=500, y=330)

Button_sleep = Button(root, borderwidth=0, image=image_sleep, bg="#008DDA", command=lambda: staticts("sleep"))
Button_sleep.place(x=180, y=200)
Button_steps = Button(root, borderwidth=0, image=image_steps, bg="#008DDA", command=lambda: staticts("steps"))
Button_steps.place(x=560, y=200)

Label(root, text="Last Statistics", bg="#008DDA", font=("Arial", 30, "bold")).place(x=340, y=450)

Label(root, image=image_sleep, bg="#008DDA", font=("Arial", 25, "bold")).place(x=180, y=550)
Label(root, image=image_steps, bg="#008DDA", font=("Arial", 25, "bold")).place(x=500, y=550)

heure_steps = Label(root, text="0", bg="#008DDA", font=("Arial", 20, "bold"))
heure_steps.place(x=180, y=660)
minutes_steps = Label(root, text="0", bg="#008DDA", font=("Arial", 20, "bold"))
minutes_steps.place(x=220, y=660)
step_steps = Label(root, text="0", bg="#008DDA", font=("Arial", 20, "bold"))
step_steps.place(x=550, y=660)

root.after(100, lambda: num("heure"))
root.after(100, lambda: num("minute"))
root.after(100, lambda: num("steps"))

root.mainloop()
