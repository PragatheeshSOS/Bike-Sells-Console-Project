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
    elif choice == "8":
        print("Exiting...")
        break
    else:
        print("Invalid option! Try again.")