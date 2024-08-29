'''   
Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

Problem Statement: You are given a list of tuples, each representing a customer's order. 
Each tuple contains the customer's name, the product ordered, and the quantity. 
Your task is to unpack each tuple and print the order details in a user-friendly format.

Sample Order Data:
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

- Write a function to iterate over the list of orders. - Unpack each tuple in the list and format the details for display.
'''


orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Tyler", "Video Game", 3),
    ("Noah", "Phone", 1),
    ("Arielle", "Phone Case", 2)
]


def display_orders(list): 
    print("Current Orders: ")
    for index, order in enumerate(list): # for loop to iterate through each tuple in list
        name = order[0]     # set first index [0] to name to make print statement cleaner
        product = order[1]  # same as above
        quantity = order[2] # same as above 
        if quantity > 1: 
            print(f"Order {index + 1}: {quantity} {product}'s for {name}")
        else: 
            print(f"Order {index + 1}: {quantity} {product} for {name}")    

display_orders(orders) 
