# Ask user for day
day_leave_str = input("What day are you leaving?(0-6)")
holiday_length_str = input("How long is you stay? (In days)")

# Change to int
day_leave_int = int(day_leave_str)
holiday_length_int = int(holiday_length_str)

# Convert
day = day_leave_int + holiday_length_int
return_day = day % 7
# output
print("You will return on day", return_day)
