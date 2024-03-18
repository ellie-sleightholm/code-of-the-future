# Timing Python Scripts

# Import relevant modules
import time
from datetime import datetime

# Start of the python script
script_start_time = datetime.now()

# Extra coding...
for i in range(10000000):
    j = 10 + i

# Timing a section of python code
# This gives the start time
start_time = time.time()
# Do some code
for i in range(10000000):
    j = 10 + i
# End time once the code has finished
end_time = time.time()
# Total time
final_time = end_time - start_time
print(final_time)

# Script end time
script_end_time = datetime.now()
print(script_end_time - script_start_time)