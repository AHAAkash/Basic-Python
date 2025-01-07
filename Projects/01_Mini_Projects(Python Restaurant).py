#Define the Menu of RESTAURANT..
menu = {
    'Pizza': 60,
    'Pasta': 40,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}

#Greetings..
print("Welcome to Python Restaurant")
print("pizza: 60 Tk\nPasta: 40 Tk\nBurger: 60 Tk\nsalad: 70 Tk\ncoffee: 80 Tk")

order_total = 0

while True:
    item = input("Enter the item you want to order: ")
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order")
    else:
        print("Sorry, we don't have that item on the menu")

    another_order = input("Do you want to add another item? (yes/no): ")
    if another_order.lower() != 'yes':
        break

print(f"The total amount to pay is {order_total} Tk")
