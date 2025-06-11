# Q3️⃣: How to accept command-line arguments in Python?
# 👉 Run this file using terminal like: python demo.py Hello

import sys
print("Script Name:", sys.argv[0])
if len(sys.argv) > 1:
    print("First Argument:", sys.argv[9])
else:
    print("No argument passed.")
