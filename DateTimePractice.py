# 📦 Import necessary modules
import datetime
import calendar
from datetime import timedelta

# 🔢 Q1. Print the current date and time
now = datetime.datetime.now()
print("Q1. Current date and time:", now)
# now() returns current date and time like: 2025-05-31 19:20:12.123456

# 🔢 Q2. Extract only the date (without time)
today = datetime.date.today()
print("Q2. Only date:", today)
# date.today() gives today's date only

# 🔢 Q3. Get yesterday’s and tomorrow’s date
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Q3. Yesterday:", yesterday)
print("Q3. Today:", today)
print("Q3. Tomorrow:", tomorrow)
# timedelta is used to move back/forward in days

# 🔢 Q4. Create a custom date: 15 August 1947
independence_day = datetime.date(1947, 8, 15)
print("Q4. Indian Independence Day:", independence_day)
# Custom date with date(year, month, day)

# 🔢 Q5. Format today’s date as "31-May-2025"
formatted = today.strftime("%d-%b-%Y")
print("Q5. Formatted date:", formatted)
# %d = day, %b = month short name, %Y = year

# 🔢 Q6. Convert string "25-12-2024" to a date
date_str = "25-12-2024"
converted = datetime.datetime.strptime(date_str, "%d-%m-%Y")
print("Q6. Converted date:", converted)
# strptime converts string to datetime object

# 🔢 Q7. Calculate number of days between today and 1 June 2025
future_date = datetime.date(2025, 6, 1)
diff = future_date - today
print("Q7. Days left until 1 June 2025:", diff.days)
# Subtracting two dates gives a timedelta object

# 🔢 Q8. What day of the week is today?
weekday = today.strftime("%A")
print("Q8. Today is:", weekday)
# %A = full weekday name

# 🔢 Q9. Display current time in 12-hour format
formatted_time = now.strftime("%I:%M %p")
print("Q9. Current time (12-hour format):", formatted_time)
# %I = 12-hour, %M = minutes, %p = AM/PM

# 🔢 Q10. Check if a given year is a leap year
year = 2005
is_leap = calendar.isleap(year)
print("Q10. Is year", year, "a leap year?", is_leap)
# calendar.isleap() returns True or False

