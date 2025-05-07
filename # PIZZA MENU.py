# PIZZA MENU


menu = {
    "pizza": 100,
    "burger": 50,
    "pasta": 40,
    "coffee": 60,
}

print("Welcome to my restaurant") 
print("Menu:")
for item, price in menu.items():
    print(f"{item.capitalize()} : Rs.{price}")

order_total = 0

item_1 = input("Enter the name of the item: ").lower()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Sorry, '{item_1}' is not available.")

another_order = input("Do you want to add another item? (Yes/No): ").lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").lower()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item '{item_2}' has been added to your order.")
    else:
        print(f"Sorry, '{item_2}' is not available.")

print(f"The total amount to pay is Rs.{order_total}")
print("THANK YOU VISIT AGAIN ")
