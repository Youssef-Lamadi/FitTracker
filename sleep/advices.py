import numpy as np
import random

# Create a list using NumPy
my_list = np.array([
    "Experts recommend that adults sleep between 7 and 9 hours a night.\n Adults who sleep less than 7 hours a night may have more health issues than those who sleep 7 or more hours a night.",
    "A healthy adult usually needs around 7 to 9 hours of sleep.",
    "How sustainable is 5 hours of sleep? Experts recommend adults get at least 7 hours of sleep per night for better health.\n Consistently getting less than 5 hours of sleep can have adverse effects on physical and mental health.\n Inadequate sleep can impact memory, mood, concentration, immunity, and overall quality of life.",
    "What are sleep restrictions? Sleep restriction therapy is a common feature of virtually all types of cognitive behavior therapy for insomnia (CBTi).\n It aims to address difficulty staying asleep through reverse logic.\n Limiting the amount of time spent in bed can actually help those struggling with sleeplessness to sleep better.",
    "Can you survive on 4 hours of sleep? You may be able to survive on four hours of sleep, but you probably won't be even close to thriving.\nIt aims to address difficulty staying asleep through reverse logic.\nLimiting the amount of time spent in bed can actually help those struggling with sleeplessness to sleep better.",
    "Why do adults need less sleep? Sleep and Aging: Why Sleep Gets Worse As You Age As we age,\nour energy levels naturally decline due to changes in metabolism and hormone production, \nwhich can cause us to need fewer hours of sleep than when we were younger. \nSo, older people may require slightly less sleep compared to when they were younger, but not significantly less.",
    "The importance of sleep for overall well-being cannot be overstated.",
    "What is REM sleep and why is it important? REM (rapid eye movement) sleep is a stage of sleep characterized by rapid eye movements,\nincreased brain activity, and vivid dreaming.\nIt is believed to play a crucial role in memory consolidation and emotional regulation.",
    "Tips for improving sleep quality: Maintain a consistent sleep schedule. \nCreate a relaxing bedtime routine. Make sure your sleep environment is comfortable and conducive to sleep. \nLimit exposure to screens and bright lights before bedtime.",
    "The effects of sleep deprivation can include impaired cognition, mood disturbances,\nand increased risk of accidents.",
    "A normal resting heart rate should be between 60 to 100 beats per minute, but it can vary from minute to minute.\nYour age and general health can also affect your pulse rate, so it's important to remember that a 'normal' \npulse can vary from person to person."
])
def get_random_string():
    # Convert NumPy array to a Python list
    my_list_python = my_list.tolist()
    # Randomly select a string from the list
    random_string = random.choice(my_list_python)
    return random_string

