import csv
import os
from collections import defaultdict

# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Path to the CSV file relative to the script
csv_file_path = os.path.join(current_directory, 'sleepdata.csv')

# Initialize a dictionary of lists
sleepdata= defaultdict(list)

# Open the CSV file and read its contents
with open(csv_file_path, newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.DictReader(csvfile, delimiter=';')
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Iterate over each column in the row
        for column, value in row.items():
            # Append the value to the corresponding list in the dictionary
            sleepdata[column].append(value) 

def get_sleep_data_for_month(sleepdata, month):
    month_data = {"Start": [], "End": [], "Sleep quality": [], "Time in bed": [], "Wake up": [], "Sleep Notes": [], "Heart rate": [], "Activity (steps)": []}
    
    for start, end, quality, time, wakeup, notes, heart_rate, steps in zip(
        sleepdata["Start"], 
        sleepdata["End"], 
        sleepdata["Sleep quality"], 
        sleepdata["Time in bed"], 
        sleepdata["Wake up"], 
        sleepdata["Sleep Notes"], 
        sleepdata["Heart rate"], 
        sleepdata["Activity (steps)"]
    ):
        if start.startswith(month) or end.startswith(month):
            month_data["Start"].append(start)
            month_data["End"].append(end)
            month_data["Sleep quality"].append(quality)
            month_data["Time in bed"].append(time)
            month_data["Wake up"].append(wakeup)
            month_data["Sleep Notes"].append(notes)
            month_data["Heart rate"].append(heart_rate)
            month_data["Activity (steps)"].append(steps)
    
    return month_data

# Example usage:
month_data = get_sleep_data_for_month(sleepdata, "2018-02")

#-------------------------function calculate Asleep Average-----------------------------#
def asleep_average(sleepdata):
    total_minutes = 0
    num_entries = 0
    
    for time_in_bed in sleepdata["Time in bed"]:
        if time_in_bed:
            hours, minutes = map(int, time_in_bed.split(":"))
            total_minutes += hours * 60 + minutes
            num_entries += 1
    
    if num_entries == 0:
        return "0 hr 0 min"
    
    average_minutes = total_minutes / num_entries
    average_hours = int(average_minutes / 60)
    average_minutes = int(average_minutes % 60)
    
    return f"{average_hours} hr {average_minutes} min"
#usage:
average_sleep_time = asleep_average(month_data)

#--------------------function calculate the total sleep quality for month <<month_data>>---------------#
def calculate_monthly_sleep_quality(month_data):
    total_quality = 0
    total_entries = 0

    for quality in month_data["Sleep quality"]:
        try:
            quality_value = int(quality.strip('%'))
            total_quality += quality_value
            total_entries += 1
        except ValueError:
            pass  # Skip invalid quality values

    if total_entries == 0:
        return None  # No valid sleep quality data found for the month
    else:
        average_quality = total_quality / total_entries
        return "{:.2f}%".format(average_quality)

monthly_average_sleep_quality = calculate_monthly_sleep_quality(month_data)

#----------------------------function calculate the heart rate average--------------------------------#
def calculate_heart_rate_average(month_data):
    heart_rates = [int(rate) for rate in month_data['Heart rate'] if rate.isdigit()]
    if heart_rates:
        return "{:.2f}".format(sum(heart_rates) / len(heart_rates))
    else:
        return "No data found"

#--------------------------------function return the steps average-----------------------------------#
def calculate_monthly_steps_average(month_data):
    steps = [int(step) for step in month_data['Activity (steps)'] if step.isdigit()]
    if steps:
        return "{:.2f}".format(sum(steps) / len(steps))
    else:
        return "No data found"
    
#-----------------------------convert steps into distance in kilometer--------------------------------#
def steps_to_km(steps):
    # Assuming one step is approximately equal to 0.75 meters (0.00075 kilometers)
    if steps == "No data found":
        return 0.00
    nbr_steps = float(steps)
    distance_in_km = nbr_steps * 0.00075
    return "{:.2f}".format(distance_in_km)

#------------------convert the csv file into list of lists for the table chart--------------------------#

#----------------------Initialize table_columns with the desired column names---------------------------#
table_columns = ["Start", "End", "Sleep quality", "Time in bed", "Wake up", "Sleep Notes", "Heart rate", "Activity (steps)"]

#-------------------------Initialize an empty list to store the table data------------------------------#
table_data = []
#-----------------------------Open the CSV file and read its contents-----------------------------------#
with open(csv_file_path, newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.DictReader(csvfile, delimiter=';')
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Create a list containing values for each column in the row
        row_data = [row[column] for column in table_columns]
        
        # Append the row data to the table data list
        table_data.append(row_data)
