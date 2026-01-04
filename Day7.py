# Day 7 Challenge 7  Reading/writing files, handling text and CSV
# Count word frequencies in a text file
from collections import Counter

with open("Assests\MY TESTIMONIAL.txt", "r") as file:
    words = file.read().lower().split()

word_count = Counter(words)

for word, count in word_count.items():
    print(word, count)
