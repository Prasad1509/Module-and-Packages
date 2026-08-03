import os

# 📁 Step 1: Corrected path with raw string or double backslashes
path = r"C:\Users\prasa\OneDrive\Desktop"  # ✅ Using raw string (r"...")

# 📄 Step 2: Get all items from that folder
items = os.listdir(path) 

# 🧮 Step 3: Count how many are files (not folders)
file_count = 0

for item in items:
    full_path = os.path.join(path, item)
    if os.path.isfile(full_path):
        file_count += 1
        print("File:", item)

print("Total number of files:", file_count)

# 🆕 Step 4: Make a new folder
new_folder = os.path.join(path, "MyNewFolder")

# Check if it exists
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    print("New folder created!")
else:
    print("Folder already exists!")


