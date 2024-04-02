from tkinter import *

























from tkinter import Tk, Button, Frame, Label

def switch_mode():
  global bg_color, text_color
  if bg_color == "black":
    bg_color = "white"
    text_color = "black"
  else:
    bg_color = "black"
    text_color = "white"
  root.config(bg=bg_color)
  for label in label_list:
    label.config(bg=bg_color, fg=text_color)

root = Tk()
root.title("Summary")
root.geometry("400x300")

bg_color = "black"
text_color = "white"

root.config(bg=bg_color)

frame_title = Frame(root, bg=bg_color)
frame_title.pack(fill="x", pady=10)

label_title = Label(frame_title, text="Summary", fg=text_color, bg=bg_color, font=("Arial", 20))
label_title.pack(padx=10)

frame_data = Frame(root, bg=bg_color)
frame_data.pack(fill="both", expand=True)

label_list = []

label_favourites = Label(frame_data, text="Favourites", fg=text_color, bg=bg_color, font=("Arial", 16))
label_favourites.pack(pady=5)
label_list.append(label_favourites)

button_edit = Button(frame_data, text="Edit", fg=text_color, bg=bg_color, font=("Arial", 12))
button_edit.pack(pady=5)

label_sleep = Label(frame_data, text="Sleep Analysis        May 2022 >", fg=text_color, bg=bg_color, font=("Arial", 12))
label_sleep.pack(pady=5)
label_list.append(label_sleep)

label_sleep_data = Label(frame_data, text="3hr 2 min", fg=text_color, bg=bg_color, font=("Arial", 16))
label_sleep_data.pack(pady=5)
label_list.append(label_sleep_data)

label_steps = Label(frame_data, text="Steps                    04:24 >", fg=text_color, bg=bg_color, font=("Arial", 12))
label_steps.pack(pady=5)
label_list.append(label_steps)

label_steps_data = Label(frame_data, text="170 steps", fg=text_color, bg=bg_color, font=("Arial", 16))
label_steps_data.pack(pady=5)
label_list.append(label_steps_data)

button_all_data = Button(frame_data, text="Show All Health Data                                 >", fg=text_color, bg=bg_color, font=("Arial", 12))
button_all_data.pack(pady=5)

button_mode = Button(root, text="Dark Mode", fg=text_color, bg=bg_color, command=switch_mode)
button_mode.pack(pady=10)

root.mainloop()
