from pyscript import display
# Restaurant Order System using Python Data Types

# String data type
restaurant_name = "Milktea Shop"
owner_name = "Eyl Valeroso"

# Integer data type
year_since = 2067

# Float data type
tax_rate = 0.08  # 8% tax

# Boolean data type
has_delivery = True
is_dine_in = True
is_takeaway = False

# List data type
beverages = ["Milktea", "Choc Milktea", "Strawberry Milktea", "Coffee Milktea", "Milktea w/ IceCream"]

# Tuple data type
business_hours = ("11:00 AM", "10:00 PM")

# Dictionary data type
menu = {
    "Milktea": 79.99,
    "Choc Milktea": 89.00,
    "Strawberry Milktea": 89.00,
    "Coffee Milktea": 89.00,
    "Milktea w/ IceCream": 99.00
}

# Set data type
common_allergens = {"dairy", "nuts"}

# Displaying restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

# Display menu items
display(beverages[0], target="prod1")
display(f"₱{menu['Milktea']:.2f}", target="price1")
display(beverages[1], target="prod2")
display(f"₱{menu['Choc Milktea']:.2f}", target="price2")
display(beverages[2], target="prod3")
display(f"₱{menu['Strawberry Milktea']:.2f}", target="price3")
display(beverages[3], target="prod4")
display(f"₱{menu['Coffee Milktea']:.2f}", target="price4")
display(beverages[4], target="prod5")
display(f"₱{menu['Milktea w/ IceCream']:.2f}", target="price5")

# Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")


# Display order type
display(f"Dine-in Available", target="orderType")

