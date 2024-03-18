# Adding special characters in Python
# Random Password Generator Example

# Import relevant modules
import random

# Imports special characters, i.e punctuation
from string import punctuation

# Create a list with all these special characters in
special_chars = list(punctuation)

print(len(special_chars))  # There are 32 elements in the list!

# Example - Random Password Generator WITH special characters
password = ''
for i in range(5):
    # Produces a random uppercase character/letter
    a = chr(random.randint(65, 90))
    # Produces a random lowercase character/letter
    b = chr(random.randint(65, 90)).lower()
    # Produce a special character
    c = special_chars[random.randint(0, 31)]
    password = password + a + b + c

print(password)

# Shuffle the password you have - doesn't follow uppercase,
# lowercase, special character structure.

print(''.join(random.sample(password, len(password))))




