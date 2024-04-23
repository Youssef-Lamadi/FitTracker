'''advices=['Drink plenty of water throughout the day to maintain proper hydration levels, especially during and after exercise.',
'Drink plenty of water throughout the day to maintain proper hydration levels, especially during and after exercise.',

'Pay attention to your bodys signals and rest when you need it. Push yourself during workouts, but also know when to take breaks and allow for recovery.',
'Aim for 7-9 hours of quality sleep each night to allow your body to rest, recover, and perform at its best.',


'Establish achievable goals that are specific, measurable, attainable, relevant, and time-bound (SMART). Celebrate your progress along the way and adjust your goals as needed.']'''
from tkinter import *
import webbrowser
from PIL import ImageTk,Image
import os
import sys
def email(address):
    webbrowser.open("mailto:" + address)

def colour1(button):
    button.config(fg="white")
def colour2 (button):
    button.config(fg="black")
help_window = Tk()
help_window.geometry("1300x600")
help_window.config(bg="light blue")
os.path.join(os.path.dirname(__file__))
support_image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\support.png")).resize((400,600)))

Label(help_window, image=support_image, bg="light blue").pack(side=LEFT)
Label(help_window, bg="light blue", text="For any questions or suggestions ", font=("Tahoma", 25, "bold")).pack()
Label(help_window, bg="light blue", text="Contact with the developers of application ", font=("Tahoma", 25, "bold")).pack()
Label(help_window, bg="light blue", text="Youssef lamadi: ", font=("Tahoma", 25, "bold")).place(x=500, y=150)
button_1_email = Label(help_window, bg="light blue", text="yousseflamadi3@gmail.com", font=("Courier", 22, "bold"))
button_1_email.place(x=800, y=155)
Label(help_window, bg="light blue", text="Mohamed Sababar: ", font=("Tahoma", 25, "bold")).place(x=450, y=250)
button_2_email = Label(help_window, bg="light blue", text="mohamedazrou2003@gmail.com", font=("Courier", 22, "bold"))
button_2_email.place(x=800, y=255)

button_1_email.bind("<Button-1>", lambda event: email("yousseflamadi3@gmail.com"))
button_2_email.bind("<Button-1>", lambda event: email("mohamedazrou2003@gmail.com"))
button_1_email.bind("<Enter>", lambda event: colour1(button_1_email))
button_2_email.bind("<Enter>", lambda event: colour1(button_2_email))
button_1_email.bind("<Leave>", lambda event: colour2(button_1_email))
button_2_email.bind("<Leave>", lambda event: colour2(button_2_email))

help_window.mainloop()


