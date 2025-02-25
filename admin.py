from bike import Bike
from order import Order

class Admin:
    admins = [{"email": "asd@gmail.com", "password": "asd123"}]

    def login(self):
        email, password = input("Enter Your Email ID: "), input("Enter Your Password: ")
        for admin in Admin.admins:
            if admin["email"] == email and admin["password"] == password:
                print("Admin Login Successful!")
                return True
        print("Enter Correct Email ID And Password!")
        return False

    def manage_bikes(self, bikes):
        while True:
            print("\nManage Bikes\n1. View All Bikes\n2. Add New Bike\n3. Update Bike Stock\n4. Delete a Bike\n5. Back to Admin Panel")
            choice = input("Enter Your Choice: ")
            if choice == '1':
                print("\n----- Available Bikes -----")
                for bike in bikes:
                    bike.display_details()
            elif choice == '2':
                stock = int(input("Enter Stock: "))
                bikes.append(Bike(int(input("Enter Bike ID: ")), input("Enter Model Name: "), input("Enter Brand: "), float(input("Enter Price: ")), input("Enter Engine Capacity: "), float(input("Enter Mileage: ")), stock, "Available" if stock > 0 else "Out of Stock"))
                print("New Bike Added Successfully!")
            elif choice == '3':
                bike_id = int(input("Enter Bike ID To Update Stock: "))
                for bike in bikes:
                    if bike.bike_id == bike_id:
                        new_stock = int(input("Enter New Stock Quantity: "))
                        bike.stock = new_stock
                        bike.status = "Available" if new_stock > 0 else "Out of Stock"
                        print("Stock updated successfully!")
                        break
                else:
                    print("Enter Correct Bike ID To Update!")
            elif choice == '4':
                bike_id = int(input("Enter Bike ID To Delete: "))
                check_id = 0
                for bike in bikes:
                    if bike.bike_id == bike_id:
                        bikes.remove(bike)
                        check_id = 1
                        break
                print("Enter Correct Bike ID To Delete!") if check_id == 0 else print("Bike Deleted Successfully!")
            elif choice == '5':
                break
            else:
                print("Invalid Choice. Try Again!")

    def view_sales_report(self):
        if not Order.orders:
            print("Sales Data Unavailable!")
            return
        print("\n----- Sales Report -----")
        total = 0
        for order in Order.orders:
            print(f"Order ID: {order.order_id} | Customer ID: {order.customer_id} | Bike Model: {order.bike.model} | Quantity: {order.quantity} | Total Price: {order.total_price} | Date: {order.date}")
            total += order.total_price
        print(f"\nTotal Sales: ${total:.2f}")
