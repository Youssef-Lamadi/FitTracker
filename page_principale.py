from tkinter import *
import time
from PIL import Image,ImageTk
import sys
import subprocess
import os
import time
menu_is_open = False
def help():
   subprocess.run(["python",os.path.join(os.path.dirname(__file__),'advices.py')])
def profile():
    #subprocess.run(["python",os.path.join(os.path.dirname(__file__),'profile.py'),sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8]])
    pass
def create_menu():
    global menu_frame
    menu_label = Label(menu_frame, text="Ceci est le menu", bg="lightblue")
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

    for i in range(-200, 0):
        menu_frame.place(x=i, y=120)
        root.update()
        time.sleep(0.00)

def move_menu_back():
    global menu_frame

    

    for i in range(0, -200, -1):

        
        menu_frame.place(x=i, y=120)
        root.update()
        time.sleep(0.00)
    menu_frame.place(x=-200, y=120)

root = Tk()
root.geometry("1000x800")
root.title("page principale")
#Label(root, text="Welcome To our application {}".format(sys.argv[2]+" "+sys.argv[3]),font=("Arial",22,"bold"),bg="light blue").place(x=200,y=30)
x=Frame(bg="light blue",width=1000,height=400).pack()
Frame(root,height=100,width=2)
menu_frame = Frame(x, bg="white",height=800,width=100)
menu_frame.place(x=-200, y=120)

image=Image.open(os.path.join(os.path.dirname(__file__,),"images\\menu.png")).resize((80,80))

photo=ImageTk.PhotoImage(image=image)
user_image=(ImageTk.PhotoImage(image=Image.open( os.path.join(os.path.dirname(__file__),"images\\user.png")).resize((60,60))))
profile_button=Button(menu_frame,image=user_image,bg="white",borderwidth=0,command=profile)
profile_button.place(x=15,y=40)
image_setting=ImageTk.PhotoImage(image=Image.open( os.path.join(os.path.dirname(__file__),"images\\parametres.png")).resize((60,60)))
setting_buton=Button(menu_frame,image=image_setting,bg="white",borderwidth=0)
staticts_image=ImageTk.PhotoImage(image=Image.open( os.path.join(os.path.dirname(__file__),"images\\stat.png")).resize((60,60)))
help_image=ImageTk.PhotoImage(image=Image.open( os.path.join(os.path.dirname(__file__),"images\\help.png")).resize((60,60)))
staticts_button=Button(menu_frame,image=staticts_image,bg="white",borderwidth=0)
staticts_button.place(x=15,y=170)
Label(menu_frame,text="profile",font=("Arial",19,"bold"),bg="white").place(x=0,y=100)
Label(menu_frame,text="statics",font=("Arial",19,"bold"),bg="white").place(x=0,y=230)
Label(menu_frame,text="settings",font=("Arial",19,"bold"),bg="white").place(x=0,y=360)
Label(menu_frame,text="help",font=("Arial",19,"bold"),bg="white").place(x=15,y=510)
Label(x,text=f"{time.strftime('%I:%M %p')}",bg="light blue",font=("Arial",22,"bold")).pack(side=LEFT)
help_button=Button(menu_frame,image=help_image,bg="white",borderwidth=0,command=help)
help_button.place(x=10,y=440)
setting_buton.place(x=10,y=300)
button = Button(root, text="Menu", command=toggle_menu,image=photo,borderwidth=0,bg="light blue")
button.place(x=20,y=30)

root.mainloop()
