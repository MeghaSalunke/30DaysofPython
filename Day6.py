# Day 6 Challenge 6  Importing modules (math, random), creating custom modules
# Generate a random 8-character password

import random
import string

password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
print(password)

#-------------------------------------------------------------------
# Using User Input 
import random
import string

n = int(input("Enter password length: "))

password = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
print(password)

