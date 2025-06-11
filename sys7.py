# Q7️⃣: How to see which modules are currently loaded?
import sys
print("First 10 loaded modules:")
print(list(sys.modules.keys())[:19])
