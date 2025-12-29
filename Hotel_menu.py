menu = {
    'Pizza':90,
    'Pasta':50,
    'Burger':60,
    'Sandwich':80,
    'Coffee':40,
}
print("Welcome to Python Restaurant")
print("Pizza: Rs90\nPasta: Rs50\nBurger: Rs60\nSandwich: Rs80\nCoffee: Rs40")

order_total = 0
another_order = "Yes"

while another_order == "Yes":

    item_1 = input("Enter the name of item you want to order =")

    if item_1 in menu:
        order_total += menu[item_1]
        print(f"Your item {item_1} has been added to your order")
        another_order = input("Do you want to add another item? (Yes/No) ")

    else:
        print(f"Ordered item {item_1} is not avaialable yet!")
        another_order = input("Do you want to add another item? (Yes/No) ")
    
print(f"The total amount of items is {order_total}")