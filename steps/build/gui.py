from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from data import *

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
    100.0,
    16.0,
    anchor="nw",
    text="Steps",
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
    file=relative_to_assets("image_2.png"))
image_2 = gui_canvas.create_image(
    250.0,
    445.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = gui_canvas.create_image(
    760.0,
    445.0,
    image=image_image_3
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = gui_canvas.create_image(
    1250.0,
    143.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = gui_canvas.create_image(
    770.0,
    142.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = gui_canvas.create_image(
    129.0,
    123.0,
    image=image_image_7
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = gui_canvas.create_image(
    660.0,
    122.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = gui_canvas.create_image(
    56.0,
    31.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = gui_canvas.create_image(
    1140.0,
    123.0,
    image=image_image_13
)

gui_canvas.create_text(
    140.0,
    114.0,
    anchor="nw",
    text="Traveled Distance in Km",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

gui_canvas.create_text(
    670.0,
    114.0,
    anchor="nw",
    text="Monthly Steps Average",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

gui_canvas.create_text(
    1153.0,
    114.0,
    anchor="nw",
    text="Max Steps Per Month",
    fill="#FFFFFF",
    font=("Inter Bold", 14 * -1)
)

gui_canvas.create_text(
    145.0,
    136.0,
    anchor="nw",
    text=calculate_travelled_distance(april),
    fill="#FFFFFF",
    font=("Inter Bold", 22 * -1),
    tags="travelled_distance"
)

gui_canvas.create_text(
    675.0,
    135.0,
    anchor="nw",
    text=calculate_monthly_average_steps(april),
    fill="#FFFFFF",
    font=("Inter Bold", 22 * -1),
    tags="calculate_monthly_average_steps"
)

gui_canvas.create_text(
    1165.0,
    136.0,
    anchor="nw",
    text=max_steps_per_month(april)[0][1],
    fill="#FFFFFF",
    font=("Inter Bold", 22 * -1),
    tags="max_steps_per_month"
)

gui_canvas.create_text(
    1320.0,
    126.0,
    anchor="nw",
    text=max_steps_per_month(april)[0][3],
    fill="#D9FFCA",
    font=("Inter Bold", 20 * -1),
    tags="max_steps_per_month_date"
)

gui_canvas.create_text(
    1320.0,
    151.0,
    anchor="nw",
    text=max_steps_per_month(april)[0][2],
    fill="#FFFFFF",
    font=("Inter Bold", 11 * -1),
    tags="max_steps_per_month_day"
)

gui_canvas.create_text(
    310.0,
    151.0,
    anchor="nw",
    text="Km Per day",
    fill="#FFFFFF",
    font=("Inter Bold", 10 * -1)
)

gui_canvas.create_text(
    310.0,
    126.0,
    anchor="nw",
    text=round(calculate_travelled_distance(april)/30, 2),
    fill="#D9FFCA",
    font=("Inter Bold", 18 * -1),
    tags="traveled_distance_per_day"
)

gui_canvas.create_text(
    825.0,
    147.0,
    anchor="nw",
    text="Total Calories \n     Burned",
    fill="#FFFFFF",
    font=("Inter Bold", 10 * -1)
)


gui_canvas.create_text(
    835.0,
    125.0,
    anchor="nw",
    text=round(calculate_monthly_average_steps(april)*3, 2),
    fill="#D9FFCA",
    font=("Inter Bold", 20 * -1),
    tags="monthly_calories_burned"
)

#----------------------------------Creating Circular Bar Chart--------------------------------------#
fig_2 = Figure(figsize=(5, 5), facecolor="#917FB3")
ax_2 = fig_2.add_subplot(projection="polar")
ax_2.set_facecolor("#917FB3")
ax_2.bar(x=sales["angles"], height=sales["revenue"], color=sales["colors"])
ax_2.set_frame_on(False)
ax_2.set_xticks([])
ax_2.tick_params(labelsize=2, colors="white")
ax_2.grid(alpha=0.9)

for angle, label, rotation in zip(sales["angles"], sales["products"], sales["rotation"]):
    ax_2.text(x=angle, y=max(sales["revenue"]) + 30, s=label, rotation=rotation, ha="center", va="center", color="white", fontsize=8)

canvas = FigureCanvasTkAgg(figure=fig_2, master=window)
canvas.draw()
canvas.get_tk_widget().place(x=510, y=200)

#----------------------------------------Creating Table---------------------------------------------#
table = ttk.Treeview(master=window, columns=table_columns, show="headings")
for column in table_columns:
    table.heading(column=column, text=column)
    table.column(column=column, width=140)
for row_data in table_list:
    table.insert(parent="", index="end", values=row_data)

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", background="#917FB3", fieldbackground="#917FB3", foreground="white")
style.configure("Treeview.Heading", background="#917FB3", fieldbackground="#917FB3", foreground="white")
style.map("Treeview", background=[("selected", "#E5BEEC")])
table.place(x=1050, y=200, height=500)
#-------------------------------definition of the update chart function----------------------------------#
#------------------------------------Creating Area Chart-------------------------------------------------#
def month_selected_data(selected_month):
    if selected_month == "november":
        selected_data = november
    elif selected_month == "december":
        selected_data = december
    elif selected_month == "january":
        selected_data = january
    elif selected_month == "february":
        selected_data = february
    elif selected_month == "march":
        selected_data = march
    elif selected_month == "april":
        selected_data = april
    return selected_data

#--------------------------------------function update chart---------------------------------------------#
def update_chart(month_data):
    gui_canvas.delete("travelled_distance")
    gui_canvas.create_text(
    145.0,
    136.0,
    anchor="nw",
    text=calculate_travelled_distance(month_data),
    fill="#FFFFFF",
    font=("Inter Bold", 22 * -1),
    tags="travelled_distance"
    )
    
    gui_canvas.delete("calculate_monthly_average_steps")
    gui_canvas.create_text(
    675.0,
    135.0,
    anchor="nw",
    text=calculate_monthly_average_steps(month_data),
    fill="#FFFFFF",
    font=("Inter Bold", 22 * -1),
    tags="calculate_monthly_average_steps"
    )
    
    gui_canvas.delete("max_steps_per_month")
    gui_canvas.create_text(
    1165.0,
    136.0,
    anchor="nw",
    text=max_steps_per_month(month_data)[0][1],
    fill="#FFFFFF",
    font=("Inter Bold", 22 * -1),
    tags="max_steps_per_month"
    )
    
    gui_canvas.delete("max_steps_per_month_date")
    gui_canvas.create_text(
    1320.0,
    126.0,
    anchor="nw",
    text=max_steps_per_month(month_data)[0][3],
    fill="#D9FFCA",
    font=("Inter Bold", 13 * -1),
    tags="max_steps_per_month_date"
    )
    
    gui_canvas.delete("max_steps_per_month_day")
    gui_canvas.create_text(
    1323.0,
    146.0,
    anchor="nw",
    text=max_steps_per_month(month_data)[0][2],
    fill="#FFFFFF",
    font=("Inter Bold", 12 * -1),
    tags="max_steps_per_month_day"
    )
    
    gui_canvas.delete("traveled_distance_per_day")
    gui_canvas.create_text(
    310.0,
    126.0,
    anchor="nw",
    text=round(calculate_travelled_distance(month_data)/30, 2),
    fill="#D9FFCA",
    font=("Inter Bold", 18 * -1),
    tags="traveled_distance_per_day"
    )
    
    gui_canvas.delete("monthly_calories_burned")
    gui_canvas.create_text(
    824.0,
    125.0,
    anchor="nw",
    text=round(calculate_monthly_average_steps(month_data)*3, 2),
    fill="#D9FFCA",
    font=("Inter Bold", 18 * -1),
    tags="monthly_calories_burned"
    )
       
    #update chart    
    revenue_data = pd.DataFrame(month_data)
    revenue_data["DATE"] = pd.to_datetime(month_data["DATE"])

    # Sort the data by the "STEPS" column
    revenue_data = revenue_data.sort_values(by="STEPS")
    
    fig_1 = Figure(figsize=(4.1, 4.2), facecolor="#917FB3")
    ax_1 = fig_1.add_subplot()
    ax_1.set_facecolor("#917FB3")
    ax_1.fill_between(x=revenue_data["DATE"], y1=revenue_data["STEPS"], alpha=0.7)
    ax_1.tick_params(labelsize=7, colors="white")
    fig_1.autofmt_xdate()
    ax_1.bar(revenue_data["DATE"], revenue_data["STEPS"], color="deepskyblue")
    ax_1.grid(visible=False)

    ax_1.set_xlabel("Date", fontsize=10, color="white")  # X-axis label
    ax_1.set_ylabel("Steps", fontsize=10, color="white")  # Y-axis label
    ax_1.set_title("Monthly Steps Chart", fontsize=12, color="white")  # Title

    canvas = FigureCanvasTkAgg(figure=fig_1, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=55, y=260)

update_chart(april)

# Define a callback function to update the chart
def update_chart_selected_month(*args):
    selected_month = dropdown_var.get()
    # Call update_chart with the selected month data
    update_chart(month_selected_data(selected_month))
#----------------------------------------Create dropdown menu for selecting month-----------------------------------#
#--------------------------------------return the data for the month selected by user-------------------------------#
#---------------------------------Function to update the chart based on the selected month--------------------------#
select_month = Label(window, text="Select Month ",bg="#917FB3", fg="white", font=("Inter Bold", 12))
select_month.place(x=220,y=230)
#---------------------------------------------the above code is work correctly--------------------------------------#
months = ["november", "december", "january", "february", "march", "april"]
dropdown_var =StringVar(window)
dropdown_var.set(months[-1])  # Set default value
dropdown_menu = OptionMenu(window,dropdown_var, *months )
dropdown_menu.config(background="#917FB3",font=("Inter Bold", 12))
dropdown_menu.place(x=350, y=230)

#-------------------------------------Attach the callback function to the dropdown menu-----------------------------#
dropdown_var.trace_add("write", update_chart_selected_month)
window.mainloop()
