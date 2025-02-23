from bike import Bike
from customer import Customer
from order import Order
from admin import Admin
from payment import Payment

bikes = [Bike(1, "YZF R15", "Yamaha", 200000, "155cc", 5, "Available"),Bike(2, "Ninja 300", "Kawasaki", 500000, "300cc", 3, "Available")]
customers = []
admin = Admin(1, "Admin", "admin123")

while True:
    print("\n1. View Bikes\n2. Register Customer\n3. Login Customer\n4. Place Order\n5. View Orders\n6. Cancel Order\n7. Admin Panel\n8. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        print("\n\n--- BIKE DETAILS ---")
        for bike in bikes:
            bike.displayDetails()
    elif choice == "2":
        name = input("Enter Name: ")
        contact = input("Enter Contact: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        customer = Customer(len(customers) + 1, name, contact, email, password)
        customers.append(customer)
        customer.register()
    elif choice == "3":
        # Customer.login() pending............
        print(3)
    elif choice == "4":
        #pending.........
        print(4)
    elif choice == "5":
        #pending.........
        print(5)
    elif choice == "6":
        #pending.........
        print(6)
    elif choice == "7":
        #pending.........
        print(7)
    elif choice == "8":
        print("Why So Soon.........")
        break
    else:
        print("Invalid option! Try again.")