from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import os 
def connection():
    
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="client")
    if(entries[9].get()==entries[8].get()):
    
      if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT username from personne1")
        rows=cursor.fetchall()
        for i in rows:
            if((entries[0].get(),)==i):
                messagebox.showerror("error","This username is already used!")
                entries[0].delete(0,'end')
        else:
         valeurs=[]
         for i in range(0,9):
            valeurs.append(entries[i].get())
        
        
        
         cursor.execute("INSERT INTO personne1 (username, first_name, last_name, gender, age, weight,height ,email,password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", tuple(valeurs))
         conn  .commit()
            
        
            
        cursor.close()
        conn.close()
        messagebox.showinfo("info","your user is added to our database!")
        signup_window.after(100,signup_window.destroy)
        
    else:
        messagebox.showerror("error","inscription error!!!")
        entries[9].delete(0,'end')
   
def on_entry_focus_in(event):
    global a
    a = event.widget.get()
    if a in default_names:
        event.widget.delete(0, END)

def on_entry_focus_out(event):
    if not event.widget.get():
        event.widget.insert(0, a)

signup_window = Tk()
signup_window.config(bg="light blue")
signup_window.geometry("1000x800")

signup_image = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\signup.webp")).resize((490, 800))) 
Label(signup_window, image=signup_image).pack(side="left")
Label(signup_window, text="Sign Up", font=("Arial", 30,"bold"), bg="light blue").place(x=650, y=10)

entries = [
    Entry(signup_window, bg="light blue",borderwidth=0, font=("Arial", 19)),
    Entry(signup_window, bg="light blue",borderwidth=0, font=("Arial", 19)),
    Entry(signup_window, bg="light blue",borderwidth=0, font=("Arial", 19)),
    Entry(signup_window, bg="light blue",borderwidth=0, font=("Arial", 19)),
    Entry(signup_window, bg="light blue",borderwidth=0, font=("Arial", 19)),
    Entry(signup_window, bg="light blue",borderwidth=0, font=("Arial", 19)),
    Entry(signup_window, bg="light blue",borderwidth=0, font=("Arial", 19)),
    Entry(signup_window, bg="light blue",borderwidth=0, font=("Arial", 19)),
    Entry(signup_window, bg="light blue",borderwidth=0, font=("Arial", 19)),
    Entry(signup_window, bg="light blue",borderwidth=0, font=("Arial", 19))

]

default_names = ["Username", "First name", "Last name", "Gender", "Age", "Weight","height","email", "password","Confirm password"]
for entry, default_name in zip(entries, default_names):
    entry.insert(0, default_name)
y_positions = [65, 130, 195, 260, 325, 390, 455, 520, 585,650]

for entry, y in zip(entries, y_positions):
    entry.place(x=580, y=y)
    entry.bind("<FocusIn>", on_entry_focus_in)
    entry.bind("<FocusOut>", on_entry_focus_out)

for y in range(100, 715, 65):
    Frame(signup_window, bg="black", width=300, height=2).place(x=580, y=y)

signup_enter = Image.open("C:\\Users\\Mohamed Sabbar\\OneDrive\\Bureau\\java programme\\FitTracker\\FitTracker\\images\\button_signup_leave.png").resize((200, 100))
photo_1 = ImageTk.PhotoImage(signup_enter)
button_connection = Button(signup_window, bg="black", image=photo_1, borderwidth=0, highlightthickness=0, padx=10, pady=10, command=connection)
button_connection.place(x=610, y=700)
photos=[
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\user.png")).resize((35,35))),  
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\id.png")).resize((45,45))),
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\id.png")).resize((45,45))),
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\gender.png")).resize((45,45))),
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\age.png")).resize((45,45))),
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\weight.png")).resize((40,40))),
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\height .png")).resize((40,40))),
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\password.webp")).resize((40,40))),
    ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__),"images\\email.png")).resize((40,40)))
]
for i,y in zip(range(0,7),range(66,507,63)):
   Label(signup_window,image=photos[i],bg="Light blue").place(x=530,y=y)

Label(signup_window,image=photos[8],bg="Light blue").place(x=526,y=510)
Label(signup_window,image=photos[7],bg="Light blue").place(x=526,y=585)
Label(signup_window,image=photos[7],bg="Light blue").place(x=526,y=645)
signup_window.mainloop()
print(os.path.dirname(__file__))