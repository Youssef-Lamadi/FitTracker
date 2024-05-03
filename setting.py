from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
import subprocess
import sys,os
from tkinter import messagebox
conn = mysql.connector.connect(host="localhost", user="root", password="", database="client")
root=Tk()
exits=False
old_password=Entry(root,borderwidth=0,font=("Arial",25),bg="#008DDA")
old_password.insert(0,"Write the old password")
old_password.bind("<Button-1>",lambda event:old_password.delete(0,END))
new_password=Entry(root,borderwidth=0,font=("Arial",25),bg="#008DDA")
new_password.insert(0,"Write the new password")
new_password.bind("<Button-1>",lambda event:new_password.delete(0,END))
def deleteuser():
    global conn
    reponse = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir continuer?")
    if reponse:
        if conn.is_connected():
            cursor=conn.cursor()
            cursor.execute("DELETE FROM personne1 WHERE username = %s",(sys.argv[1],))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("info","this user is deleted")
            root.destroy()
def ver():
  global conn
  if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT username,password from personne1")
        rows=cursor.fetchall()
        for i in rows:
            if(i==(sys.argv[1],sys.argv[9])):
                exits=True
        if exits==True:
            cursor.execute("UPDATE personne1 SET password= %s WHERE username=%s",(new_password.get(),sys.argv[1]))
            conn.commit()
        else:
            messagebox.showerror("Error", "This user doesn't exist or the password is wrong!!")
            old_password.insert(0,END)
def entercouleur(l):
    l.config(fg="white")
def leavecouleur(l):
   l.config(fg="black")


def change_password():
    root.after(200,lambda:old_password.place(x=200,y=410))
    root.after(200,lambda:Frame(root,height=4,width=350,bg="black").place(x=200,y=460))
    root.after(200,lambda:new_password.place(x=200,y=510))
    root.after(200,lambda:Frame(root,height=4,width=350,bg="black").place(x=200,y=560))
    root.after(200,lambda:button_sumbit.place(x=300,y=560))
    
root.geometry("800x700")
root.config(bg="#008DDA")
Label(root,text="Choose one of them ",font=("Arial",30,"bold"),bg="#008DDA").place(x=180,y=100)
user_delete_image=ImageTk.PhotoImage(Image.open( os.path.join(os.path.dirname(__file__),"images\\delete_user.png")).resize((60,60)))
froget_password_image=ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\forgetpassword.png")).resize((60,60)))
Label(root,image=user_delete_image,bg="#008DDA").place(x=150,y=200)
Label(root,image=froget_password_image,bg="#008DDA").place(x=150,y=290)
delete_user=Label(root,text="Delete user",bg="#008DDA",font=("Arial",30,"bold"))
delete_user.place(x=300,y=210)
forget_password=Label(root,text="Change password",bg="#008DDA",font=("Arial",30,"bold"))
forget_password.place(x=280,y=300)
delete_user.bind("<Enter>",lambda event:entercouleur(delete_user))
forget_password.bind("<Enter>",lambda event:entercouleur(forget_password))
delete_user.bind("<Leave>",lambda event:leavecouleur(delete_user))
forget_password.bind("<Leave>",lambda event:leavecouleur(forget_password))
delete_user.bind("<Button-1>",lambda event:leavecouleur(deleteuser()))
forget_password.bind("<Button-1>",lambda event:change_password())
i=ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\submit.png")).resize((180,140)))
button_sumbit=Button(root,text="sumbit",bg="#008DDA",borderwidth=0,image=i,command=ver)


root.mainloop()