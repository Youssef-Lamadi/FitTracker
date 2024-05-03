from tkinter import *
import time
from PIL import Image, ImageTk
import sys
import subprocess
import os
import webbrowser
toggle = False
menu_is_open = False

def help():
    subprocess.run(["python", os.path.join(os.path.dirname(__file__), 'help.py')])

def profile():
     subprocess.run(["python", os.path.join(os.path.dirname(__file__), 'profile.py'), sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8]])
    
def settings():
    root.destroy()
    subprocess.run(["python", os.path.join(os.path.dirname(__file__), 'setting.py'), sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9]])
def statics()  :
    root.destroy()
    subprocess.run(["python", os.path.join(os.path.dirname(__file__), 'graphes.py')])
def brm():
    root.destroy()    
    subprocess.run(["python", os.path.join(os.path.dirname(__file__), 'workoutPlan\\main.py')])
def create_menu():
    global menu_frame
    menu_label = Label(menu_frame, text="Ceci est le menu", bg="#008DDA")
    menu_label.pack(padx=10, pady=5)

def toggle_menu():
    global menu_is_open
    if not menu_is_open:
        menu_is_open = True
        move_menu_to_right()
    else:
        menu_is_open = False
        move_menu_back()

def move_menu_to_right():
    global menu_frame

    for i in range(-200, 1):
        menu_frame.place(x=i, y=120)
        root.update()
        time.sleep(0.00)

def move_menu_back():
    global menu_frame

    for i in range(0, -201, -1):
        menu_frame.place(x=i, y=120)
        root.update()
        time.sleep(0.00)
    menu_frame.place(x=-200, y=120)

root = Tk()
root.geometry("2000x1280")
root.config(bg="white")
root.title("page principale")

x = Frame(bg="#008DDA", width=2000, height=400)
x.place(x=0)

menu_frame = Frame(root, bg="white", height=800, width=100)
menu_frame.place(x=-200, y=120)

image = Image.open(os.path.join(os.path.dirname(__file__), "images/menu.png")).resize((80, 80))
photo = ImageTk.PhotoImage(image=image)
user_image = ImageTk.PhotoImage(image=Image.open(os.path.join(os.path.dirname(__file__), "images/user.png")).resize((60, 60)))
profile_button = Button(menu_frame, image=user_image, bg="white", borderwidth=0, command=profile)
profile_button.place(x=15, y=40)
image_setting = ImageTk.PhotoImage(image=Image.open(os.path.join(os.path.dirname(__file__), "images/parametres.png")).resize((60, 60)))
setting_button = Button(menu_frame, image=image_setting, bg="white", borderwidth=0,command=settings)
statistics_image = ImageTk.PhotoImage(image=Image.open(os.path.join(os.path.dirname(__file__), "images/stat.png")).resize((60, 60)))
help_image = ImageTk.PhotoImage(image=Image.open(os.path.join(os.path.dirname(__file__), "images/help.png")).resize((60, 60)))
statistics_button = Button(menu_frame, image=statistics_image, bg="white", borderwidth=0,command=statics)
statistics_button.place(x=15, y=170)
brm_image=ImageTk.PhotoImage(image=Image.open(os.path.join(os.path.dirname(__file__), "images/BRM.png")).resize((60, 60)))
brm_button = Button(menu_frame, image=brm_image, bg="white", borderwidth=0,command=brm)
brm_button.place(x=15, y=420)
Label(menu_frame, text="profile", font=("Arial", 19, "bold"), bg="white").place(x=0, y=100)
Label(menu_frame, text="statistics", font=("Arial", 19, "bold"), bg="white").place(x=0, y=230)
Label(menu_frame, text="settings", font=("Arial", 19, "bold"), bg="white").place(x=0, y=360)
Label(menu_frame, text="help", font=("Arial", 19, "bold"), bg="white").place(x=15, y=600)
Label(menu_frame, text="Work out", font=("Arial", 16, "bold"), bg="white").place(x=0, y=480)
help_button = Button(menu_frame, image=help_image, bg="white", borderwidth=0, command=help)
help_button.place(x=10, y=540)
setting_button.place(x=10, y=300)
button = Button(root, text="Menu", command=toggle_menu, image=photo, borderwidth=0, bg="#008DDA")
button.place(x=20, y=30)

def animate_text(l, words, index=0):
    if index < len(words):
        l.config(text=' '.join(words[:index+1]), font=("Arial", 45))
        root.after(300, animate_text, l, words, index + 1)

def separate_text():
    words = f'Welcome back {sys.argv[2]} {sys.argv[3]}'.split()
    animate_text(label_text, words)

def animate_text1(l, chars, index=0):
    if index < len(chars):
        l.config(text=l.cget("text") + chars[index])
        root.after(25, animate_text1, l, chars, index + 1)
    else:
        if(l==label_water):
         root.after(33000, remove_text, l)
         root.after(40000,lambda:water.destroy())
         
        if(l==label_food):
            
            root.after(15500,remove_text,l)
            root.after(24000,lambda:food.destroy())
        if(l==label_run):
            root.after(1000,remove_text,l)
            root.after(8100,lambda:run.destroy())

def remove_text(l, index=0):
    if len(l.cget("text")) > 0:
        l.config(text=l.cget("text")[:-1])
        root.after(25, remove_text, l, index + 1)

label_text = Label(x, text="", font=("Arial", 30), bg="#008DDA", fg="white")
label_text.place(x=20, y=40)

label_text = Label(root, text="", font=("Arial", 25), bg="#008DDA")
label_text.place(x=190, y=100)

curseur_label = Label(root, text="", bg="#008DDA", font=("Arial", 50))
curseur_label.place(x=180, y=100)

running = True

def stop_update():
    global running
    running = False
    curseur_label.config(text="")

root.after(2500, stop_update)

def update():
    global running
    global toggle
    if running:
        if toggle:
            curseur_label.config(text="")
        else:
            curseur_label.config(text="|")
        toggle = not toggle
        root.after(100, update)

def change_position():
    curseur_label.place(x=450, y=60)
    curseur_label.config(text="|")

update()
root.after(2500, separate_text)



water_image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\drop.png")).resize((90,90)))
food_image=ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\salad.png")).resize((90,90)))
run_image=ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\speed.png")).resize((90,90)))
def affiche(i):
    global water
    global food
    global run
    if(i==water_image):
     water=Label(root, image=i, bg="white")
    water.place(x=250, y=420)
    if(i==food_image):
     food=Label(root, image=i, bg="white")
     food.place(x=700, y=420)
    if(i==run_image):
      run=Label(root, image=i, bg="white")
      run.place(x=1300, y=420)
label_water=Label(root,text="",font=("Arial",17,"bold"),bg="white")
label_water.place(x=150,y=530)
label_food=Label(root,text="",font=("Arial",17,"bold"),bg="white")
label_food.place(x=550,y=530)
label_run=Label(root,text="",font=("Arial",17,"bold"),bg="white")
label_run.place(x=1150,y=530)
label_texte=Label(root,text="",font=("Arial",30,"bold"),bg="white")
label_texte.place(x=100,y=530)
label_web=Label(root,text="",font=("Arial",20,"bold"),bg="white")
label_web.place(x=500,y=600)

root.after(4000,lambda:animate_text1(label_water, "Stay Hydrated: Drink water \n regularly throughout \n the day to maintain proper\n hydration levels.\n Your body needs water\nto function optimally\nso it's essential to stay \nhydrated for overall health."))
root.after(3500, lambda: affiche(water_image))
root.after(10000, lambda: affiche(food_image))
root.after(18200,lambda:affiche(run_image))

root.after(10500,lambda:animate_text1(label_food, "Focus on Whole Foods: Base your \nmeals around whole,\nminimally processed \nfoods such as fruits,\nvegetables,whole grains,lean proteins,\nand healthy fats.\nThese foods are rich in nutrients\nand provide essential vitamins,\nminerals, and fiber."))
root.after(18700,lambda:animate_text1(label_run,"Start Slowly: If you're\nnew to running\n or getting back \ninto it after a break,\nstart with a manageable\n pace and distance.\nIncrease your intensity\nand duration over time to\navoid injury and build endurance."))
root.after(51000,lambda:animate_text1(label_texte,"For more infomations visite the website bellow:"))
root.after(55000,lambda:animate_text1(label_web,"www.xnxx.com:"))
label_web.bind("<Button-1>",lambda event:webbrowser("www.xnxx,com"))
label_web.bind("<Enter>",lambda event:label_web.config(fg="white"))
label_web.bind("<Leave>",lambda event:label_web.config(fg="black"))

root.mainloop()
