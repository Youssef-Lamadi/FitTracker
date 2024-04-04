from tkinter import *

root = Tk()
root.title("Animation de texte")
root.geometry("1000x500")

frame = Frame(root, bg="#008DDA", width=300, height=500)
frame.place(x=0, y=0)

def animate_text(words, index=0):
    

    label.config(text='\n'.join(words[:index+1]))
    root.after(500, animate_text, words, index + 1)

def separate_text():
    words = 'Welcome to our appliaction'.split()
    animate_text(words)

label = Label(root, text="", font=("Arial", 30), bg="#008DDA", fg="white")
label.place(x=20, y=40)

separate_text()

root.mainloop()
