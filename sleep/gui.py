#----------------------------------------Sleep Analysis-------------------------------------------#`    `
from pathlib import Path 
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from tkinter import *
from customtkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from data import *
from advices import *
import advices
import matplotlib.pyplot as plt
from datetime import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1550x800")
window.configure(bg = "#2A2F4F")

gui_canvas = Canvas(
    window,
    bg = "#2A2F4F",
    height = 800,
    width = 1550,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

gui_canvas.place(x = 0, y = 0)
gui_canvas.create_rectangle(
    0.0,
    0.0,
    2000.0,
    72.0,
    fill="orange", # or #E5BEEC
    outline=""
)

gui_canvas.create_text(
    83.0,
    16.0,
    anchor="nw",
    text="Sleep Analysis",
    fill="#000000",
    font=("Inter Bold", 30 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = gui_canvas.create_image(
    240.0,
    143.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_222.png"))
image_2 = gui_canvas.create_image(
    240.0,
    450.0,
    image=image_image_2
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = gui_canvas.create_image(
    1170.0,
    143.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = gui_canvas.create_image(
    830.0,
    142.0,
    image=image_image_6
)

gui_canvas.create_text(
    140.0,
    117.0,
    anchor="nw",
    text="Asleep Average",
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)

gui_canvas.create_text(
    728.0,
    116.0,
    anchor="nw",
    text="Monthly Steps Average",
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)

gui_canvas.create_text(
    1070.0,
    117.0,
    anchor="nw",
    text="Monthly Heart Rate Average",
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1)
)

def average_asleep_gui():
    gui_canvas.create_text(
        124.0,
        136.0,
        anchor="nw",
        text=asleep_average(month_data),
        fill="#FFFFFF",
        font=("Inter Bold", 22 * -1),
        tags="average_text"  # Adding a tag for easy deletion
    )
average_asleep_gui()

gui_canvas.create_text(
    1070.0,
    136.0,
    anchor="nw",
    text=calculate_heart_rate_average(month_data),
    fill="#FFFFFF",
    font=("Inter Bold", 22 * -1),
    tags="heart_rate_average"
)

steps = calculate_monthly_steps_average(month_data)
gui_canvas.create_text(
    740.0,
    135.0,
    anchor="nw",
    text=steps,
    fill="#FFFFFF",
    font=("Inter Bold", 22 * -1),
    tags="monthly_steps_average"
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = gui_canvas.create_image(
    125.0,
    123.0,
    image=image_image_7
)

gui_canvas.create_text(
    300.0,
    126.0,
    anchor="nw",
    text=calculate_monthly_sleep_quality(month_data),
    fill="#D9FFCA",
    font=("Inter Bold", 20 * -1),
    tags="monthly_average_text"  # Adding a tag for easy deletion
)

gui_canvas.create_text(
    1228.0,
    130.0,
    anchor="nw",
    text="60-100 bpm",
    fill="#D9FFCA",
    font=("Inter Bold", 12 * -1)
)

gui_canvas.create_text(
    897.0,
    125.0,
    anchor="nw",
    text=str(steps_to_km(steps)),
    fill="#D9FFCA",
    font=("Inter Bold", 20 * -1),
    tags="steps_to_km"
)

gui_canvas.create_text(
    268.0,
    151.0,
    anchor="nw",
    text="Monthly sleep Quality",
    fill="#FFFFFF",
    font=("Inter Bold", 10 * -1)
)

gui_canvas.create_text(
    1220.0,
    151.0,
    anchor="nw",
    text="Normal heart rate",
    fill="#FFFFFF",
    font=("Inter Bold", 11 * -1)
)

gui_canvas.create_text(
    885.0,
    150.0,
    anchor="nw",
    text="distance in Km",
    fill="#FFFFFF",
    font=("Inter Bold", 11 * -1)
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = gui_canvas.create_image(
    718.0,
    122.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_31.png"))
image_12 = gui_canvas.create_image(
    47.0,
    25.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = gui_canvas.create_image(
    1055.0,
    123.0,
    image=image_image_13
)

#------------------------------------Generate random advice when the app launches---------------------------------#
random_value = advices.get_random_string()

# Create label widget
label = Label(window, text=random_value, bg="#2A2F4F", fg="white", font=("Inter Bold", 11))

# Embed the label onto the canvas
gui_canvas.create_window(510, 640, window=label, anchor="nw")

#---------------------------------------------Creating Table------------------------------------------------------#
table = ttk.Treeview(master=window, columns=table_columns, show="headings")

for column in table_columns:
    table.heading(column=column, text=column)
    table.column(column=column, width=130)

for row_data in table_data:
    table.insert(parent="", index="end", values=row_data)

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", background="#917FB3", fieldbackground="#917FB3", foreground="white")
style.configure("Treeview.Heading", background="#917FB3", fieldbackground="#917FB3", foreground="white")
style.map("Treeview", background=[("selected", "#E5BEEC")])

table.place(x=480, y=205, height=400)
#------------------------------------------------Chart Bar---------------------------------------------------------#
#definition of the update chart function
def update_chart(month_data):
    gui_canvas.delete("average_text")
    gui_canvas.create_text(
        124.0,
        136.0,
        anchor="nw",
        text=asleep_average(month_data),
        fill="#FFFFFF",
        font=("Inter Bold", 22 * -1),
        tags="average_text"  # Adding a tag for easy deletion
    )
    
    gui_canvas.delete("monthly_average_text")
    gui_canvas.create_text(
        300.0,
        126.0,
        anchor="nw",
        text=calculate_monthly_sleep_quality(month_data),
        fill="#D9FFCA",
        font=("Inter Bold", 20 * -1),
        tags="monthly_average_text"  # Adding a tag for easy deletion
    )

    gui_canvas.delete("heart_rate_average")
    gui_canvas.create_text(
    1070.0,
    136.0,
    anchor="nw",
    text=calculate_heart_rate_average(month_data),
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1),
    tags="heart_rate_average"
    )
    
    steps = calculate_monthly_steps_average(month_data)
    gui_canvas.delete("monthly_steps_average")
    gui_canvas.create_text(
    740.0,
    135.0,
    anchor="nw",
    text=steps,
    fill="#FFFFFF",
    font=("Inter Bold", 22 * -1),
    tags="monthly_steps_average"
    )
    
    gui_canvas.delete("steps_to_km")
    gui_canvas.create_text(
    897.0,
    125.0,
    anchor="nw",
    text=str(steps_to_km(steps)),
    fill="#D9FFCA",
    font=("Inter Bold", 20 * -1),
    tags="steps_to_km"
    )
    
    revenue_data = pd.DataFrame(month_data)
    revenue_data["Start"] = pd.to_datetime(revenue_data["Start"])
    
    # Sort the data by the "Time in bed" column
    revenue_data = revenue_data.sort_values(by="Time in bed")

    fig_1 = Figure(figsize=(4, 4), facecolor="#917FB3")
    ax_1 = fig_1.add_subplot()
    ax_1.set_facecolor("#917FB3")
    ax_1.bar(revenue_data["Start"], revenue_data["Time in bed"], alpha=0.7)
    ax_1.tick_params(labelsize=7, colors="white")
    fig_1.autofmt_xdate()
    ax_1.plot(revenue_data["Start"], revenue_data["Time in bed"], color="deepskyblue")
    ax_1.grid(visible=True)

    # Adding labels to the axes
    ax_1.set_xlabel("Day", fontsize=10, color="white")  # X-axis label
    ax_1.set_ylabel("Time in bed", fontsize=10, color="white")  # Y-axis label

    canvas = FigureCanvasTkAgg(figure=fig_1, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=60, y=260)
    
update_chart(month_data)
#-------------------------------Create dropdown menu for selecting month----------------------------------------------------#
sleep_analysis_by_month_label = Label(window, text="Sleep Analysis By Month",bg="#917FB3", fg="white", font=("Inter Bold", 12))
sleep_analysis_by_month_label.place(x=120,y=230)

label_month = Label(window, text="Select Month",bg="#917FB3", fg="white", font=("Inter Bold", 11))
label_month.place(x=355,y=210)
#the above code is work correctly
months = sorted(set(date.split()[0][:7] for date in sleepdata["Start"]))
dropdown_var =StringVar(window)
dropdown_var.set(months[-1])  # Set default value
dropdown_menu = OptionMenu(window,dropdown_var, *months,  command=lambda selected_month: update_chart(get_sleep_data_for_month(sleepdata, selected_month) ) )
dropdown_menu.config(background="#917FB3",font=("Inter Bold", 11))
dropdown_menu.place(x=350, y=230)

dropdown_var.trace_add("write",  get_sleep_data_for_month(sleepdata, dropdown_var.get()))
window.mainloop()
