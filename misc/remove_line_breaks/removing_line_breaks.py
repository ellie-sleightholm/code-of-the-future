# Import relevant modules
import pyautogui
import time

# Let the python file sleep for 3 seconds
time.sleep(3)

# Open a text file
text = open('text.txt')

# Create a new string with NO line breaks - this will write
# an entire paragraph and not each line separately
text_no_line_breaks = ''
for each_line in text:
    # Remove the line break at the end of the line
    stripped_line = each_line.rstrip()
    # add this to the new string
    text_no_line_breaks += stripped_line

pyautogui.write(text_no_line_breaks)

