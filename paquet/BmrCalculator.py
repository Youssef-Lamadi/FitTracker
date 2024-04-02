import tkinter as tk


def calculate_bmr():
    # Get values from entries
    weight_str = weight_entry.get()
    height_cm_str = height_cm_entry.get()
    age_str = age_entry.get()

    # Convert values to numbers
    try:
        weight = float(weight_str)
        height_cm = float(height_cm_str)
        age = int(age_str)
    except ValueError:
        # Handle invalid input
        result_label.config(text="Invalid input. Please enter numbers only.")
        return

    # Calculate BMR using the Harris-Benedict equation
    if gender_var.get() == "Male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height_cm) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height_cm) - (4.330 * age)

    # Display the result
    result_label.config(text=f"Your BMR is: {bmr:.2f} calories per day")


# Create main window
window = tk.Tk()
window.title("BMR Calculator")


def position_window():
    window_width = window.winfo_reqwidth()
    window_height = window.winfo_reqheight()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = screen_width - window_width
    y = screen_height - window_height

    window.geometry(f"300x300+{x - 300}+{y - 300}")  # Adjusting position to be 300 pixels to the left and 300 pixels up


position_window()

# Create a frame within the main window with a border and orange header
frame = tk.Frame(window, bg="lightgrey", bd=2, relief="raised")
frame.place(relx=1, rely=1, anchor="se", x=-5, y=-5)

# Add a title to the frame
frame_title = tk.Label(frame, text="BMR Calculator", bg="orange", fg="white", padx=10)
frame_title.pack(fill="x")

# Create a subframe for input fields
input_frame = tk.Frame(frame, bg="lightgrey")
input_frame.pack(padx=10, pady=(10, 0), fill="both", expand=True)

# Create labels and entries for weight, height, and age
weight_label = tk.Label(input_frame, text="Weight (kg):", bg="lightblue")
weight_label.pack(side="top", pady=(5, 2))
weight_entry = tk.Entry(input_frame)
weight_entry.pack(side="top", pady=(0, 5))
height_cm_label = tk.Label(input_frame, text="Height (cm):", bg="lightblue")
height_cm_label.pack(side="top", pady=(5, 2))
height_cm_entry = tk.Entry(input_frame)
height_cm_entry.pack(side="top", pady=(0, 5))
age_label = tk.Label(input_frame, text="Age:", bg="lightblue")
age_label.pack(side="top", pady=(5, 2))
age_entry = tk.Entry(input_frame)
age_entry.pack(side="top", pady=(0, 5))

# Create a subframe for gender selection
gender_frame = tk.Frame(frame, bg="lightgrey")
gender_frame.pack(padx=10, pady=5, fill="both", expand=True)

# Create a radio button for gender selection
gender_var = tk.StringVar(value="Male")
male_radio = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg="lightblue")
male_radio.pack(side="left")
female_radio = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg="lightblue")
female_radio.pack(side="left")

# Create a subframe for buttons
button_frame = tk.Frame(frame, bg="lightgrey")
button_frame.pack(padx=10, pady=(0, 10), fill="both", expand=True)

# Create buttons for calculation and reset
calculate_button = tk.Button(button_frame, text="Calculate", command=calculate_bmr, bg="lightgreen")
calculate_button.pack(side="left", padx=(0, 5))
reset_button = tk.Button(button_frame, text="Reset", command=lambda: [entry.delete(0, tk.END) for entry in
                                                                      (weight_entry, height_cm_entry, age_entry)],
                         bg="salmon")
reset_button.pack(side="left")

# Create a label to display the result
result_label = tk.Label(frame, text="", bg="lightyellow")
result_label.pack(pady=(5, 10))

window.mainloop()