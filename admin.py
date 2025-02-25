from bike import Bike
from order import Order
class Admin:
    admins = [{"email":"asd@gmail.com","password":"asd123"}]
    def login(self):
        email = input("Enter Your Email ID: ")
        password = input("Enter Your Password: ")
        for admin in Admin.admins:
            if admin["email"] == email and admin["password"] == password:
                print("Admin Login Successful!")
                return True
        print("Enter Correct Email ID And Password!")
        return False
    def manage_bikes(self,bikes):
        while True:
            print("\nManage Bikes")
            print("1. View All Bikes")
            print("2. Add New Bike")
            print("3. Update Bike Stock")
            print("4. Delete a Bike")
            print("5. Back to Admin Panel")
            choice = input("Enter Your Choice: ")
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
                mileage = float(input("Enter Mileage: "))
                stock = int(input("Enter Stock: "))
                status = "Available" if stock > 0 else "Out of Stock"
                new_bike = Bike(bike_id, model, brand, price, engine_capacity, mileage, stock, status)
                bikes.append(new_bike)
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
                for bike in bikes:
                    if bike.bike_id == bike_id:
                        bikes.remove(bike)
                        print("Bike Deleted Successfully!")
                        break
                else:
                    print("Enter Correct Bike ID To Delete!")
            elif choice == '5':
                break
            else:
                print("Invalid Choice. Try Again!")
    def view_sales_report(self):
        if not Order.orders:
            print("Sales Data Unavailable!")
            return
        print("\nSales Report")
        total_sales = 0
        for order in Order.orders:
            print(f"Order ID: {order.order_id}, Customer ID: {order.customer_id}, Bike ID: {order.bike_id}, Quantity: {order.quantity}, Total Price: {order.total_price}, Date: {order.date}")
            total_sales += order.total_price
        print(f"\nTotal Sales: ${total_sales:.2f}")
