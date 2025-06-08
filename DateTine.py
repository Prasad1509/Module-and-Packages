# 📦 Import datetime module
import datetime

# 1️⃣ Get current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# 2️⃣ Get individual parts from the current date and time
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# 3️⃣ Create a custom date and time
# Format: datetime(year, month, day, hour, minute)
custom_date = datetime.datetime(2024, 12, 25, 10, 30)
print("Custom date and time:", custom_date)

# 4️⃣ Format current date/time as string (e.g., 31-05-2025 18:30:00)
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted date and time:", formatted)

# 5️⃣ Find the number of days between two dates
date1 = datetime.date(2025, 6, 10)
date2 = datetime.date(2025, 5, 31)
difference = date1 - date2
print("Days between:", difference.days)

# 6️⃣ Add or subtract days using timedelta
from datetime import timedelta

today = datetime.date.today()
print("Today:", today)

tomorrow = today + timedelta(days=1)
print("Tomorrow:", tomorrow)

yesterday = today - timedelta(days=1)
print("Yesterday:", yesterday)

# 7️⃣ Convert a string to a date (parse string)
date_str = "01-06-2025"
parsed = datetime.datetime.strptime(date_str, "%d-%m-%Y")
print("Parsed date:", parsed)


