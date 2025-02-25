from admin import Admin
from customer import Customer
from bike import Bike
from order import Order

bikes = [
    Bike(1, "R15", "Yamaha", 1500, "150cc", 40, 5, "Available"),
    Bike(2, "Pulsar", "Bajaj", 1300, "160cc", 35, 3, "Available"),
]

admin = Admin()
customer = Customer()

while True:
    print("\n----- HAPPY TO SEE YOU HERE -----")
    print("1. Admin Login\n2. Customer Registration\n3. Customer Login\n4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        if admin.login():
            admin.manage_bikes(bikes)
    elif choice == "2":
        customer.register()
    elif choice == "3":
        if customer.login():
            customer.view_bikes(bikes)
            bike, quantity = customer.place_order(bikes)
            if bike:
                Order(customer.customer_id, bike, quantity)
    elif choice == "4":
        print("Exiting system...")
        break
    else:
        print("Invalid choice. Try again.")