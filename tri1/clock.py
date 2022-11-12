# ask the user for the time in hours
print("What is the current time in hours?")
current_tine_string = input()

# ask the user how many to wait
print("How many hours do you have to wait?")
waiting_time_string = input()

# change to int
current_time_int = int(current_tine_string)
waiting_time_int = int(waiting_time_string)

# figure out the hours and convert to regular tine
hours = current_time_int + waiting_time_int
timeofday = hours % 24
print(timeofday)