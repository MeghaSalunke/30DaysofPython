# Day 3- Challenge 3 Lists (slicing, methods), tuples (immutability), dictionaries (key-value pairs), Sets
#Create an inventory system tracking items and quantities with a dictionary



# Create inventory dictionary
inventory = {}

# Add items
inventory["Apple"] = 10
inventory["Banana"] = 25
inventory["Orange"] = 15

# Update quantity
inventory["Apple"] += 5      # Added 5 apples
inventory["Banana"] -= 3     # Sold 3 bananas

# Display inventory
print("Inventory:")
for item, quantity in inventory.items():
    print(item, ":", quantity)
