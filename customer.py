# customer.py
class Customer:
    customers = []
    
    def __init__(self):
        self.customer_id = None
        self.name = ""
        self.contact = ""
        self.email = ""
        self.password = ""
    
    def register(self):
        self.name = input("Enter your name: ")
        self.contact = input("Enter your contact: ")
        self.email = input("Enter your email: ")
        self.password = input("Create a password: ")
        Customer.customers.append(self)
        print("Registration successful!")
    
    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        for customer in Customer.customers:
            if customer.email == email and customer.password == password:
                print("Login successful!")
                return True
        print("Invalid credentials!")
        return False
    
    def view_bikes(self, bikes):
        for bike in bikes:
            bike.display_details()
    
    def place_order(self, bikes):
        bike_id = int(input("Enter Bike ID to order: "))
        quantity = int(input("Enter quantity: "))
        for bike in bikes:
            if bike.bike_id == bike_id:
                if bike.stock >= quantity:
                    bike.stock -= quantity
                    print(f"Order placed successfully! Remaining stock: {bike.stock}")
                else:
                    print("Not enough stock available!")
                return
        print("Bike not found!")
