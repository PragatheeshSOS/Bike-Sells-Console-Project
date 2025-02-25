from bike import Bike
from order import Order

class Admin:
    admins = [
        {"email": "admin@example.com", "password": "admin123"}
    ]

    def login(self):
        email = input("Enter admin email: ")
        password = input("Enter password: ")
        for admin in Admin.admins:
            if admin["email"] == email and admin["password"] == password:
                print("Admin login successful!")
                return True
        print("Invalid credentials!")
        return False

    def manage_bikes(self, bikes):
        while True:
            print("\nManage Bikes")
            print("1. View All Bikes")
            print("2. Add New Bike")
            print("3. Update Bike Stock")
            print("4. Delete a Bike")
            print("5. Back to Admin Panel")
            choice = input("Enter your choice: ")

            if choice == '1':
                print("\nAvailable Bikes:")
                for bike in bikes:
                    bike.display_details()

            elif choice == '2':
                bike_id = int(input("Enter Bike ID: "))
                model = input("Enter Model Name: ")
                brand = input("Enter Brand: ")
                price = float(input("Enter Price: "))
                engine_capacity = input("Enter Engine Capacity: ")
                stock = int(input("Enter Stock: "))
                status = "Available" if stock > 0 else "Out of Stock"

                new_bike = Bike(bike_id, model, brand, price, engine_capacity, stock, status)
                bikes.append(new_bike)
                print("New bike added successfully!")

            elif choice == '3':
                bike_id = int(input("Enter Bike ID to update stock: "))
                for bike in bikes:
                    if bike.bike_id == bike_id:
                        new_stock = int(input("Enter new stock quantity: "))
                        bike.stock = new_stock
                        bike.status = "Available" if new_stock > 0 else "Out of Stock"
                        print("Stock updated successfully!")
                        break
                else:
                    print("Bike not found!")

            elif choice == '4':
                bike_id = int(input("Enter Bike ID to delete: "))
                for bike in bikes:
                    if bike.bike_id == bike_id:
                        bikes.remove(bike)
                        print("Bike deleted successfully!")
                        break
                else:
                    print("Bike not found!")

            elif choice == '5':
                break

            else:
                print("Invalid choice! Try again.")

    def view_sales_report(self):
        if not Order.orders:
            print("No sales data available.")
            return

        print("\nSales Report")
        total_sales = 0
        for order in Order.orders:
            print(f"Order ID: {order.order_id}, Customer ID: {order.customer_id}, Bike ID: {order.bike_id}, Quantity: {order.quantity}, Total Price: {order.total_price}, Date: {order.date}")
            total_sales += order.total_price

        print(f"\nTotal Sales: ${total_sales:.2f}")
