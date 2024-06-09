'''Using the given dictionary, update it according to the following: 

Add a new category called "Beverages" with at least two items.
Update the price of "Steak" to 17.99.
Remove "Bruschetta" from "Starters".'''

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add a new category called "Beverages" with at least two items.

restaurant_menu["Beverages"] = {"Dr.Pepper": 3.99, "Lemonade": 2.99}
print(restaurant_menu)

# Update the price of "Steak" to 17.99.

restaurant_menu["Main Course"]["Steak"] = 17.99
print(restaurant_menu)

# Remove "Bruschetta" from "Starters".
del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)

