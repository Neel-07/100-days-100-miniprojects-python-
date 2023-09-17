import calendar

# Input month and year
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

# Create a calendar object
cal = calendar.month(year, month)

# Display the calendar
print(f"Calendar for {calendar.month_name[month]} {year}:\n")
print(cal) 