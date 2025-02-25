from admin import Admin
from customer import Customer
from bike import Bike
from order import Order
from payment import Payment

bikes = [
    Bike(1, "Model X", "Brand A", 1500.0, "150cc", 10, "Available"),
    Bike(2, "Model Y", "Brand B", 2000.0, "200cc", 5, "Available")
]

def main():
    while True:
        print("\nBike Sales Management System")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Customer Registration")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            admin = Admin()
            if admin.login():
                while True:
                    print("\nAdmin Panel")
                    print("1. Manage Bikes")
                    print("2. View Sales Report")
                    print("3. Logout")
                    admin_choice = input("Enter your choice: ")
                    
                    if admin_choice == '1':
                        admin.manage_bikes()
                    elif admin_choice == '2':
                        admin.view_sales_report()
                    elif admin_choice == '3':
                        break
                    else:
                        print("Invalid choice! Try again.")
        
        elif choice == '2':
            customer = Customer()
            if customer.login():
                while True:
                    print("\nCustomer Panel")
                    print("1. View Bikes")
                    print("2. Place Order")
                    print("3. Logout")
                    customer_choice = input("Enter your choice: ")
                    
                    if customer_choice == '1':
                        customer.view_bikes(bikes)
                    elif customer_choice == '2':
                        customer.place_order(bikes)
                    elif customer_choice == '3':
                        break
                    else:
                        print("Invalid choice! Try again.")
        
        elif choice == '3':
            customer = Customer()
            customer.register()
        
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
