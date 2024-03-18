# How to shuffle a string

# Import relevant modules
import random

string = "animalanimalbananaapplegrapefruit"

shuffled_string = "".join(random.sample(string, len(string)))

print(shuffled_string)