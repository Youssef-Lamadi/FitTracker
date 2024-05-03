#-----------------------------------------read the csv files useing numpy--------------------------------------------------#
import numpy as np
from collections import defaultdict
from datetime import datetime
import os 
# Define the filenames
filenames = [os.path.join(os.path.dirname(__file__),"daily_steps_november21.csv"), os.path.join(os.path.dirname(__file__),"daily_steps_december21.csv"), 
             os.path.join(os.path.dirname(__file__),"daily_steps_january22.csv"), os.path.join(os.path.dirname(__file__),"daily_steps_february22.csv"), 
             os.path.join(os.path.dirname(__file__),"daily_steps_march22.csv"), os.path.join(os.path.dirname(__file__),"daily_steps_april22.csv")]

# Initialize dictionaries for each month
november = {"DAY": [], "DATE": [], "STEPS": []}
december = {"DAY": [], "DATE": [], "STEPS": []}
january = {"DAY": [], "DATE": [], "STEPS": []}
february = {"DAY": [], "DATE": [], "STEPS": []}
march = {"DAY": [], "DATE": [], "STEPS": []}
april = {"DAY": [], "DATE": [], "STEPS": []}

# Loop through each file
for filename in filenames:
    # Read the CSV file using numpy
    data = np.genfromtxt(filename, delimiter=',', dtype=str, skip_header=1)
    days, dates, steps = np.hsplit(data, 3)
    
    # Add data to the corresponding dictionary
    if "november" in filename.lower():
        november["DAY"].extend(days.flatten())
        november["DATE"].extend(dates.flatten())
        november["STEPS"].extend(steps.flatten())
    elif "december" in filename.lower():
        december["DAY"].extend(days.flatten())
        december["DATE"].extend(dates.flatten())
        december["STEPS"].extend(steps.flatten())
    elif "january" in filename.lower():
        january["DAY"].extend(days.flatten())
        january["DATE"].extend(dates.flatten())
        january["STEPS"].extend(steps.flatten())
    elif "february" in filename.lower():
        february["DAY"].extend(days.flatten())
        february["DATE"].extend(dates.flatten())
        february["STEPS"].extend(steps.flatten())
    elif "march" in filename.lower():
        march["DAY"].extend(days.flatten())
        march["DATE"].extend(dates.flatten())
        march["STEPS"].extend(steps.flatten())
    elif "april" in filename.lower():
        april["DAY"].extend(days.flatten())
        april["DATE"].extend(dates.flatten())
        april["STEPS"].extend(steps.flatten())
        
#------------------------travelled distance-------------------------------------#
def calculate_travelled_distance(data):
    total_distance = 0
    
    # Extract the month name from the first date entry
    month_name = data['DATE'][0].split('/')[0]
    
    # Iterate over the data
    for i in range(len(data['DATE'])):
        date = data['DATE'][i]
        steps = int(data['STEPS'][i])
        
        # Calculate distance for each day
        distance = steps * 0.75
        
        # Accumulate total distance for the given month
        if date.startswith(month_name):
            total_distance += distance
            
    # Return the total distance for the given month
    total_distance = total_distance / 1000
    return round(total_distance, 2)

#---------------------------monthly steps average------------------------------#
def calculate_monthly_average_steps(data):
    # Dictionary to store total steps and number of days for each month
    monthly_steps = defaultdict(int)
    monthly_days = defaultdict(int)
    
    # Extract data
    dates = data['DATE']
    steps = data['STEPS']
    
    # Convert steps to integers
    steps = [int(step) for step in steps]
    
    # Iterate over the data
    for date_str, step in zip(dates, steps):
        # Parse date string to extract month
        date = datetime.strptime(date_str, '%m/%d/%Y')
        month = date.month
        
        # Update total steps and number of days for the month
        monthly_steps[month] += step
        monthly_days[month] += 1
    
    # Calculate daily averages for each month
    monthly_avg_steps = {month: monthly_steps[month] / monthly_days[month] for month in monthly_steps}
    
    # Calculate overall monthly average
    overall_monthly_avg = sum(monthly_avg_steps.values()) / len(monthly_avg_steps)
    
    return round(overall_monthly_avg, 2)

#-------------------------------max steps per day in the month----------------------------------#
def max_steps_per_month(data):
    # List to store max steps info for each month
    max_steps_list = []
    
    # Extract data
    days = data['DAY']
    dates = data['DATE']
    steps = data['STEPS']
    
    # Convert steps to integers
    steps = [int(step) for step in steps]
    
    # Dictionary to store max steps, day, and date for each month
    max_steps_info = {}
    
    # Iterate over the data
    for date_str, day, step in zip(dates, days, steps):
        # Parse date string to extract month
        date = datetime.strptime(date_str, '%m/%d/%Y')
        month = date.month
        
        # If month is not already in the dictionary, initialize it
        if month not in max_steps_info:
            max_steps_info[month] = {'max_steps': 0, 'day': '', 'date': ''}
        
        # Update max steps if current step is greater
        if step > max_steps_info[month]['max_steps']:
            max_steps_info[month]['max_steps'] = step
            max_steps_info[month]['day'] = day
            max_steps_info[month]['date'] = date_str
    
    # Convert max_steps_info to a list
    for month, info in max_steps_info.items():
        max_steps_list.append((month, f"{info['max_steps']:.2f}", info['day'], info['date']))
    
    return max_steps_list

#--------------------------convert steps into distance in kilometer--------------------------------#
def travelled_distance(steps):
    nbr_steps = float(steps)
    distance_in_km = nbr_steps * 0.00075
    return "{:.2f}".format(distance_in_km)

#-------------for the table--------------#
def dict_to_list_of_lists(data_dict):
    list_of_lists = []
    for i in range(len(data_dict["DAY"])):
        sublist = [data_dict["DAY"][i], data_dict["DATE"][i], data_dict["STEPS"][i]]
        list_of_lists.append(sublist)
    return list_of_lists

#-------------------Convert april (default) dictionary to list of lists---------------------------#
table_columns = ["Day", "Date", "Steps"]
table_data = []
november_list = dict_to_list_of_lists(november)
table_data.extend(november_list)
december_list = dict_to_list_of_lists(december)
table_data.extend(december_list)
january_list = dict_to_list_of_lists(january)
table_data.extend(january_list)
february_list = dict_to_list_of_lists(february)
table_data.extend(february_list)
march_list = dict_to_list_of_lists(march)
table_data.extend(march_list)
april_list = dict_to_list_of_lists(april)
table_data.extend(april_list)
table_list = table_data







































# read the data from csv file and transfer it into python dictionnary
november = {
  "DAY": [],
  "DATE": [],
  "STEPS": []
}

# Split the CSV data into lines
lines = [line.strip() for line in open(os.path.join(os.path.dirname(__file__),"daily_steps_november21.csv")).readlines()]  # Replace "your_data.csv" with your actual file path

# Skip the header row (assuming the first row contains column names)
header = lines.pop(0).split(",")

# Add data from remaining lines to the dictionary
for line in lines:
  values = line.split(",")
  for i, value in enumerate(values):
    november[header[i]].append(value)


table_columns = ["Day", "Date", "Steps"]
table_data = []

for i in range(len(november['DAY'])):
    row = [ november['DAY'][i], november['DATE'][i], november['STEPS'][i]]
    table_data.append(row)

# Sales data
sales = {
    "revenue": [472 ,356,278, 412, 550, 672],
    "products": ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5", "Product 6"],
    "angles": [0, 1.04719, 2.094395, 3.141592, 4.18879, 5.23598],
    "rotation": [-90, -30, 30, 90, 330, 390, 450],
    "colors": ["#439A97", "#56a8a5", "#6cbdba", "#12b2ed", "#008fc4", "#0a7ca6"]
}

# #### remember to delete this part of code #################
# # Revenue data
# revenue = { 
#     "date": [
#         "2022-08-19",
#         "2022-08-20",
#         "2022-08-23",
#         "2022-08-24",
#         "2022-08-25",
#         "2022-08-26",
#         "2022-08-27",
#         "2022-08-30",
#         "2022-08-31",
#         "2022-09-01",
#         "2022-09-02",
#         "2022-09-03",
#         "2022-09-07",
#         "2022-09-08",
#         "2022-09-09",
#         "2022-09-10",
#         "2022-09-13",
#         "2022-09-14",
#         "2022-09-15",
#         "2022-09-16",
#         "2022-09-17",
#         "2022-09-20",
#         "2022-09-21",
#         "2022-09-22",
#         "2022-09-23",
#         "2022-09-24",
#         "2022-09-27",
#         "2022-09-28",
#         "2022-09-29",
#         "2022-09-30",
#         "2022-10-01",
#         "2022-10-04",
#         "2022-10-05",
#         "2022-10-06",
#         "2022-10-07",
#         "2022-10-08",
#         "2022-10-11",
#         "2022-10-12",
#         "2022-10-13",
#         "2022-10-14",
#         "2022-10-15",
#         "2022-10-18",
#         "2022-10-19",
#         "2022-10-20",
#         "2022-10-21",
#         "2022-10-22",
#         "2022-10-25",
#         "2022-10-26",
#         "2022-10-27",
#         "2022-10-28",
#         "2022-10-29",
#         "2022-11-01",
#         "2022-11-02",
#         "2022-11-03",
#         "2022-11-04",
#         "2022-11-05",
#         "2022-11-08",
#         "2022-11-09",
#         "2022-11-10",
#         "2022-11-11",
#         "2022-11-12",
#         "2022-11-15",
#         "2022-11-16",
#         "2022-11-17",
#         "2022-11-18",
#         "2022-11-19",
#         "2022-11-22",
#         "2022-11-23",
#         "2022-11-24",
#         "2022-11-26",
#         "2022-11-29",
#         "2022-11-30",
#         "2022-12-01",
#         "2022-12-02",
#         "2022-12-03",
#         "2022-12-06",
#         "2022-12-07",
#         "2022-12-08",
#         "2022-12-09",
#         "2022-12-10",
#         "2022-12-13",
#         "2022-12-14",
#         "2022-12-15",
#         "2022-12-16",
#         "2022-12-17",
#         "2022-12-20",
#         "2022-12-21",
#         "2022-12-22",
#         "2022-12-23",
#         "2022-12-27",
#         "2022-12-28",
#         "2022-12-29",
#         "2022-12-30",
#         "2022-12-31",
#         "2023-01-03",
#         "2023-01-04",
#         "2023-01-05",
#         "2023-01-06",
#         "2023-01-07",
#         "2023-01-10",
#         "2023-01-11",
#         "2023-01-12",
#         "2023-01-13",
#         "2023-01-14",
#         "2023-01-18",
#         "2023-01-19",
#         "2023-01-20",
#         "2023-01-21",
#         "2023-01-24",
#         "2023-01-25",
#         "2023-01-26",
#         "2023-01-27",
#         "2023-01-28",
#         "2023-01-31",
#         "2023-02-01",
#         "2023-02-02",
#         "2023-02-03",
#         "2023-02-04",
#         "2023-02-07",
#         "2023-02-08",
#         "2023-02-09",
#         "2023-02-10",
#         "2023-02-11",
#         "2023-02-14",
#         "2023-02-15",
#         "2023-02-16",
#         "2023-02-17",
#         "2023-02-18",
#         "2023-02-22",
#         "2023-02-23",
#         "2023-02-24",
#         "2023-02-25",
#         "2023-02-28",
#         "2023-03-01",
#         "2023-03-02",
#         "2023-03-03",
#         "2023-03-04",
#         "2023-03-07",
#         "2023-03-08",
#         "2023-03-09",
#         "2023-03-10",
#         "2023-03-11",
#         "2023-03-14",
#         "2023-03-15",
#         "2023-03-16",
#         "2023-03-17",
#         "2023-03-18",
#         "2023-03-21",
#         "2023-03-22",
#         "2023-03-23",
#         "2023-03-24",
#         "2023-03-28",
#         "2023-03-29",
#         "2023-03-30",
#         "2023-03-31",
#         "2023-04-01",
#         "2023-04-04",
#         "2023-04-05",
#         "2023-04-06",
#         "2023-04-07",
#         "2023-04-08",
#         "2023-04-11",
#         "2023-04-12",
#         "2023-04-13",
#         "2023-04-14",
#         "2023-04-15",
#         "2023-04-18",
#         "2023-04-19",
#         "2023-04-20",
#         "2023-04-21",
#         "2023-04-22",
#         "2023-04-25",
#         "2023-04-26",
#         "2023-04-27",
#         "2023-04-28",
#         "2023-04-29",
#         "2023-05-02",
#         "2023-05-03",
#         "2023-05-04",
#         "2023-05-05",
#         "2023-05-06",
#         "2023-05-09",
#         "2023-05-10",
#         "2023-05-11",
#         "2023-05-12",
#         "2023-05-13",
#         "2023-05-16",
#         "2023-05-17",
#         "2023-05-18",
#         "2023-05-19",
#         "2023-05-20",
#         "2023-05-23",
#         "2023-05-24",
#         "2023-05-25",
#         "2023-05-26",
#         "2023-05-27",
#         "2023-05-31",
#         "2023-06-01",
#         "2023-06-02",
#         "2023-06-03",
#         "2023-06-06",
#         "2023-06-07",
#         "2023-06-08",
#         "2023-06-09",
#         "2023-06-10",
#         "2023-06-13",
#         "2023-06-14",
#         "2023-06-15",
#         "2023-06-16",
#         "2023-06-17",
#         "2023-06-20",
#         "2023-06-21",
#         "2023-06-22",
#         "2023-06-23",
#         "2023-06-24",
#         "2023-06-27",
#         "2023-06-28",
#         "2023-06-29",
#         "2023-06-30",
#         "2023-07-01",
#         "2023-07-05",
#         "2023-07-06",
#         "2023-07-07",
#         "2023-07-08",
#         "2023-07-11",
#         "2023-07-12",
#         "2023-07-13",
#         "2023-07-14",
#         "2023-07-15",
#         "2023-07-18",
#         "2023-07-19",
#         "2023-07-20",
#         "2023-07-21",
#         "2023-07-22",
#         "2023-07-25",
#         "2023-07-26",
#         "2023-07-27",
#         "2023-07-28",
#         "2023-07-29",
#         "2023-08-01",
#         "2023-08-02",
#         "2023-08-03",
#         "2023-08-04",
#         "2023-08-05",
#         "2023-08-08",
#         "2023-08-09",
#         "2023-08-10",
#         "2023-08-11",
#         "2023-08-12",
#         "2023-08-15",
#         "2023-08-16",
#         "2023-08-17",
#         "2023-08-18",
#         "2023-08-19",
#         "2023-08-22",
#         "2023-08-23",
#         "2023-08-24",
#         "2023-08-25",
#         "2023-08-26",
#         "2023-08-29",
#         "2023-08-30",
#         "2023-08-31",
#     ],
#     "amount": [
#         105.73,
#         107.15,
#         107.04,
#         106.23,
#         105.52,
#         104.61,
#         102.7,
#         101.54,
#         101.04,
#         100.84,
#         101.35,
#         101.55,
#         102.88,
#         104.36,
#         106.66,
#         109.08,
#         111.24,
#         113.74,
#         115.7,
#         117.16,
#         118.27,
#         119.1,
#         119.22,
#         119.32,
#         121.44,
#         124.01,
#         126.45,
#         130.03,
#         132.08,
#         133.9,
#         135.77,
#         137.34,
#         138.01,
#         137.23,
#         137.31,
#         137.82,
#         138.89,
#         141.1,
#         144.04,
#         145.8,
#         145.43,
#         146.74,
#         152.56,
#         162.43,
#         172.75,
#         181.9,
#         187.12,
#         187.93,
#         191.48,
#         193.71,
#         193.3,
#         191.82,
#         185.15,
#         179.57,
#         173.82,
#         169.62,
#         173.03,
#         175.4,
#         179.44,
#         180.61,
#         177.98,
#         174.36,
#         170.49,
#         168.64,
#         167.39,
#         169.2,
#         171.69,
#         175.68,
#         179.3,
#         180.6,
#         180.6,
#         180.44,
#         179.01,
#         176.88,
#         174.52,
#         172.78,
#         171.62,
#         171.38,
#         173.56,
#         175.14,
#         176.35,
#         178.76,
#         180.34,
#         181.33,
#         183.79,
#         185.74,
#         187.46,
#         189.72,
#         191.37,
#         193.79,
#         194.01,
#         196.5,
#         196.9,
#         195.88,
#         194.82,
#         192.6,
#         192.74,
#         192.75,
#         194.46,
#         194.83,
#         196.06,
#         198.64,
#         199.12,
#         198.77,
#         195.85,
#         190.06,
#         185.01,
#         183.84,
#         183.79,
#         186.2,
#         190.82,
#         191.48,
#         195.96,
#         201.08,
#         203.27,
#         204.3,
#         202.47,
#         197.65,
#         193.56,
#         191.4,
#         189.99,
#         190.9,
#         193.51,
#         196.13,
#         197.37,
#         196.41,
#         195.29,
#         193.04,
#         190.02,
#         189.18,
#         187.2,
#         186.28,
#         186.56,
#         186.04,
#         186.73,
#         186.73,
#         185.32,
#         183.84,
#         181.08,
#         178.53,
#         177.84,
#         176.75,
#         177.12,
#         178.38,
#         178.95,
#         179.7,
#         179.62,
#         179.43,
#         179.56,
#         179.8,
#         180.17,
#         180.49,
#         180.14,
#         181.57,
#         183.6,
#         185.78,
#         189.21,
#         190.9,
#         192.06,
#         193.25,
#         193.04,
#         192.89,
#         190.83,
#         189.09,
#         188.7,
#         190.37,
#         195.17,
#         202.38,
#         210.42,
#         215.58,
#         219.47,
#         220.38,
#         219.5,
#         220.38,
#         221.98,
#         224.24,
#         225.99,
#         227.42,
#         227.38,
#         227.2,
#         228.28,
#         228.46,
#         229.26,
#         230.08,
#         230.54,
#         233.14,
#         235.63,
#         238.27,
#         243.85,
#         248.06,
#         253.47,
#         257.86,
#         260.5,
#         265.82,
#         272.62,
#         279.79,
#         283.36,
#         286.77,
#         288.05,
#         285.97,
#         287.48,
#         285.37,
#         282.78,
#         282.48,
#         279.6,
#         278.34,
#         277.72,
#         279.81,
#         283.07,
#         286.03,
#         288.39,
#         291.02,
#         295.09,
#         298.26,
#         299.02,
#         298.24,
#         295.03,
#         293.46,
#         293.16,
#         293.5,
#         294.75,
#         294.16,
#         294.23,
#         295.06,
#         296.22,
#         298.18,
#         300.12,
#         302.88,
#         305.66,
#         308.85,
#         309.56,
#         306.05,
#         302.07,
#         297.82,
#         295.59,
#         293.57,
#         292.45,
#         293.02,
#         293.96,
#         296.46,
#         296.64,
#         294.66,
#         293.23,
#         290.21,
#         288.14,
#         287.76,
#         285.86,
#         285.86,
#         286.12,
#         283.68,
#         282.68,
#         279.77,
#         278.4,
#         279.04,
#         279.69,
#         282.08,
#         284.3,
#         285.47,
#         286.32,
#         286.99,
#         286.99,
#         286.95,
#     ]
# }

# # Sales data
# sales = {
#     "revenue": [472 ,356,278, 412, 550, 672],
#     "products": ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5", "Product 6"],
#     "angles": [0, 1.04719, 2.094395, 3.141592, 4.18879, 5.23598],
#     "rotation": [-90, -30, 30, 90, 330, 390, 450],
#     "colors": ["#439A97", "#56a8a5", "#6cbdba", "#12b2ed", "#008fc4", "#0a7ca6"]
# }

